# Editorial Planning

Use this reference before designing a substantial page. Keep the planning compact; write a separate brief file only when the source is long, the page has many assets, or later revisions need a durable record.

## Contents

1. Choose the content mode
2. Write the Design Read
3. Map sections and cadence
4. Select composition, layout, and navigation
5. Plan assets
6. Declare the implementation system
7. Establish a representative slice

## Choose the content mode

Treat content mode as a structural and fidelity decision, not an aesthetic one.

| Mode | Preserve | Suitable output |
| --- | --- | --- |
| Faithful | All meaningful claims, evidence, qualifications, and sequence | longform, archival article, complete report |
| Edited | All main arguments and supporting evidence; remove repetition and improve order | tutorial, report, explainer, review |
| Condensed | Conclusions, essential evidence, and actions; omit secondary detail intentionally | briefing, executive summary, visual essay |
| Reconstructed | Core concepts remain authoritative, but teaching copy and structure are newly composed | interactive explainer, learning page |

Default to **Faithful** when the user says “convert,” “present,” or “make this into HTML” without requesting summarization. Never imply full preservation when using another mode.

Do not use percentages as a substitute for editorial judgment. Record instead:

- must preserve: exact claims, numbers, quotations, steps, tables, caveats, and attribution;
- may compress: repetition, navigation boilerplate, or tangents;
- may restructure: headings, order, summaries, and transitions;
- must not invent: proof, examples presented as real, citations, or conclusions.

## Write the Design Read

Capture the decisions that should visibly affect the page:

```yaml
Design Read:
  page-type: longform | report | tutorial | explainer | review | briefing | visual-essay | interactive-explainer
  audience: who is reading and what they need to understand or do
  reading-goal: the single outcome the page should produce
  content-mode: faithful | edited | condensed | reconstructed
  design-context: supplied | extracted | none
  visual-language: a specific family, not “modern” or “clean”
  form-source: the content-specific object, relationship, or metaphor shaping the page
  signature-investment: the one detail or section that deserves exceptional craft
  expressive-temperature: quiet | neutral | bold
  layout-width: narrow | regular | wide | full
  visual-variance: 1-10
  information-density: 1-10
  motion-intensity: 1-10
  asset-dependence: 1-10
  constraints: accessibility, offline use, brand, viewport, supplied assets
```

If the user or an existing brand already supplies a visual direction, record it directly. For brand-sensitive work, read [Design Context and Provenance](design-context.md) before selecting tokens or identity assets. Otherwise read `design-directions.md`, choose a content-led recipe, and replace the vague `visual-language` value with the selected recipe plus a subject-specific motif.

The `form-source` must answer “Where does this visual behavior come from in the supplied content?” If only a style label answers the question, the concept is still generic. Concentrate extra craft in `signature-investment`; do not distribute equal animation and ornament across every section.

Use the dials as decisions, not decorative scores:

- **Expressive temperature:** quiet prioritizes contemplation and evidence; neutral balances system and character; bold accepts stronger scale, color, or spatial tension. Temperature is independent of information density and section energy.
- **Visual variance 1–3:** stable grid and low surprise; **4–6:** varied rhythm with one or two asymmetric moves; **7–10:** art-directed or experimental, provided comprehension survives.
- **Information density 1–3:** one dominant idea with generous pauses; **4–6:** balanced editorial density; **7–8:** analytical or comparison-heavy; **9–10:** only for reference-like material with strong grouping and navigation.
- **Motion intensity 1–2:** feedback only; **3–4:** restrained transitions; **5–7:** sequenced or scroll-driven explanation; **8–10:** cinematic behavior that needs especially strong fallbacks.
- **Asset dependence 1–3:** typography and code-native visuals can carry the page; **4–6:** a few images materially help; **7–10:** inventory real assets before fixing the composition.

Resolve conflicts deliberately:

- High variance + high density → preserve a stable grid and navigation spine; experiment in one layer.
- High motion + high density → animate focus or transitions, not every element.
- High asset dependence + named brand → source official assets before layout; generated imagery must not replace identity-critical material.
- Accessibility constraints override every dial.

## Map sections and cadence

Create a compact map for each section:

```text
Section: 02 — Why the system fails
Source anchors: paragraphs 6–10, table 1
Narrative role: evidence
Reader question: “What actually causes the failure?”
Must preserve: three causes, quoted threshold, caveat
Composition contract: system map
Energy: build
Contrast role: base
Visual form: annotated causal diagram
Interaction: none
Fallback: ordered list with the same relationships
Asset slot: none
```

For each visual or interaction, be able to finish this sentence: “This helps the reader understand ___.” If the answer is merely “it makes the page interesting,” redesign or remove it.

Plan the content relationship before the animation. Record “sequence,” “accumulation,” “comparison,” or “causal flow”; choose fades, path drawing, pinning, or state transitions only during implementation.

Before coding, list all sections in order with an **energy** beat (`quiet`, `build`, `focus`, `peak`, or `release`) and a separate **contrast role** (`base`, `inverse`, or `accent`). Avoid three consecutive sections with the same composition and density. Let consequential content earn peaks and inverse surfaces instead of inserting them on a fixed interval.

## Select composition, layout, and navigation

Read [Section Composition Grammar](composition-grammar.md) for substantial pages or whenever several sections risk becoming interchangeable. Choose by content shape and capacity, then let the selected recipe determine the visual treatment. Treat contracts as communication structures, not paste-ready templates.

Keep layout width independent from visual style:

| Width | Use for |
| --- | --- |
| Narrow | focused essays, short briefings, quotation-led prose |
| Regular | most articles and explainers |
| Wide | tables, code, diagrams, reports, comparisons |
| Full | image-led essays and spatial explanations |

Add a table of contents or chapter navigation when it improves orientation. Omit it when the navigation would compete with a short page. Collapse multi-column navigation cleanly on narrow screens.

## Plan assets

Choose one or combine deliberately:

- **None:** typography, tables, CSS, Canvas, and SVG are sufficient.
- **User-provided:** preserve the files and their intended role.
- **Sourced:** use authoritative or properly licensed material and retain attribution.
- **Generated:** use for atmosphere, editorial illustration, or non-identity-critical concepts.
- **Placeholder:** reserve the correct aspect and describe the missing asset honestly.

Classify every proposed medium before collecting it:

- **Essential:** removing it loses evidence, orientation, comparison, or explanation.
- **Supporting:** prose remains complete, but the medium materially improves understanding or atmosphere.
- **Ornamental:** removing it changes neither meaning nor useful context; omit by default.

For each consequential image, screenshot, scan, or diagram, define a slot in [Media Framing and Fidelity](media-framing.md): semantic ID, necessity class, purpose, desktop and mobile placement, target ratio, fit policy, focal safe area, fidelity mode, caption, and alt text. For each generated image, also record its prompt and forbidden drift. Do not add one image per section by rote.

For references, distinguish:

- **direct:** use the actual supplied asset;
- **style:** borrow visual treatment only;
- **palette:** extract color relationships only;
- **composition:** borrow spatial organization without copying content.

When external media is required, read [Asset Sourcing and Selection](asset-sourcing.md) before accepting candidates. Collect and compare before the layout becomes dependent on a mediocre first result.

## Declare the implementation system

Before styling the representative slice, write a compact declaration that implementation can be checked against:

```yaml
Design System Declaration:
  source: brand context | recipe | subject-derived hybrid
  palette-logic: token roles and where consequential colors came from
  typography: display, heading, body, utility, data roles and real weights
  grid-and-measure: alignment spine, columns, prose measure, spacing scale
  surfaces: paper, wash, inverse, accent, border, radius, shadow behavior
  media-treatment: crop, framing, caption, attribution, and evidence status
  motion-grammar: semantic recipes, easing family, calm fallback
  expressive-extension: optional single technique and its content source
  prohibited-moves: brand prohibitions and chosen anti-patterns
```

This is not a second design brief. It translates the Design Read into observable rules and should be short enough to audit against the CSS and markup.

## Establish a representative slice

For a long or high-variance page, implement the opening and one representative section before completing the rest. Use it to test:

- whether the visual language fits the source;
- whether type size and line length support reading;
- whether density matches the chosen mode;
- whether custom visuals feel native to the page;
- whether mobile and reduced-motion fallbacks are viable.

Treat the slice as an internal style anchor. Request user confirmation only when the direction is genuinely ambiguous, brand-sensitive, costly to reverse, or the user asked for iterative checkpoints. When the choice cannot be evaluated from prose, render the smallest comparable fork—usually the opening plus one representative section in two or three directions—rather than asking the user to choose between abstract adjectives. Keep content and viewport constant, label the axes that changed, and vary at least two meaningful dimensions instead of recoloring one composition.
