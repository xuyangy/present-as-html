#!/usr/bin/env python3
"""Render an HTML page at several viewports and report browser-level failures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


DEFAULT_VIEWPORTS = "375x812,768x1024,1440x1000"


def parse_viewports(raw: str) -> list[tuple[int, int]]:
    viewports: list[tuple[int, int]] = []
    for item in raw.split(","):
        item = item.strip().lower()
        try:
            width_text, height_text = item.split("x", 1)
            width, height = int(width_text), int(height_text)
        except ValueError as exc:
            raise argparse.ArgumentTypeError(
                f"Invalid viewport {item!r}; use WIDTHxHEIGHT"
            ) from exc
        if width < 240 or height < 240:
            raise argparse.ArgumentTypeError(
                f"Viewport {item!r} is too small for a useful review"
            )
        viewports.append((width, height))
    if not viewports:
        raise argparse.ArgumentTypeError("At least one viewport is required")
    return viewports


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="Local HTML file to review")
    parser.add_argument(
        "--out",
        type=Path,
        help="Output directory (default: <page-directory>/review-html)",
    )
    parser.add_argument(
        "--viewports",
        default=DEFAULT_VIEWPORTS,
        help=f"Comma-separated WIDTHxHEIGHT values (default: {DEFAULT_VIEWPORTS})",
    )
    parser.add_argument(
        "--modes",
        choices=("normal", "reduced", "print", "both", "all"),
        default="both",
        help=(
            "Capture normal, reduced-motion, print, both normal/reduced, "
            "or all three (default: both)"
        ),
    )
    parser.add_argument(
        "--no-scroll",
        dest="scroll",
        action="store_false",
        help=(
            "Skip the scroll pass. By default the page is scrolled to the bottom "
            "and back before inspection so IntersectionObserver reveals fire; "
            "without it, scroll-revealed sections are captured still hidden."
        ),
    )
    parser.add_argument(
        "--no-contact-sheet",
        dest="contact_sheet",
        action="store_false",
        help=(
            "Skip contact-sheet.png. By default one sheet tiles the above-the-fold "
            "view of every mode and viewport, so a single image read replaces one "
            "read per capture."
        ),
    )
    parser.add_argument(
        "--wait-ms",
        type=int,
        default=900,
        help="Wait after load before inspection (default: 900)",
    )
    parser.add_argument(
        "--timeout-ms",
        type=int,
        default=15000,
        help="Navigation timeout (default: 15000)",
    )
    return parser


TILE_HEIGHT = 460


def build_contact_sheet(browser, output_dir: Path, results: list[dict[str, Any]]) -> Path | None:
    """Tile every above-the-fold capture into one PNG.

    One image read then replaces one read per capture. The sheet is a squint
    test: it shows opening composition, colour scheme, and gross layout across
    modes and widths. Open the individual full-page captures for craft detail.
    """
    tiles = [item for item in results if item.get("fold")]
    if not tiles:
        return None

    rows: dict[str, list[dict[str, Any]]] = {}
    for item in tiles:
        rows.setdefault(item["mode"], []).append(item)

    def cell(item: dict[str, Any]) -> str:
        width, height = item["viewport"]["width"], item["viewport"]["height"]
        scaled = max(80, round(TILE_HEIGHT * width / height))
        flags = []
        if item["horizontalOverflow"]:
            flags.append("OVERFLOW")
        if item["hiddenContent"]:
            flags.append(f"{len(item['hiddenContent'])} HIDDEN")
        if item["consoleErrors"] or item["pageErrors"]:
            flags.append("JS ERROR")
        badge = (
            f'<b class="flag">{" · ".join(flags)}</b>' if flags else '<b class="ok">ok</b>'
        )
        return (
            f'<figure style="width:{scaled}px">'
            f'<img src="{Path(item["fold"]).name}" width="{scaled}" height="{TILE_HEIGHT}" alt="">'
            f'<figcaption>{width}&times;{height} {badge}</figcaption>'
            f"</figure>"
        )

    body = "".join(
        f'<section><h2>{mode}</h2><div class="row">'
        + "".join(cell(item) for item in items)
        + "</div></section>"
        for mode, items in rows.items()
    )
    sheet_html = output_dir / "contact-sheet.html"
    sheet_html.write_text(
        "<!doctype html><meta charset='utf-8'><style>"
        "body{margin:0;padding:14px;background:#20242a;color:#e8edf2;"
        "font:12px/1.4 ui-sans-serif,system-ui,sans-serif}"
        "section{margin-bottom:14px}"
        "h2{margin:0 0 6px;font:600 11px/1 ui-monospace,monospace;"
        "letter-spacing:.14em;text-transform:uppercase;color:#8fa3b0}"
        ".row{display:flex;gap:10px;align-items:flex-start}"
        "figure{margin:0}"
        "img{display:block;border:1px solid #3a444e;object-fit:cover;object-position:top}"
        "figcaption{padding-top:4px;font:11px/1.3 ui-monospace,monospace;color:#8fa3b0}"
        ".flag{color:#ffb45c}.ok{color:#7fd6a2;font-weight:400}"
        "</style>" + body,
        encoding="utf-8",
    )

    page = browser.new_page(viewport={"width": 1600, "height": 900})
    page.goto(sheet_html.as_uri(), wait_until="load")
    page.wait_for_timeout(250)
    sheet_png = output_dir / "contact-sheet.png"
    page.locator("body").screenshot(path=str(sheet_png))
    page.close()
    sheet_html.unlink(missing_ok=True)
    return sheet_png


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    page_path = args.html.expanduser().resolve()
    if not page_path.is_file():
        print(f"ERROR: file not found: {page_path}", file=sys.stderr)
        return 2

    try:
        viewports = parse_viewports(args.viewports)
    except argparse.ArgumentTypeError as exc:
        parser.error(str(exc))

    try:
        from playwright.sync_api import Error as PlaywrightError
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "Playwright is unavailable. Install the Python package and Chromium "
            "in the current environment, or use a runtime-native browser tool.",
            file=sys.stderr,
        )
        return 2

    output_dir = (args.out or page_path.parent / "review-html").expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    if args.modes == "both":
        modes = ("normal", "reduced")
    elif args.modes == "all":
        modes = ("normal", "reduced", "print")
    else:
        modes = (args.modes,)
    results: list[dict[str, Any]] = []

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            for mode in modes:
                for width, height in viewports:
                    page = browser.new_page(viewport={"width": width, "height": height})
                    if mode == "reduced":
                        page.emulate_media(reduced_motion="reduce")
                    elif mode == "print":
                        page.emulate_media(media="print", reduced_motion="reduce")

                    console_errors: list[str] = []
                    page_errors: list[str] = []
                    failed_requests: list[str] = []
                    page.on(
                        "console",
                        lambda message, sink=console_errors: (
                            sink.append(message.text) if message.type == "error" else None
                        ),
                    )
                    page.on("pageerror", lambda error, sink=page_errors: sink.append(str(error)))
                    page.on(
                        "requestfailed",
                        lambda request, sink=failed_requests: sink.append(
                            f"{request.url}: {request.failure}"
                        ),
                    )

                    page.goto(
                        page_path.as_uri(),
                        wait_until="load",
                        timeout=args.timeout_ms,
                    )
                    page.evaluate(
                        """async () => {
                          if (document.fonts?.ready) await document.fonts.ready;
                          await new Promise(resolve => requestAnimationFrame(
                            () => requestAnimationFrame(resolve)
                          ));
                        }"""
                    )
                    if args.scroll:
                        # Scroll-revealed sections stay at opacity 0 until an
                        # IntersectionObserver fires. Walk the page so the captures
                        # and the hidden-content check see the settled state.
                        page.evaluate(
                            """async () => {
                              const pause = ms => new Promise(r => setTimeout(r, ms));
                              const step = Math.max(200, window.innerHeight * 0.8);
                              let y = 0;
                              for (let guard = 0; guard < 400; guard += 1) {
                                const limit = document.documentElement.scrollHeight;
                                if (y >= limit) break;
                                window.scrollTo(0, y);
                                await pause(50);
                                y += step;
                              }
                              window.scrollTo(0, 0);
                              await pause(150);
                            }"""
                        )
                    page.wait_for_timeout(max(0, args.wait_ms))
                    metrics = page.evaluate(
                        """() => {
                          const root = document.documentElement;
                          const body = document.body;
                          const visible = element => {
                            const style = getComputedStyle(element);
                            return style.display !== 'none' &&
                              style.visibility !== 'hidden' &&
                              element.getClientRects().length > 0;
                          };
                          const identify = element => {
                            const id = element.id ? `#${element.id}` : '';
                            const classes = [...element.classList].slice(0, 2)
                              .map(name => `.${name}`).join('');
                            return `${element.tagName.toLowerCase()}${id}${classes}`;
                          };
                          const accessibleName = element => {
                            const aria = element.getAttribute('aria-label')?.trim();
                            if (aria) return aria;
                            const labelledby = element.getAttribute('aria-labelledby');
                            if (labelledby) {
                              const text = labelledby.split(/\\s+/)
                                .map(id => document.getElementById(id)?.textContent || '')
                                .join(' ').trim();
                              if (text) return text;
                            }
                            if (element.labels?.length) {
                              const text = [...element.labels]
                                .map(label => label.textContent || '').join(' ').trim();
                              if (text) return text;
                            }
                            const mediaName = element.querySelector(
                              'img[alt], svg[aria-label], svg title'
                            );
                            if (mediaName) {
                              const mediaLabel = mediaName.getAttribute?.('alt') ||
                                mediaName.getAttribute?.('aria-label') ||
                                mediaName.textContent || '';
                              if (mediaLabel.trim()) return mediaLabel.trim();
                            }
                            return (
                              element.getAttribute('alt') ||
                              element.textContent ||
                              element.getAttribute('title') ||
                              ((element.type === 'submit' || element.type === 'button')
                                ? element.value : '') || ''
                            ).trim();
                          };
                          const brokenImages = [...document.images]
                            .filter(visible)
                            .filter(image => !image.complete || image.naturalWidth === 0)
                            .map(image => ({
                              element: identify(image),
                              src: image.currentSrc || image.src || '(empty)',
                              complete: image.complete,
                              naturalWidth: image.naturalWidth,
                              naturalHeight: image.naturalHeight,
                            }));
                          const unnamedControls = [...document.querySelectorAll(
                            'button, a[href], input:not([type="hidden"]), select, textarea'
                          )]
                            .filter(visible)
                            .filter(element => !accessibleName(element))
                            .map(identify);
                          // Substantial blocks left effectively invisible after the
                          // page has settled: a reveal whose observer never fired, or
                          // content gated behind script that did not run. Deliberate
                          // disclosure (details, dialog, hidden, aria-hidden) is exempt,
                          // and the threshold is opacity 0.05 so mid-transition
                          // elements are not reported.
                          const reported = [];
                          const hiddenContent = [...document.querySelectorAll(
                            'main *, article *, section *'
                          )]
                            .filter(element => {
                              const rect = element.getBoundingClientRect();
                              if (rect.width * rect.height < 15000) return false;
                              const style = getComputedStyle(element);
                              if (style.display === 'none') return false;
                              return parseFloat(style.opacity) < 0.05 ||
                                style.visibility === 'hidden';
                            })
                            .filter(element => !element.closest(
                              '[hidden], [aria-hidden="true"], details:not([open]), ' +
                              'dialog:not([open])'
                            ))
                            .filter(element => {
                              // keep only the outermost element of each hidden subtree
                              if (reported.some(seen => seen.contains(element))) return false;
                              reported.push(element);
                              return true;
                            })
                            .slice(0, 12)
                            .map(identify);
                          return {
                            hiddenContent,
                            title: document.title,
                            viewportWidth: root.clientWidth,
                            documentWidth: Math.max(root.scrollWidth, body?.scrollWidth || 0),
                            documentHeight: Math.max(root.scrollHeight, body?.scrollHeight || 0),
                            brokenImages,
                            unnamedControls,
                          };
                        }"""
                    )
                    overflow = metrics["documentWidth"] > metrics["viewportWidth"] + 1
                    screenshot = output_dir / f"{mode}-{width}x{height}.png"
                    page.screenshot(path=str(screenshot), full_page=True)
                    fold = None
                    if args.contact_sheet:
                        fold = output_dir / f"{mode}-{width}x{height}-fold.png"
                        page.screenshot(path=str(fold), full_page=False)
                    results.append(
                        {
                            "mode": mode,
                            "viewport": {"width": width, "height": height},
                            "screenshot": str(screenshot),
                            "fold": str(fold) if fold else None,
                            "metrics": metrics,
                            "horizontalOverflow": overflow,
                            "hiddenContent": metrics.pop("hiddenContent"),
                            "brokenImages": metrics.pop("brokenImages"),
                            "unnamedControls": metrics.pop("unnamedControls"),
                            "consoleErrors": sorted(set(console_errors)),
                            "pageErrors": sorted(set(page_errors)),
                            "failedRequests": sorted(set(failed_requests)),
                        }
                    )
                    page.close()
            sheet = build_contact_sheet(browser, output_dir, results) if args.contact_sheet else None
            browser.close()
    except PlaywrightError as exc:
        print(f"Browser review could not run: {exc}", file=sys.stderr)
        return 2

    failures = sum(
        bool(item["horizontalOverflow"])
        + len(item["hiddenContent"])
        + len(item["brokenImages"])
        + len(item["unnamedControls"])
        + len(item["consoleErrors"])
        + len(item["pageErrors"])
        + len(item["failedRequests"])
        for item in results
    )
    report = {
        "page": str(page_path),
        "viewports": [f"{width}x{height}" for width, height in viewports],
        "modes": list(modes),
        "scrolled": bool(args.scroll),
        "contactSheet": str(sheet) if sheet else None,
        "failures": failures,
        "results": results,
    }
    report_path = output_dir / "review-report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")

    if sheet:
        print(f"Contact sheet (read this first): {sheet}")
    if failures:
        print(f"REVIEW FAILED: {failures} browser finding(s); see {report_path}")
        return 1
    print(f"REVIEW OK: {len(results)} captures; report: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
