# Technical Schematic

Use for systems, mechanisms, workflows, engineering explanations, and interactive technical learning. Avoid when a human narrative or emotional atmosphere should remain primary.

## Tokens

```css
:root {
  --paper: #0f1820;
  --surface: #16242d;
  --ink: #edf3f4;
  --muted: #a8bac1;
  --accent: #62d4f5;
  --accent-on: #0f1820;
  --signal: #ffb45c;
  --line: #36515d;
  --grid: rgba(98, 212, 245, 0.08);
  --font-display: ui-sans-serif, system-ui, sans-serif;
  --font-body: ui-sans-serif, system-ui, sans-serif;
  --font-data: ui-monospace, "SFMono-Regular", Consolas, monospace;
  --measure: 70ch;
  --radius: 0.25rem;
}
```

## Typography and layout

- Use wide layouts for diagrams and regular measure for explanations.
- Distinguish prose from instrument labels: readable sans for paragraphs, monospace for identifiers and measurements.
- Organize complex systems into zones with explicit boundaries, direction, and legends only when direct labels are insufficient.
- Keep a stable diagram frame across state changes so readers compare rather than reorient.

## Signature moves

- Reveal or emphasize the primary path through a system while secondary paths remain visible but quiet.
- Pair every schematic with a plain-language explanation or ordered text equivalent.
- Use the amber signal only for warnings, exceptions, or points requiring action.

## Media and diagrams

Prefer accessible inline SVG, Canvas for genuinely dynamic simulation, and HTML/CSS for simple states. Use raster imagery only for physical subjects or atmosphere. Keep labels horizontal and large enough to read on mobile.

## Motion, responsive, and print

Use motion around 3–6 for causal flow, state changes, or progressive layers. Avoid decorative terminal typing. On mobile, stack zones or expose explicit state panels rather than miniaturizing. Provide a light print treatment with dark ink, visible boundaries, and no dependency on glow.

## Avoid

- generic cyber-neon, code rain, or glowing circuitry;
- presenting invented values as measurements;
- unlabeled connectors or color-only meaning;
- turning every paragraph into a terminal window;
- shrinking a desktop architecture diagram until its labels are illegible.

## Image prompt DNA

Use: precise technical cutaway or schematic atmosphere, dark blue-black field, cyan structural lines, sparse amber warning points, controlled grid, orthographic or isometric clarity, no fake data, no embedded labels, no futuristic HUD clutter.
