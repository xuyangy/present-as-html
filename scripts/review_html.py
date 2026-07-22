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
                          return {
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
                    results.append(
                        {
                            "mode": mode,
                            "viewport": {"width": width, "height": height},
                            "screenshot": str(screenshot),
                            "metrics": metrics,
                            "horizontalOverflow": overflow,
                            "brokenImages": metrics.pop("brokenImages"),
                            "unnamedControls": metrics.pop("unnamedControls"),
                            "consoleErrors": sorted(set(console_errors)),
                            "pageErrors": sorted(set(page_errors)),
                            "failedRequests": sorted(set(failed_requests)),
                        }
                    )
                    page.close()
            browser.close()
    except PlaywrightError as exc:
        print(f"Browser review could not run: {exc}", file=sys.stderr)
        return 2

    failures = sum(
        bool(item["horizontalOverflow"])
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
        "failures": failures,
        "results": results,
    }
    report_path = output_dir / "review-report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")

    if failures:
        print(f"REVIEW FAILED: {failures} browser finding(s); see {report_path}")
        return 1
    print(f"REVIEW OK: {len(results)} captures; report: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
