# Present as HTML — User Manual

An agent skill that turns text you give it (notes, reports, articles, explanations) into a
polished, self-contained HTML page — a visual essay, explainer, or content-led microsite —
rather than a plain document dump.

This manual is for people using the skill. For the instructions the agent itself follows, see
[`SKILL.md`](SKILL.md).

---

## 1. What it's for

Use it when you want source material presented as a **standalone webpage** with real visual
structure: typography, imagery, diagrams, charts, light animation, or small interactions — while
keeping the source's meaning intact.

**Good fits:** reports, research writeups, technical explainers, profiles/essays, guides,
field notes, changelogs, comparison briefs, process/system explanations, scrollytelling pieces.

**Not for:** dashboards, operational product UIs, or general-purpose web apps. If you need an
app with real state and backend logic, this is the wrong skill.

## 2. How to invoke it

- In a conversation, ask directly, e.g. *"Present this report as an HTML page"* or *"Turn these
  notes into a visual explainer"* — the agent recognizes the intent from `SKILL.md`'s
  description and loads it automatically.
- Or invoke it by name if your environment supports explicit skill invocation
  (`$present-as-html`, per [`agents/openai.yaml`](agents/openai.yaml)).
- Supply the source content directly in the message, or point to files/notes to convert.
- Optionally tell it your visual direction ("make it feel like a museum field guide," "keep it
  spare and Swiss," "match our brand colors"). If you don't, it picks a content-appropriate style
  itself.

## 3. What happens when it runs

The agent works through a fixed pipeline (full detail in `SKILL.md`):

1. **Reads the source** — extracts thesis, audience, tone, narrative order, key facts/quotes/
   comparisons, and anything that must not be embellished.
2. **Plans** — a compact "Design Read" (page type, audience, tone, layout, motion level, etc.),
   then picks one coherent visual concept (e.g. field notes, a technical blueprint, a magazine
   feature) rather than a generic template.
3. **Maps sections** — each section gets one clear communication job.
4. **Chooses visual forms** for the content — tables/bars for comparisons, timelines for
   sequence, diagrams for process/flow, maps for places, image or illustration for mood, etc.
5. **Decides on imagery** — none, your assets, honest placeholders, sourced real assets, or
   generated assets, depending on what the content needs.
6. **Builds** a self-contained `index.html` (inline CSS/JS by default, no build step) unless you
   ask for a project/framework structure.
7. **Reviews it in a browser** — checks desktop and mobile widths, reduced-motion behavior,
   console errors, broken assets, overflow — using the bundled scripts when available.
8. **Runs an automated quality check** and fixes flagged issues.
9. **Delivers the HTML file** with a short description of the visual concept and interactions.

For long or visually ambitious pages, it typically builds the opening plus one representative
section first, checks that it looks right, then continues — it won't stop and wait for your
approval unless a decision would materially change the outcome.

## 4. What you get back

- A single `index.html` file (or a small project folder if images/fonts require it), including:
  - Inline CSS and JS by default — no build step, opens directly in a browser.
  - Semantic HTML, responsive layout (works ~375px–1440px wide), visible keyboard focus.
  - `prefers-reduced-motion` support — a calmer version for users who need it.
  - Print styles if the content resembles a report/guide/brief.
- If images were generated or sourced, they're saved alongside the HTML in a named asset folder.
- A short handoff note describing the visual concept, any fidelity tradeoffs (e.g. if content was
  condensed rather than presented verbatim), and any known limitations (e.g. no browser available
  to visually QA).

## 5. Content fidelity — what it will and won't do

- Keeps every important fact, number, quote, attribution, and qualification from your source.
- Will improve headings/ordering/phrasing, but not in ways that change meaning.
- **Never invents** metrics, quotes, dates, sources, or testimonials.
- Visually distinguishes quotes, inferred synthesis, and supporting context from each other.
- By default it preserves your text faithfully rather than summarizing — if it does condense or
  restructure content, it flags that explicitly in the handoff.

## 6. Design system (how it picks a look)

The skill ships eight named visual "recipes" it can start from — each is a starting system with
its own tokens and grammar, not a rigid template:

| Recipe | Best for |
|---|---|
| Evidence-led editorial | research, reports, investigations, technical essays |
| Press editorial | profiles, interviews, criticism, narrative essays |
| Swiss structured | briefings, comparisons, policy summaries, mixed text/data |
| Technical schematic | systems, mechanisms, workflows, engineering explanations |
| Warm humanist | education, care, community, wellness, approachable guidance |
| Archival field guide | history, place, ecology, taxonomy, collections |
| Kinetic editorial | visual essays, manifestos, launches, scrollytelling |
| Raw document | technical notes, dossiers, incident narratives, changelogs |

If you give no direction, the agent chooses one of these based on your content. It keeps one
recipe dominant and will only ever blend in one additional expressive technique, and only when
the source earns it.

## 7. Images and diagrams

- Images are used only when they add evidence, orientation, or mood — not decoration.
- Real brands/products get real logos/screenshots, never faked marks.
- Supplied screenshots/charts/documents are preserved or reframed, not stylistically regenerated.
- Diagrams are built natively in HTML/CSS or SVG (not baked into images), so labels stay legible,
  accessible, and readable on narrow screens.
- Generated imagery (when used) is saved next to the HTML with its prompt recorded.

## 8. Motion and interaction

- Motion is used to reveal structure or causality, not for ambient decoration.
- Each animated section gets one deliberate motion treatment tied to what it's showing.
- Everything degrades gracefully: content is available with JavaScript off, keyboard-accessible,
  and calm for `prefers-reduced-motion` users.
- No scroll-hijacking, autoplay audio, or forced-progression tricks.

## 9. Quality checks (what's verified before delivery)

Two bundled scripts back the review step — you can also run them yourself against any HTML file
this skill produced:

```bash
# Visual/browser QA: screenshots at mobile/tablet/desktop widths, reduced-motion pass,
# console errors, failed requests, broken images, overflow. Requires Python + Playwright/Chromium.
python3 scripts/review_html.py path/to/index.html
python3 scripts/review_html.py path/to/index.html --modes all   # adds print-media check

# Static checks: broken local links/asset paths, heading structure, duplicate IDs,
# leftover placeholder text, unlabeled controls, etc.
python3 scripts/check_html.py path/to/index.html
```

Findings are triaged P0 (must fix) through P3, per
[`references/quality-checks.md`](references/quality-checks.md). The agent resolves P0s and
relevant P1/P2s before calling the page done.

## 10. Tips for better results

- **Give the raw content, not a summary of it** — the more complete your source, the more the
  agent can preserve faithfully instead of guessing.
- **State your audience and tone** if it matters ("this is for executives," "keep it playful") —
  it shapes the whole visual concept.
- **Mention any brand constraints up front** (colors, existing site, logo files) — real brand
  assets are used as supplied, not reinvented.
- **Flag data that must not be touched** (exact figures, legal language, quotes) so it's clearly
  marked as verbatim in the output.
- **If you want a specific look**, name it (e.g. "Swiss structured," "feels like a field guide")
  — otherwise the agent chooses for you based on content.
- **Large or many-section content** may take a couple of passes; the agent builds a
  representative slice first, so early output isn't necessarily the whole page.

## 11. Reference library (for advanced/manual use)

These live under `references/` and are normally consulted by the agent automatically — you don't
need to read them, but they're useful if you want to understand or influence a specific decision:

- `editorial-planning.md` — how the initial content plan/brief is built.
- `design-playbook.md` — page archetypes, hierarchy, imagery and interaction principles.
- `design-directions.md` — how a visual style gets picked when you give no direction.
- `design-context.md` — how existing brand/product/publication context is incorporated.
- `composition-grammar.md` — section-level structural patterns.
- `expressive-techniques.md` — optional stylistic extensions layered onto a recipe.
- `palette-families.md` — coordinated color-token bundles.
- `typography-system.md` — type scale/role decisions for longform or multilingual pages.
- `media-framing.md`, `asset-sourcing.md`, `image-generation.md`, `image-prompt-patterns.md` —
  how images/diagrams are framed, sourced, or generated.
- `motion-grammar.md` — animation/scrollytelling patterns for higher-motion pages.
- `quality-checks.md` — the full P0–P3 severity checklist.
- `recipe-*.md` — the eight visual recipes described in §6.

## 12. Known constraints

- No build step or external framework by default — everything ships as inline CSS/JS in one
  HTML file unless you ask otherwise.
- External dependencies are avoided; if truly needed, they're version-pinned and disclosed.
- Untrusted source text is always rendered as text, never as raw HTML — this skill won't
  interpolate your content into markup or scripts.
- Current factual claims about real people/organizations/products beyond what you supplied are
  verified and sourced before being added, not assumed.
- If a browser isn't available in the environment to run the visual QA step, the agent will say
  so rather than silently skipping it.
