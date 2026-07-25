#!/usr/bin/env python3
"""Run severity-ranked checks on a standalone HTML presentation."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


PLACEHOLDER = re.compile(r"(?:REPLACE_WITH_|\b(?:TODO|LOREM IPSUM)\b)", re.IGNORECASE)
CSS_URL = re.compile(r"url\(\s*(['\"]?)([^'\")]+)\1\s*\)", re.IGNORECASE)


def srcset_urls(value: str) -> list[str]:
    """Return candidate URLs from a conventional comma-separated srcset."""
    if re.search(r"(?:^|,\s*)data:", value, re.IGNORECASE):
        return []
    urls: list[str] = []
    for candidate in value.split(","):
        parts = candidate.strip().split()
        if parts and parts[0]:
            urls.append(parts[0])
    return urls


def warning_priority(message: str) -> str:
    """Map non-blocking checks to the quality model in references/quality-checks.md."""
    p1_markers = (
        "Heading level jumps",
        "SVG image(s)",
        "Motion detected",
        "Clickable <div>",
        "Effects-heavy page",
        "Live map detected",
    )
    return "P1" if message.startswith(p1_markers) else "P2"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[str] = []
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.refs: list[tuple[str, str]] = []
        self.headings: list[int] = []
        self.images_without_alt = 0
        self.unlabelled_image_svgs = 0
        self.has_viewport = False
        self.has_title = False
        self.lang: str | None = None
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(tag)
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)
        if tag == "html":
            self.lang = values.get("lang")
        if tag == "title":
            self._in_title = True
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
        if tag == "meta" and values.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag == "img" and "alt" not in values:
            self.images_without_alt += 1
        if (
            tag == "svg"
            and values.get("aria-hidden", "").lower() != "true"
            and values.get("role", "").lower() == "img"
            and not values.get("aria-label")
            and not values.get("aria-labelledby")
        ):
            self.unlabelled_image_svgs += 1
        for attribute in ("src", "href", "poster"):
            value = values.get(attribute)
            if value:
                self.refs.append((attribute, value))
        srcset = values.get("srcset")
        if srcset:
            self.refs.extend(("srcset", value) for value in srcset_urls(srcset))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title and data.strip():
            self.has_title = True


def local_target(page: Path, ref: str) -> Path | None:
    parsed = urlparse(ref)
    if parsed.scheme or parsed.netloc or ref.startswith(("#", "data:", "mailto:", "tel:")):
        return None
    return (page.parent / unquote(parsed.path)).resolve()


def check(page: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not page.is_file():
        return [f"File not found: {page}"], warnings

    text = page.read_text(encoding="utf-8")
    parser = PageParser()
    try:
        parser.feed(text)
    except Exception as exc:  # HTMLParser errors are uncommon but actionable.
        errors.append(f"Could not parse HTML: {exc}")
        return errors, warnings

    parser.refs.extend(("css url", value) for _, value in CSS_URL.findall(text))

    if "html" not in parser.tags or "body" not in parser.tags:
        errors.append("Missing <html> or <body> element")
    if not parser.lang:
        errors.append("Missing lang attribute on <html>")
    if not parser.has_title:
        errors.append("Missing a non-empty <title>")
    if not parser.has_viewport:
        errors.append("Missing viewport meta tag")
    if "main" not in parser.tags:
        errors.append("Missing <main> landmark")
    if 1 not in parser.headings:
        errors.append("Missing primary <h1> heading")
    elif parser.headings.count(1) > 1:
        warnings.append("Multiple <h1> headings found; confirm there is one clear page title")
    for previous, current in zip(parser.headings, parser.headings[1:]):
        if current > previous + 1:
            warnings.append(f"Heading level jumps from h{previous} to h{current}")
    if parser.duplicate_ids:
        errors.append("Duplicate id value(s): " + ", ".join(sorted(parser.duplicate_ids)))
    if parser.images_without_alt:
        errors.append(f"{parser.images_without_alt} image(s) have no alt attribute")
    if parser.unlabelled_image_svgs:
        warnings.append(
            f"{parser.unlabelled_image_svgs} SVG image(s) have no aria-label or aria-labelledby"
        )
    if PLACEHOLDER.search(text):
        errors.append("Template placeholder text remains")

    for attribute, ref in parser.refs:
        if ref.startswith("#") and ref[1:] not in parser.ids:
            errors.append(f"Broken fragment {attribute}: {ref}")
        target = local_target(page, ref)
        if target is not None and not target.exists():
            errors.append(f"Broken local {attribute}: {ref}")

    remote_refs = sorted(
        {
            ref
            for _, ref in parser.refs
            if urlparse(ref).scheme.lower() in {"http", "https"}
        }
    )
    if remote_refs:
        warnings.append(
            f"{len(remote_refs)} remote asset or link reference(s) found; confirm offline behavior and provenance"
        )

    if "prefers-reduced-motion" not in text and any(
        token in text for token in ("animation:", "transition:", "scroll-behavior:")
    ):
        warnings.append("Motion detected without a prefers-reduced-motion rule")
    has_continuous_effects = bool(
        re.search(
            r"requestAnimationFrame\s*\(|getContext\s*\(\s*['\"]webgl",
            text,
            re.IGNORECASE,
        )
    )
    has_static_control = bool(
        re.search(
            r"data-(?:effects|static)-toggle|(?:effects|static)-toggle|low-power|static-mode",
            text,
            re.IGNORECASE,
        )
    )
    if has_continuous_effects and not has_static_control:
        warnings.append(
            "Effects-heavy page has no detectable manual static-mode control"
        )
    has_live_map = bool(
        re.search(r"\b(?:maplibregl|leaflet|L\.map\s*\()", text, re.IGNORECASE)
    )
    if has_live_map and not re.search(r"data-map-fallback\b", text, re.IGNORECASE):
        warnings.append(
            "Live map detected without a data-map-fallback static representation"
        )
    if "@media print" not in text:
        warnings.append("No print stylesheet found (recommended for report-like pages)")
    if re.search(r"<div[^>]+onclick=", text, re.IGNORECASE):
        warnings.append("Clickable <div> found; prefer a keyboard-accessible button or link")

    return sorted(set(errors)), sorted(set(warnings))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="HTML file to inspect")
    args = parser.parse_args()
    errors, warnings = check(args.html.resolve())

    for item in errors:
        print(f"ERROR [P0]: {item}")
    for item in warnings:
        print(f"WARNING [{warning_priority(item)}]: {item}")
    if not errors and not warnings:
        print("OK: basic HTML presentation checks passed")
    elif not errors:
        print("OK: passed with warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
