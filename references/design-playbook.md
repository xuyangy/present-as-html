# Design Playbook

Use this reference to turn a content outline into a visual system. Select only the patterns the material needs.

## Choose a page archetype

| Source shape | Useful archetype | Typical visual devices |
| --- | --- | --- |
| Essay, manifesto, or profile | Editorial feature | expressive opener, pull quotes, full-bleed imagery, margin notes |
| Process, history, or roadmap | Guided timeline | progress rail, milestones, changing scene, directional diagram |
| Technical explanation | Interactive explainer | annotated schematic, staged reveal, glossary, code or data samples |
| Findings or report | Visual report | key-number typography, restrained charts, evidence blocks, print styles |
| Place, ecosystem, or taxonomy | Atlas or field guide | map-like layout, labels, specimens, filters, layered legend |
| Contrasting options | Comparative story | split composition, synchronized rows, before/after control |

Do not force an archetype onto incompatible content. Combine at most two, with one clearly dominant.

## Build visual hierarchy

Define a small token system before styling:

```css
:root {
  --ink: #191816;
  --paper: #f2eee4;
  --accent: #c64b32;
  --muted: #716d64;
  --line: color-mix(in srgb, var(--ink) 18%, transparent);
  --measure: 68ch;
  --space: clamp(1rem, 2.5vw, 2.5rem);
}
```

Replace these example colors with a palette grounded in the subject. Use one scale for spacing and one type scale. Keep body copy around 45–75 characters per line. Let headings, media, and diagrams exceed that measure when useful.

Use contrast through scale, weight, position, whitespace, and color—not through decoration alone. A strong page usually needs:

- one unmistakable focal point above the fold;
- one recurring visual motif;
- one or two surprising compositional shifts;
- quieter connective sections that make the dramatic moments meaningful.

## Avoid generic output

Reject these habits unless the content specifically calls for them:

- a centered gradient headline followed by a uniform three-card grid;
- excessive rounded containers, glass panels, pills, and shadows;
- icons added to every heading;
- decorative charts with invented data;
- repeated section layouts with only the text swapped;
- animation on every element;
- purple-on-dark palettes used without a subject-driven reason.

Instead, derive motifs from the content: rules and folios for an editorial essay, contour lines for geography, registration marks for an engineering story, or chapter tabs for an archival narrative.

## Compose sections

Use a mixture of these patterns:

- **Statement:** large claim paired with a compact supporting passage.
- **Evidence:** data, quote, artifact, or image with a precise caption.
- **Sequence:** steps arranged spatially or progressively.
- **Pause:** a quiet transition with reduced density.
- **Detail:** optional explanation behind a disclosure or annotation.
- **Synthesis:** a final visual or concise conclusion that resolves the opening.

Alternate density. Avoid making every section full-screen or every section a card grid.

## Select imagery

Choose an image approach before collecting assets:

- **Documentary:** real people, objects, or locations; use when evidence and authenticity matter.
- **Editorial illustration:** metaphorical or atmospheric; use when a concept lacks literal imagery.
- **Texture and artifact:** scans, paper, handwriting, maps, or material detail; use to establish context.
- **Diagrammatic:** maps, systems, cutaways, and labeled forms; use when explanation is primary.

Crop intentionally with `object-fit` and `object-position`. Preserve faces, labels, and essential subjects. Supply width and height attributes when known to prevent layout shift.

## Design diagrams

Start by writing the relationship in one sentence. If the sentence is already clearer than a diagram, keep the sentence.

For a useful diagram:

1. Define nodes, groups, and direction.
2. Emphasize the primary path and mute secondary connections.
3. Put labels close to what they describe.
4. Include a legend only if direct labeling is impractical.
5. Provide a text equivalent in the surrounding copy or accessible description.
6. Test at mobile width; stack or simplify instead of miniaturizing.

For inline SVG, include `role="img"` and an accessible name. Use `vector-effect="non-scaling-stroke"` where scaling would make strokes inconsistent.

## Use motion as grammar

Map motion to meaning:

| Meaning | Motion pattern |
| --- | --- |
| Entry into a chapter | short fade and vertical settle |
| Connection or flow | draw or highlight a path |
| Accumulation | stagger related items as a group |
| Change between states | crossfade or interpolate the changed property |
| User feedback | immediate color, transform, or label response |

Keep most transitions between 150–500 ms. Longer sequences should be interruptible and must not delay access to content. Animate `transform` and `opacity` where possible. Never require animation to understand the page.

Use a single reduced-motion override:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    scroll-behavior: auto !important;
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Add interaction deliberately

Before adding an interaction, name the reader's question it answers. Good examples include:

- “What changes if I select this scenario?” → toggle or range input;
- “How do these layers combine?” → progressive layer control;
- “What does this term mean?” → inline definition or tooltip;
- “Can I inspect the details?” → disclosure or modal;
- “Where am I in the story?” → chapter navigation or progress marker.

Avoid hiding core prose behind interaction. Make touch targets at least 44 px where practical, preserve visible focus, and update state textually as well as visually.

## Responsive and print behavior

At narrow widths:

- collapse multi-column prose to one column;
- turn wide comparisons into stacked, labeled groups;
- simplify diagrams while preserving labels;
- reduce decoration before reducing font size;
- keep edge padding with `clamp()`;
- test long words, URLs, and headings for overflow.

For report-like pages, add print rules that remove controls, animations, sticky positioning, and decorative backgrounds while preserving charts, captions, and source URLs.

