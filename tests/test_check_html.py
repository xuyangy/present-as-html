from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_html import check, srcset_urls  # noqa: E402


BASE = """<!doctype html>
<html lang="en">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Example</title>
  <style>@media print { body { color: black; } }</style>
</head>
<body>
  <main><h1>Example</h1>{content}</main>
</body>
</html>
"""


class CheckHtmlTests(unittest.TestCase):
    def run_check(
        self,
        content: str = "",
        local_files: tuple[str, ...] = (),
    ) -> tuple[list[str], list[str]]:
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "index.html"
            for filename in local_files:
                (page.parent / filename).write_bytes(b"fixture")
            page.write_text(BASE.replace("{content}", content), encoding="utf-8")
            return check(page)

    def test_minimal_document_passes_without_findings(self) -> None:
        errors, warnings = self.run_check("<p>Complete source content.</p>")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_data_url_first_srcset_checks_later_local_candidate(self) -> None:
        errors, _ = self.run_check(
            '<img alt="" srcset="data:image/png;base64,AAAA 1x, missing.png 2x">'
        )
        self.assertIn("Broken local srcset: missing.png", errors)

    def test_data_url_after_local_srcset_is_not_treated_as_a_path(self) -> None:
        errors, _ = self.run_check(
            '<img alt="" srcset="present.png 1x, data:image/png;base64,AAAA 2x">',
            local_files=("present.png",),
        )
        self.assertEqual(errors, [])

    def test_descriptorless_data_url_checks_later_local_candidate(self) -> None:
        errors, _ = self.run_check(
            '<img alt="" srcset="data:image/png;base64,AAAA, missing.png 2x">'
        )
        self.assertIn("Broken local srcset: missing.png", errors)

    def test_data_srcset_separator_does_not_require_whitespace(self) -> None:
        self.assertEqual(
            srcset_urls("data:image/png;base64,AAAA 1x,b.png 2x"),
            ["data:image/png;base64,AAAA", "b.png"],
        )

    def test_commas_inside_srcset_url_are_not_separators(self) -> None:
        data_url = (
            "data:image/svg+xml,%3Csvg%20viewBox=%220,0,10,10%22%3E%3C/svg%3E"
        )
        self.assertEqual(
            srcset_urls(f"{data_url} 1x, b.png 2x"),
            [data_url, "b.png"],
        )

    def test_svg_title_counts_as_an_accessible_name(self) -> None:
        errors, warnings = self.run_check(
            '<svg role="img"><title>Process overview</title><path d="M0 0h1"></path></svg>'
        )
        self.assertEqual(errors, [])
        self.assertFalse(any("SVG image(s)" in item for item in warnings))

    def test_unlabelled_svg_is_reported_even_without_role(self) -> None:
        _, warnings = self.run_check('<svg><path d="M0 0h1"></path></svg>')
        self.assertIn(
            "1 SVG image(s) are neither labelled nor aria-hidden",
            warnings,
        )

    def test_svg_title_attribute_is_not_treated_as_an_accessible_name(self) -> None:
        _, warnings = self.run_check(
            '<svg title="Advisory text"><path d="M0 0h1"></path></svg>'
        )
        self.assertIn(
            "1 SVG image(s) are neither labelled nor aria-hidden",
            warnings,
        )

    def test_svg_title_does_not_replace_document_title(self) -> None:
        html = BASE.replace(
            "{content}",
            '<svg role="img"><title>Diagram title</title></svg>',
        ).replace("<title>Example</title>", "")
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "index.html"
            page.write_text(html, encoding="utf-8")
            errors, _ = check(page)
        self.assertIn("Missing a non-empty <title>", errors)

    def test_document_title_is_recognized_when_head_start_tag_is_omitted(self) -> None:
        html = BASE.replace("<head>", "").replace("</head>", "")
        with tempfile.TemporaryDirectory() as directory:
            page = Path(directory) / "index.html"
            page.write_text(html.replace("{content}", ""), encoding="utf-8")
            errors, _ = check(page)
        self.assertNotIn("Missing a non-empty <title>", errors)


if __name__ == "__main__":
    unittest.main()
