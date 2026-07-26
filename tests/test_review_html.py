from __future__ import annotations

import argparse
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from review_html import (  # noqa: E402
    GROUP_GAP,
    SHEET_PADDING,
    contact_sheet_group_width,
    contact_sheet_layout,
    parse_viewports,
    resolve_color_schemes,
    resolve_javascript,
    resolve_modes,
)


class ReviewHtmlTests(unittest.TestCase):
    @staticmethod
    def result(width: int, height: int) -> dict[str, object]:
        return {"viewport": {"width": width, "height": height}}

    def test_capture_dimensions_expand_independently(self) -> None:
        self.assertEqual(resolve_modes("all"), ("normal", "reduced", "print"))
        self.assertEqual(resolve_javascript("both"), ("enabled", "disabled"))
        self.assertEqual(resolve_color_schemes("both"), ("light", "dark"))

    def test_single_capture_values_are_preserved(self) -> None:
        self.assertEqual(resolve_modes("normal"), ("normal",))
        self.assertEqual(resolve_javascript("disabled"), ("disabled",))
        self.assertEqual(resolve_color_schemes("system"), ("system",))

    def test_viewport_parser_rejects_unhelpful_sizes(self) -> None:
        with self.assertRaises(argparse.ArgumentTypeError):
            parse_viewports("200x200")

    def test_contact_sheet_wraps_large_matrix_into_scenario_grid(self) -> None:
        groups = {
            f"scenario-{index}": [
                self.result(375, 812),
                self.result(1440, 1000),
            ]
            for index in range(12)
        }
        columns, canvas_width = contact_sheet_layout(groups)
        self.assertEqual(columns, 2)
        self.assertLessEqual(canvas_width, 1800)
        widest_group = max(contact_sheet_group_width(items) for items in groups.values())
        needed_width = (
            columns * widest_group
            + (columns - 1) * GROUP_GAP
            + 2 * SHEET_PADDING
        )
        self.assertGreaterEqual(canvas_width, needed_width)

    def test_contact_sheet_uses_two_columns_for_default_viewports(self) -> None:
        groups = {
            f"scenario-{index}": [
                self.result(375, 812),
                self.result(768, 1024),
                self.result(1440, 1000),
            ]
            for index in range(12)
        }
        columns, canvas_width = contact_sheet_layout(groups)
        self.assertEqual(columns, 2)
        widest_group = max(contact_sheet_group_width(items) for items in groups.values())
        needed_width = (
            columns * widest_group
            + (columns - 1) * GROUP_GAP
            + 2 * SHEET_PADDING
        )
        self.assertGreaterEqual(canvas_width, needed_width)
        self.assertEqual(canvas_width, 1668)


if __name__ == "__main__":
    unittest.main()
