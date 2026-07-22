#!/usr/bin/env python3
"""Run lightweight checks on a standalone HTML presentation."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


PLACEHOLDER = re.compile(r"(?:REPLACE_WITH_|\b(?:TODO|LOREM IPSUM)\b)", re.IGNORECASE)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[str] = []
        self.ids: set[str] = set()
        self.refs: list[tuple[str, str]] = []
        self.images_without_alt = 0
        self.has_viewport = False
        self.has_title = False
        self._in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(tag)
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)
        if tag == "title":
            self._in_title = True
        if tag == "meta" and values.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag == "img" and "alt" not in values:
            self.images_without_alt += 1
        for attribute in ("src", "href", "poster"):
            value = values.get(attribute)
            if value:
                self.refs.append((attribute, value))

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

    if "html" not in parser.tags or "body" not in parser.tags:
        errors.append("Missing <html> or <body> element")
    if not parser.has_title:
        errors.append("Missing a non-empty <title>")
    if not parser.has_viewport:
        errors.append("Missing viewport meta tag")
    if parser.images_without_alt:
        errors.append(f"{parser.images_without_alt} image(s) have no alt attribute")
    if PLACEHOLDER.search(text):
        errors.append("Template placeholder text remains")

    for attribute, ref in parser.refs:
        target = local_target(page, ref)
        if target is not None and not target.exists():
            errors.append(f"Broken local {attribute}: {ref}")

    if "prefers-reduced-motion" not in text and any(
        token in text for token in ("animation:", "transition:", "scroll-behavior:")
    ):
        warnings.append("Motion detected without a prefers-reduced-motion rule")
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
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARNING: {item}")
    if not errors and not warnings:
        print("OK: basic HTML presentation checks passed")
    elif not errors:
        print("OK: passed with warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

