# Content-Safe Expressive Techniques

Use this reference when a page needs more expressive range than the selected recipe supplies. These are extensions, not standalone themes. Choose at most one dominant extension and derive its motif from the source.

## Contents

1. Select by content signal
2. Keep the recipe coherent
3. Respect medium feasibility

## Select by content signal

| Technique | Source signal | Signature moves | Fails when |
| --- | --- | --- | --- |
| Scale tension | a sharp thesis, conflict, or editorial urgency | monumental headline against compact evidence, hard rules, deliberate type collision | body copy becomes tiny or every section shouts |
| Hard-edge color blocking | categories, camps, states, or a deliberately confrontational tone | flat high-chroma fields, dark outlines, offset layers, abrupt but systematic boundaries | color is arbitrary or mimics a generic neo-brutalist feed |
| Collage and overprint | archives, fragmented memory, cultural montage, conflicting sources | rotated artifacts, cropped layers, registration marks, controlled overlap | evidence is obscured or “mess” replaces hierarchy |
| Responsive geometric art | geometry, modular systems, architecture, playful computation | CSS/SVG forms reorganize meaningfully across breakpoints | shapes are generic decoration or imitate real objects poorly |
| Typographic monument | a manifesto, name, phrase, or number legitimately carries the page | full-width type, extreme scale contrast, text as spatial anchor | the phrase cannot survive mobile or supporting copy is sacrificed |
| Chromatic text accent | one pivotal word or phrase carries a real semantic turn | a restrained two-hue fill on one display phrase with a solid fallback | it becomes ambient decoration, reduces contrast, or spreads across paragraphs |
| Retro-futurist atlas | astronomy, exploration, speculative history, old/new technology | restrained orbital lines, cream/ink fields, catalog labels, measured diagrams | decorative space clichés imply scientific accuracy |
| Waveform or signal narrative | audio, rhythm, volatility, alternating states, or a measured story arc | one continuous line, direct annotations, a meaningful turning point | a random squiggle stands in for absent data |
| Pixel or system-native narrative | games, computing history, state machines, low-resolution culture | discrete steps, pixel grid, limited palette, breakpoint “levels” | nostalgia overwhelms readability or fake game UI appears |
| Bauhaus construction | education, modular identity, elemental relationships | circles, triangles, squares, primary structure, grid alignment | geometry substitutes for a missing concept |
| Terminal or document core | source code, logs, research notes, protocols, technical culture | monospace utility voice, visible rules, source fragments, explicit state | fake commands, version numbers, or terminal chrome are invented |
| Gallery framing | artworks, photography, products, or specimens whose viewing is primary | deep or quiet field, large authentic media, precise captions and metadata | low-quality media is enlarged or metadata is decorative |
| White-space object study | material culture, craft, luxury, a single object, contemplative instruction | sparse field, fine typography, one carefully placed object or mark | emptiness is filled with arbitrary micro-labels |

Match expressive temperature to the reading goal:

- **Quiet:** gallery framing, white-space object study, restrained document core.
- **Neutral:** Bauhaus construction, responsive geometry, waveform, terminal/document core.
- **Bold:** scale tension, hard-edge blocking, collage, typographic monument, pixel narrative.

Do not choose three quiet cream-paper variants and call them different directions. When comparing directions, vary at least two explicit axes such as temperature, structure, type behavior, media role, or motion.

## Keep the recipe coherent

- The recipe continues to control body typography, spacing, accessibility, and surface roles.
- The extension gets one declared responsibility: opening, evidence field, diagram language, or a single peak section.
- Palette comes from content or brand through [Palette Families](palette-families.md), not from a style label.
- Use authentic assets through [Asset Sourcing and Selection](asset-sourcing.md); do not fabricate product imagery, documentary evidence, or interfaces to satisfy a look.
- Record the extension and its content source in the Design Read. If unrelated content could use it unchanged, revise or remove it.

For a chromatic text accent, define one named gradient token and keep a solid accent-color fallback. Use two visibly distinct, palette-related hues rather than a monochrome tint. Apply the gradient only inside a feature query with `background-clip: text`; restore a solid color in print because printed backgrounds may be omitted. If the page supports multiple color schemes, derive and test a legible token for each. Do not use this extension when the recipe requires flat fills or evidence graphics would become less precise.

## Respect medium feasibility

Before proposing a direction, identify its irreplaceable ingredient. HTML/CSS/SVG are strong at typography, rules, geometry, grids, diagrams, responsive transformations, and stateful interaction. They do not replace photography, illustration, product rendering, organic ink, cinematic light, or complex 3D merely by adding gradients and filters.

If the technique's soul depends on unavailable imagery, hand-drawn material, real audio, particles, or 3D:

1. obtain or generate the correct asset honestly;
2. redesign around an HTML-native ingredient; or
3. reject the direction rather than delivering a visibly degraded imitation.

State any deliberate degradation before implementation. A simpler direction executed completely is better than a high-concept reference reduced to generic CSS effects.
