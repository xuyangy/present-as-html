# Raw Document

Use for technical notes, source-heavy dossiers, countercultural essays, incident narratives, changelogs, and material whose directness benefits from visible structure. Avoid when polished reassurance, luxury, or gentle guidance is central.

## Tokens

```css
:root {
  --paper: #fffdf7;
  --ink: #090909;
  --muted: #565656;
  --accent: #0758d9;
  --accent-on: #ffffff;
  --marker: #eee34b;
  --line: #090909;
  --wash: #efede5;
  --font-display: ui-monospace, "SFMono-Regular", Consolas, monospace;
  --font-body: ui-sans-serif, system-ui, sans-serif;
  --font-data: ui-monospace, "SFMono-Regular", Consolas, monospace;
  --measure: 72ch;
  --radius: 0;
}
```

## Typography and layout

- Expose the document's real hierarchy through labels, rules, indentation, and source ordering.
- Use regular or wide measure and let excerpts, diffs, logs, or annotations keep their native visual character.
- Prefer hard edges, visible links, underlines, and explicit state over ornamental interface chrome.
- Make roughness intentional through alignment and consistency; accidental sloppiness is not a style.

## Signature moves

- Present one primary artifact—quote, log, memo, code excerpt, or decision record—nearly unvarnished.
- Use marker yellow for a single important annotation and blue for links or cross-references.
- Reveal editorial intervention through brackets, marginal notes, or clearly labeled synthesis rather than pretending it is source text.

## Media and diagrams

Favor screenshots, source fragments, simple relationship diagrams, and honest placeholders. Use generated imagery rarely; this recipe derives credibility from actual material. Preserve line wrapping and provide accessible alternatives for dense excerpts.

## Motion, responsive, and print

Keep motion around 0–3: disclosure, focus, and navigation feedback. On mobile, allow code and source artifacts to scroll within labeled regions while prose remains fluid. Print should retain links, annotations, and source labels without relying on color.

## Avoid

- fake terminal output, logs, annotations, or version numbers;
- using browser-default styling accidentally rather than deliberately;
- dense monospace body text for long reading;
- brutalist contrast that harms accessibility;
- adding stickers, cursors, or marker effects to every section.

## Image prompt DNA

Prefer real source material. If illustration is necessary, use: direct documentary still or flat editorial artifact on off-white ground, hard crop, black structure, one blue link-like accent and sparse yellow marker, no fake UI, no fabricated text, no decorative nostalgia.
