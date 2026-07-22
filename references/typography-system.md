# Typography System

Use this reference for longform pages, multilingual content, unusual display typography, or any page whose recipe and source do not already determine a complete type system. Choose font names last.

## Contents

1. Derive the system in order
2. Set roles and scale
3. Set measure and leading
4. Handle CJK and mixed scripts
5. Load fonts honestly
6. Audit the result

## Derive the system in order

1. **Content mode:** long reading, analytical density, visual essay, reference, or display-led narrative.
2. **Language composition:** Latin, CJK, Arabic, Devanagari, mixed scripts, numerals, code, or specialist symbols.
3. **Viewing context:** phone, ordinary reading, projected display, or print.
4. **Recipe character:** restrained or dramatic scale, serif or sans emphasis, metadata voice, and grid behavior.
5. **Available context:** brand fonts, supplied files, existing CSS, system fonts, or permissible web fonts.
6. **Font names:** choose faces that satisfy the preceding decisions and include truthful fallbacks.

Do not choose a fashionable display face first and force every source into its proportions.

## Set roles and scale

Use no more roles than the page can make meaningfully distinct:

- **Display:** the opening or rare peak; it may behave as a compositional shape.
- **Heading:** chapter and section hierarchy.
- **Body:** sustained reading; optimize this before display type.
- **Utility:** captions, notes, labels, navigation, and metadata.
- **Data/code:** optional monospaced or tabular role when alignment carries meaning.

Five visible size tiers are usually enough. Start with body size and select a modular ratio by content behavior:

| Ratio | Character | Useful for |
| --- | --- | --- |
| 1.20 | quiet, many close levels | references and dense reports |
| 1.25 | balanced | general explainers and articles |
| 1.333 | editorial contrast | longform features and visual reports |
| 1.50 | few dramatic levels | visual essays and statement-led pages |

Treat a hero display as layout, not merely the next heading tier. Size it with bounded viewport logic such as `clamp()` and test both width and height constraints. Do not shrink body copy to preserve an oversized title.

Use weight as part of the hierarchy. Large type may tolerate lighter strokes; small text usually needs regular or medium weight. Verify that every declared weight actually exists, and avoid synthetic bold or italic when it visibly distorts the script.

## Set measure and leading

Measure affects reading more than font novelty:

| Text | Starting measure | Starting line height |
| --- | --- | --- |
| Latin body | 45–75 characters; often `62ch–68ch` | 1.45–1.7 |
| CJK body | roughly 22–38 full-width characters | 1.65–2.0 |
| Caption or marginal note | shorter than body | 1.35–1.6 |
| One- or two-line display | determined by composition | 0.95–1.25 Latin; 1.05–1.35 CJK |

Increase leading as lines get longer. Narrow sidebars can use tighter leading; wide prose needs stronger line separation. Keep paragraphs comfortable on a phone rather than preserving desktop column density.

Use `text-wrap: balance` for short headings and `text-wrap: pretty` for prose where supported. Test URLs, long unbroken identifiers, and translated headings explicitly.

## Handle CJK and mixed scripts

For mixed Latin and CJK, put the Latin face before the CJK face so glyph fallback happens per character:

```css
:root {
  --font-body: "Source Sans 3", "Noto Sans SC", "PingFang SC",
    "Microsoft YaHei", sans-serif;
  --font-display: "Newsreader", "Noto Serif SC", "Songti SC", serif;
}

html {
  font-synthesis: none;
  line-break: strict;
  overflow-wrap: break-word;
}

table, .data {
  font-variant-numeric: tabular-nums slashed-zero;
}

.display-cjk {
  font-feature-settings: "halt" 1;
}
```

Choose fonts with compatible apparent size and x-height, or use `font-size-adjust` where supported. Do not rely on manual spaces between scripts to repair incompatible glyph metrics.

CJK-specific checks:

- Avoid synthetic italics; use real weight, color, emphasis marks, or a compatible quotation face.
- Keep ordinary CJK tracking near `0–0.05em`; do not apply wide Western display tracking to full-width glyphs.
- Use real CJK fallback names instead of ending the stack at generic `sans-serif` or `serif`.
- Give CJK body text more leading than comparable Latin text.
- Use language-appropriate quotation marks and preserve source punctuation.
- Use `text-spacing-trim` or `hanging-punctuation` only as progressive enhancement and inspect actual browser support; never depend on them to prevent broken CJK line starts or ends.
- Mark meaningful language changes with `lang`, such as `<span lang="en">HIGH WATER</span>`, so pronunciation, shaping, and hyphenation can follow the text.
- Consider `writing-mode: vertical-rl` only when vertical reading is meaningful and the fallback remains clear.

For other scripts, verify shaping, direction, numeral behavior, and fallback with actual source text. Set `lang` correctly, and use `dir="rtl"` or semantic directionality where required rather than visually reversing layout fragments.

## Load fonts honestly

- Prefer supplied or existing brand fonts when licensing and delivery permit them.
- For offline deliverables, use local assets or robust system stacks; do not silently depend on a remote font.
- Use `font-display: swap` for web fonts and reserve compatible fallback metrics to reduce layout shift.
- Wait for `document.fonts.ready` before measuring glyphs or positioning annotations from rendered text geometry.
- Subset large font files to the characters or ranges the page needs when practical, especially for CJK display faces.
- Do not embed an unlicensed commercial font merely to imitate a reference.
- If the intended font is unavailable, choose a fallback for structural similarity—width, contrast, x-height, and tone—not merely the same serif/sans category.

## Audit the result

- Body copy is the most comfortable text on the page.
- Hierarchy remains obvious in grayscale and with a squint test.
- The same role does not drift between unrelated sizes or weights.
- Small labels remain legible and do not become decoration through excessive uppercase or tracking.
- Numerals align when the content asks readers to compare them.
- Mixed scripts sit on a compatible baseline and no script falls into an accidental platform default.
- Headline line breaks remain intentional at narrow and wide widths.
- Print output retains hierarchy without requiring background color.
