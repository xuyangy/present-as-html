# Design Playbook

Use this reference to turn a content outline into a visual system. It owns page archetypes, visual hierarchy, imagery, interaction principles, and the final critique. Select only the patterns the material needs. For section-level structure, use [Section Composition Grammar](composition-grammar.md); for motion intensity 5+, use [Motion Grammar for Editorial Pages](motion-grammar.md).

When the page has no established visual direction, select one through `design-directions.md` and read only the chosen recipe. Let the source provide the motif; let the recipe provide the visual grammar.

## Contents

1. Choose a page archetype
2. Position each section
3. Build visual hierarchy
4. Avoid generic output
5. Compose sections
6. Select imagery
7. Design diagrams
8. Use motion as grammar
9. Build scrollytelling beats
10. Add interaction deliberately
11. Responsive and print behavior
12. Run a design critique

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

## Position each section

Answer four questions before choosing its layout:

- **Narrative role:** opening, transition, explanation, evidence, comparison, pause, or synthesis?
- **Viewing context:** close reading on a phone, ordinary laptop reading, projected display, or print?
- **Section temperature:** quiet, energized, authoritative, warm, somber, playful, or tense?
- **Capacity:** does the material fit the proposed composition without overflow or empty filler?

Let these answers determine the visual register. Do not start with a favorite card layout and pour every section into it.

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

For longform, multilingual, or display-sensitive work, derive the type roles, scale, measure, language fallbacks, and font loading through [Typography System](typography-system.md). Let the recipe supply character and the source language supply reading constraints.

Use contrast through scale, weight, position, whitespace, and color—not through decoration alone. A strong page usually needs:

- one unmistakable focal point above the fold;
- one recurring visual motif;
- one or two surprising compositional shifts;
- quieter connective sections that make the dramatic moments meaningful.

## Avoid generic output

Reject these habits unless the content specifically calls for them:

- a hero headline followed by a uniform three-card grid;
- excessive rounded containers, glass panels, pills, and shadows;
- icons added to every heading;
- emoji substituted for a coherent icon or labeling system when the source does not call for emoji;
- a tiny uppercase eyebrow repeated above every section heading;
- section labels, running metadata, or kickers that merely translate or restate the adjacent heading;
- three or more consecutive left/right image-text zigzags;
- bento cells whose only purpose is filling the grid;
- fake coordinates, version labels, status dots, or other micro-metadata;
- decorative charts with invented data;
- fabricated testimonials, logos, metrics, or trust badges;
- repeated section layouts with only the text swapped;
- animation on every element;
- purple-on-dark palettes used without a subject-driven reason.

Instead, derive motifs from the content: rules and folios for an editorial essay, contour lines for geography, registration marks for an engineering story, or chapter tabs for an archival narrative.

## Compose sections

Start with the contracts in [Section Composition Grammar](composition-grammar.md). At a lighter level, a page should still contain a purposeful mixture of these narrative roles:

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

Treat atmospheric Canvas, ASCII, texture, and shader fields as background layers. Sparse openings or transitions can tolerate more visible atmosphere; dense prose and evidence sections need a quieter field. Keep the focal region behind text calm, preserve contrast without the effect, and use a source-derived character set or motif instead of random visual noise.

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
| Entry into a chapter | opening settle: a slower grouped entrance for title, deck, and one anchor visual |
| Ordinary semantic group | cascade: a short ordered entrance for a few sibling units, not every descendant |
| Quoted or poetic sequence | quote line: reveal meaningful lines at a readable cadence, then leave the full quotation visible |
| Two-sided comparison | directional pair: corresponding left/right or before/after states enter as one relationship |
| Connection or flow | draw or highlight a path |
| Accumulation | stagger related items as a group |
| Comparison | reveal corresponding sides or measures together |
| Change between states | preserve the baseline and interpolate only what changed |
| User-stepped process | step-through: explicit controls advance states while page scrolling remains normal |
| User feedback | immediate color, transform, or label response |
| Pause or sustained reading | no entrance motion, or one restrained section-level transition |

Keep most transitions between 150–500 ms. Longer sequences should be interruptible and must not delay access to content. Animate `transform` and `opacity` where possible. Never require animation to understand the page.

Assign one motion recipe to an animated section and group elements by meaning. Do not scatter independent delays across every descendant or reuse one fade-up recipe across the entire page.

Animate semantic leaves or coherent groups: a quotation line, comparison side, process stage, figure with its caption, or claim with its proof. Avoid animating both a container and all its descendants, which creates double motion and makes timing fragile. Do not require every section to animate; quiet prose is a valid recipe.

For step-through interactions, provide visible previous/next or state controls, a textual progress/state announcement, keyboard operation, and a complete final state. Do not consume wheel, arrow, or space input needed for ordinary page navigation, and do not trap the reader inside the component.

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

If the page uses continuous Canvas, WebGL, parallax, or substantial scroll choreography, add a visible static-effects control. Use a real button with a clear label, `aria-pressed`, and a stable hook such as `data-effects-toggle`. Static mode must cancel animation frames or observers, remove parallax, and leave a composed, complete frame; reduced-motion preferences should activate the same calm behavior automatically.

## Build scrollytelling beats

Treat scroll as a reading clock, not a remote control for spectacle.

- Give each beat one focused change, claim, or relationship.
- When revealing a list, introduce one item per beat; retain earlier items as subdued context instead of replaying the whole entrance.
- Let the text establish what changes and let the visual show how it changes.
- Keep a stable spatial anchor when several beats compare states of the same system.
- Avoid pinning when normal document flow communicates the sequence just as well.
- Ensure the final state contains the complete argument and can be understood without replaying the sequence.
- On narrow screens or with reduced motion, replace complex choreography with a stacked sequence or explicit state panels.

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

## Run a design critique

Resolve the P0–P2 findings in [Severity-Ranked Quality Checks](quality-checks.md), then evaluate the page through five lenses before delivery:

1. **Concept alignment:** Do typography, color, layout, imagery, and motion belong to the same visual idea? State where the form comes from in the source. Apply the substitution test: if unrelated content or another client name could replace the source without changing the design, strengthen the concept before polishing it.
2. **Hierarchy:** Does the eye find the intended entry point and reading path? Use a squint test.
3. **Craft:** Are spacing, alignment, radius, type, color, and responsive behavior systematic?
4. **Function:** Does every element help reading, understanding, navigation, or feedback? Apply the deletion test: if removing it changes nothing, remove it.
5. **Originality:** Is there at least one subject-specific, unexpected-but-right decision without falling into visual clichés?

Fix consequential failures before polish. Do not compensate for weak hierarchy by adding decoration.
