# Content-Led Design Directions

Use this advisor when the user has not provided a brand system, visual reference, or clear aesthetic direction. Select a system that helps the content communicate; do not make the content perform a style demo.

## Contents

1. Run the direction advisor
2. Choose from the recipe catalog
3. Use the compatibility matrix
4. Apply or remix a recipe
5. Keep the vocabulary separate

## Run the direction advisor

Skip the advisor when the user supplies a brand, design system, reference page, or explicit visual language. Honor that context instead.

For a genuinely open brief:

1. Read the Design Read and section map.
2. Identify the dominant communication need: evidence, narrative, explanation, warmth, place, spectacle, or raw immediacy.
3. Consider three directions from meaningfully different families. Do not offer three flavors of minimalism.
4. For each direction, state:
   - why it fits this source and audience;
   - three visible consequences in typography, layout, media, or motion;
   - its expressive temperature and HTML-native feasibility;
   - one tradeoff or situation where it would fail.
5. Recommend one direction.
6. If two choices would materially change brand meaning, cost, or comprehension, ask one focused question. Otherwise select the recommendation, state it in the Design Read, and proceed.

Do not interrogate the user with a generic taste questionnaire. Do not use empty labels such as “modern,” “clean,” “premium,” or “engaging” without describing visible design behavior.

## Choose from the recipe catalog

| Direction | Best for | Defining character | Recipe |
| --- | --- | --- | --- |
| Evidence-led editorial | research, reports, investigations, rigorous essays | quiet authority, marginal evidence, high legibility | [recipe](recipe-evidence-led.md) |
| Press editorial | profiles, criticism, interviews, cultural narratives | headline energy, column rhythm, print tension | [recipe](recipe-press-editorial.md) |
| Swiss structured | briefings, comparisons, institutional explanations | rational grid, disciplined hierarchy, signal color | [recipe](recipe-swiss-structured.md) |
| Technical schematic | systems, processes, engineering, mechanisms | measured geometry, labeled flows, instrument-like detail | [recipe](recipe-technical-schematic.md) |
| Warm humanist | education, care, community, reflective guidance | tactile warmth, generous pace, approachable expertise | [recipe](recipe-warm-humanist.md) |
| Archival field guide | history, place, taxonomy, ecology, collections | catalog labels, material texture, specimen logic | [recipe](recipe-archival-field-guide.md) |
| Kinetic editorial | launches, manifestos, visual essays, transformation stories | large type, spatial narrative, content-driven motion | [recipe](recipe-kinetic-editorial.md) |
| Raw document | technical notes, counterculture, source-heavy dossiers | directness, visible structure, deliberate roughness | [recipe](recipe-raw-document.md) |

These are descriptive systems, not instructions to reproduce a specific living designer, publication, or brand. Use references as historical context; implement original work grounded in the supplied content.

## Use the compatibility matrix

Use `++` as a strong starting match, `+` as compatible, and `—` as a choice needing a specific rationale.

| Page type | Evidence | Press | Swiss | Technical | Warm | Archival | Kinetic | Raw |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Longform | ++ | ++ | + | + | + | ++ | + | + |
| Report | ++ | + | ++ | ++ | — | + | — | + |
| Tutorial | + | + | + | ++ | ++ | + | + | + |
| Explainer | ++ | + | ++ | ++ | + | + | + | + |
| Review | ++ | ++ | ++ | + | — | + | + | ++ |
| Briefing | ++ | + | ++ | + | + | — | — | + |
| Visual essay | + | ++ | + | + | ++ | ++ | ++ | + |
| Interactive explainer | + | + | + | ++ | + | + | ++ | + |

Treat the matrix as routing guidance, not a prohibition. Let the subject, audience, supplied assets, and calibrated dials override it when they provide a clear reason.

If a recipe is correct but too restrained for the source, keep the recipe as the reading system and add one bounded technique from [Content-Safe Expressive Techniques](expressive-techniques.md). Do not replace content-led selection with a large style menu.

## Apply or remix a recipe

After choosing:

1. Read the single recipe file.
2. Copy its tokens into the page as a starting system.
3. Replace generic motifs with one derived from the source.
4. Adjust density and motion according to the Design Read without breaking the recipe's hierarchy.
5. Reuse the recipe's image-prompt DNA when generating supporting imagery so page and assets share one visual world.
6. Record meaningful deviations in the Design Read.

Keep one recipe dominant. If combining two, assign responsibilities explicitly, for example:

```text
Base grammar: Evidence-led editorial for typography, measure, and citations.
Secondary influence: Technical schematic for diagrams only.
```

Do not mix one recipe's palette, another's type, a third's radii, and a fourth's motion merely to create variety. That produces incoherence rather than originality.

## Keep the vocabulary separate

- **Page type:** structural editorial form, such as report, tutorial, or visual essay.
- **Page archetype:** narrative composition, such as atlas, timeline, or comparative story.
- **Recipe:** page-wide visual grammar: tokens, typography, layout, media, and motion.
- **Visual device:** local explanatory form, such as a chart, diagram, quote, or toggle.
- **Image style:** raster rendering treatment used for a generated or sourced asset.

Example:

```text
Page type: interactive explainer
Archetype: guided timeline
Recipe: technical schematic
Visual device: causal-flow diagram
Image style: none; use accessible inline SVG
```
