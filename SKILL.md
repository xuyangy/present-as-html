---
name: present-as-html
description: Transform supplied text, notes, reports, articles, explanations, or structured content into a polished, visually expressive HTML page. Use when Codex needs to present source material as a standalone webpage, visual essay, scrollytelling page, interactive explainer, rich report, or content-led microsite with typography, imagery, diagrams, charts, animations, or lightweight interactions while preserving the source's meaning. Do not use for dashboards, operational product interfaces, or general-purpose web applications.
---

# Present as HTML

Turn source material into a memorable web page whose visual structure clarifies the ideas. Treat the text as editorial content, not as copy to pour into generic cards.

## Choose a depth

Pick a depth before step 1 and record it in the Design Read. Depth governs how much of this skill you load, how ambitious the page is, and how hard you verify. It never governs fidelity to the source.

| Depth | Load | Plan | Verify |
| --- | --- | --- | --- |
| `sketch` | this file plus one recipe | a three-line Design Read: page type, form source, recipe | `check_html.py`, then one look at 375 px and 1440 px |
| `standard` | plus [Editorial Planning](references/editorial-planning.md) and [Content-Led Design Directions](references/design-directions.md) | full Design Read plus a section cadence | `check_html.py`, then `review_html.py --modes normal` and read its contact sheet; resolve P0 and P1 |
| `full` | plus [Design Playbook](references/design-playbook.md), [Section Composition Grammar](references/composition-grammar.md), and the specialist references the content earns | plus a Design System Declaration and a representative slice | `review_html.py --modes all`, read the contact sheet, then open individual captures for craft; keyboard pass, JavaScript-disabled pass, print preview, and a source-fidelity check |

Default to `standard`. Choose `full` when the source is long or dense, the page needs print output, several sections risk becoming interchangeable, or brand identity is at stake. Drop to `sketch` when the user asks for something quick, rough, or provisional, or when one screen carries the whole source. An explicit request from the user overrides these rules.

Two costs dominate and neither is reading: generating the page itself, and every tool round-trip taken after it exists, because the page stays in context for all of them. So batch inspection rather than iterating one observation at a time, prefer the contact sheet to reading captures individually, and run `--modes normal` while iterating and `--modes all` once at the end.

Depth never licenses invented facts, dropped source material, unreachable controls, or an undisclosed change in fidelity. A `sketch` page is smaller and less verified; it is not less honest. Name the depth in the handoff so the user can ask for more.

## Workflow

1. Read all supplied content and identify:
   - the thesis or central purpose;
   - the intended reader and tone;
   - the narrative sequence;
   - facts, quotes, comparisons, processes, hierarchies, and calls to action;
   - claims that must not be embellished.
2. Create a compact Design Read before coding: page type, audience, reading goal, content mode, design context, visual language, form source, signature investment, expressive temperature, layout width, visual variance, information density, motion intensity, asset dependence, asset mode, and constraints. At `standard` and `full`, read [Editorial Planning](references/editorial-planning.md) for the modes and template; at `sketch`, record only page type, form source, recipe, and asset mode. When an existing brand, product, publication, design system, or current external fact materially shapes the page, read [Design Context and Provenance](references/design-context.md) at any depth.
3. At `full`, read the [Design Playbook](references/design-playbook.md). At every depth, choose one coherent visual concept derived from the subject matter, such as field notes, museum labels, a technical blueprint, a magazine feature, or an annotated atlas. Keep structure, density, layout, expressive temperature, and aesthetics as separate decisions. If the user supplies no visual direction, read [Content-Led Design Directions](references/design-directions.md), select a content-appropriate recipe, and load only that recipe file. When the recipe needs more range, select at most one source-earned extension from [Content-Safe Expressive Techniques](references/expressive-techniques.md).
4. Map purposeful sections. Give every section a distinct communication job, identify the source material it must preserve, and plan its energy and contrast role. At `full`, choose content-shaped contracts from [Section Composition Grammar](references/composition-grammar.md) before coding.
5. Decide which ideas benefit from a visual form:
   - comparison or repeated values → table, bars, or small multiples;
   - verified metrics, ranks, or specifications → metric stage, ledger, ranked measure, or specification sheet;
   - sequence or change → timeline or scroll progression;
   - flow, causality, recurrence, or convergence → process, system, loop, or convergence diagram;
   - places or routes → a sourced geographic map with a static text/visual fallback;
   - several comparable artifacts → an evidence matrix with consistent framing and captions;
   - hierarchy → tree or nested composition;
   - mood or setting → image or illustration;
   - optional detail → disclosure, tabs, tooltip, or modal.
6. Choose an asset mode and record it in the Design Read: `none` (typography and code-native visuals only), `user-provided`, `placeholder`, `sourced`, or `generated`. Default to `none` — most content-led pages are carried by type, tables, CSS, and SVG, so external raster imagery is opt-in rather than expected. Three things select another mode: the user supplies assets, the user asks for imagery, or the content cannot be understood without a real image, screenshot, scan, map, or artifact.

   Treat an explicit user request for imagery — "generate images", "add illustrations", "include photos", "make it image-led" — as having already established the need. Select `generated` or `sourced` accordingly and proceed; do not re-litigate whether imagery is warranted or answer such a request with CSS shapes and SVG instead. The honesty rules still bind: no fabricated evidence, identity, screenshots, or metrics, and generated imagery stays labeled as illustration.

   For consequential images, screenshots, scans, or diagrams, define their destination and fidelity through [Media Framing and Fidelity](references/media-framing.md) before transforming or generating them. When real external assets are required, use [Asset Sourcing and Selection](references/asset-sourcing.md) to compare, verify, and record candidates. Do not treat code-native diagrams and external images as substitutes for each other.
7. At `full`, build the opening plus one representative section first and inspect it as the style anchor. Continue without a user checkpoint unless a choice would materially change the requested result.
8. Build the page as a self-contained `index.html` unless the user requests a project or framework. Start from [the page shell](assets/page-shell.html) when useful, but replace its placeholder visual language rather than merely recoloring it.
9. Inspect the result in a browser at desktop and mobile widths. When Python Playwright and Chromium are available, run `python3 scripts/review_html.py <path-to-html>` with the bundled [browser reviewer](scripts/review_html.py). It reports console errors, failed requests, broken images, unnamed controls, horizontal overflow, and hidden content — substantial blocks left invisible because a reveal never fired or script did not run. It scrolls the page before capturing so `IntersectionObserver` reveals settle; pass `--no-scroll` only to inspect the pre-reveal state deliberately.

   Read `contact-sheet.png` first: it tiles every mode and viewport into one image, so a single look replaces one per capture. Open individual full-page captures afterwards for craft detail. Iterate with `--modes normal`, and run `--modes all` once at the end to add print media. Never trust the report alone. Without Playwright, use the runtime-native browser and disclose any remaining visual-QA limitation.
10. Run `python3 scripts/check_html.py <path-to-html>` and use [Severity-Ranked Quality Checks](references/quality-checks.md). Resolve every P0 plus relevant P1 and P2 findings.
11. Deliver the HTML file, name the depth you worked at, name the asset mode, and briefly describe its visual concept and interactions. Naming the asset mode is not optional: when it was `none`, say the page uses no external images so the user can ask for imagery instead of discovering its absence.

## Preserve the source

- Keep every important fact, constraint, attribution, and qualification.
- Improve headings, ordering, and phrasing only when meaning remains intact.
- Never invent metrics, quotes, dates, sources, testimonials, or citations.
- Visually distinguish quoted material, inferred synthesis, and supporting context.
- If source content is sparse, create atmosphere and hierarchy instead of padding it with fabricated prose.
- Default to faithful preservation when the user asks to convert or present text without requesting summarization. If using an edited, condensed, or reconstructed mode, make the change in fidelity intentional and disclose it in the handoff.

## Visual direction

Treat a recipe as a concrete starting system, not a template to copy. Adapt its tokens and grammar to the source while preserving its internal logic. Keep one recipe dominant; combine two only when each has a declared responsibility.

Recipe references: [Evidence-led editorial](references/recipe-evidence-led.md), [press editorial](references/recipe-press-editorial.md), [Swiss structured](references/recipe-swiss-structured.md), [technical schematic](references/recipe-technical-schematic.md), [warm humanist](references/recipe-warm-humanist.md), [archival field guide](references/recipe-archival-field-guide.md), [kinetic editorial](references/recipe-kinetic-editorial.md), and [raw document](references/recipe-raw-document.md).

Apply these defaults:

- Make one visual idea dominant. Avoid a dashboard-like grid of interchangeable rounded cards unless the content is actually a dashboard.
- Use a deliberate type system with a display face and a readable body face. Prefer system fonts or gracefully degrading web fonts.
- For multilingual, longform, or display-sensitive pages, derive roles, scale, measure, language fallbacks, and loading through [Typography System](references/typography-system.md).
- Establish a restrained palette with named CSS custom properties and one primary accent; add a secondary signal only when it carries a distinct semantic role.
- For a small number of consequential words or phrases — in display headings or within body copy — use gradient text as a deliberate emphasis device: the gradient must travel between two clearly distinct hues (for example, blue to teal, or terracotta to violet), not a monochrome tint of one color; derive the second stop from the accent with relative color syntax (`oklch(from var(--accent) … calc(h - 80))`) so it survives palette swaps and color-scheme changes. Define it as a named token, apply it with `background-clip: text`/`-webkit-text-fill-color: transparent`, keep a solid accent-color fallback for unsupported browsers, and reset to a solid color in print styles (printed backgrounds are omitted by default, which would leave the text invisible). Reserve it for semantic emphasis (for example, a thesis keyword or pivotal phrase), never for whole paragraphs or ambient decoration; follow the chosen recipe when it explicitly requires flat fills or forbids gradients.
- Support both light and dark color schemes: declare `color-scheme: light dark`, define the palette once as tokens, and override only the tokens under `@media (prefers-color-scheme: dark)` — in dark mode, lighten the accent enough to hold contrast on the dark ground, and re-derive the gradient token with boosted lightness and chroma at both ends (roughly `l + 0.06`/`c + 0.04` at the accent end and `l + 0.16`/`c + 0.11` at the rotated end) so gradient text glows against the dark ground instead of muting. Keep print output light regardless of scheme.
- When the recipe palette needs a content-appropriate variant, choose one coherent token bundle from [Palette Families](references/palette-families.md); do not mix individual swatches across bundles.
- Use generous spacing and a clear rhythm. Let important elements break the grid intentionally.
- Prefer semantic HTML (`main`, `article`, `section`, `figure`, `nav`) and a logical heading hierarchy.
- Create responsive compositions with `clamp()`, grid/flex layouts, and focused breakpoints; do not shrink a desktop canvas to fit mobile.
- Use `text-wrap: pretty` where supported and container queries when a component's own width should determine its layout.
- Use placeholders rather than counterfeit logos, products, screenshots, metrics, or testimonials.

## Images and diagrams

- The default asset mode is `none`: build the page from typography, layout, CSS, and inline SVG, and expect a page with no external images unless something selects otherwise. Disclose that mode in the handoff.
- When the user asks for imagery, that request is the justification. Switch the asset mode, plan real slots, and produce the images; the guidance below shapes *how*, not *whether*.
- Otherwise use images only when they add evidence, orientation, mood, or explanatory value.
- Classify proposed media as essential, supporting, or ornamental; omit ornamental media by default. Requested imagery is at least supporting — do not reclassify it as ornamental to justify dropping it.
- Prefer user-provided and authoritative assets. For a named brand or product, use real logos, product imagery, or interface screenshots; never replace identity-critical material with CSS silhouettes or fabricated marks.
- Default supplied screenshots, charts, documents, and interfaces to preservation or programmatic reframing; do not regenerate them merely for stylistic consistency.
- When image search or generation tools are available and imagery materially improves the page, use them and save output beside the HTML in a clearly named asset folder. Use sourced imagery for evidence and generated imagery for non-identity-critical atmosphere or illustration.
- Before generating raster assets, read [Image Generation](references/image-generation.md) and follow its backend-resolution, prompt-record, batching, and fallback contract.
- For generated documentary, explanatory, process, comparison, system, UI-scenario, or data-poster imagery, select a purpose scaffold from [Image Prompt Patterns](references/image-prompt-patterns.md) and adapt it to the page recipe.
- Keep important labels, facts, and interface text as HTML or accessible SVG text rather than baking them into generated images.
- Provide meaningful `alt` text for informative images and empty `alt` text for decorative ones.
- Use CSS, inline SVG, or Canvas for diagrams. Use HTML/CSS for simple structures and SVG for precise connections, paths, or labeled geometry.
- Keep diagrams legible without animation and on narrow screens. Do not encode essential meaning by color alone.
- Credit external imagery when licensing or attribution requires it. Do not embed hotlinked assets of uncertain provenance.

## Motion and interaction

- Use motion to reveal structure, show causality, establish progression, or provide feedback.
- Favor a few choreographed moments over constant ambient movement.
- Give each animated section one semantic motion recipe based on its relationship—opening settle, cascade, quote line, directional pair, accumulation, path, state change, or explicit step-through. Do not apply the same generic reveal to every section.
- For motion intensity 5+, scrollytelling, shared-element transitions, or geometry-dependent choreography, read [Motion Grammar for Editorial Pages](references/motion-grammar.md) before implementation.
- Plan the relationship or narrative beat first; choose the exact animation during implementation. Do not let a preselected effect dictate the content.
- In scrollytelling, give each beat one focused change. Reveal enumerated points progressively while retaining earlier context in a quieter state.
- Use `IntersectionObserver` for scroll reveals and CSS transitions for state changes.
- Keep controls keyboard accessible and use native elements (`button`, `details`, `dialog`) where possible.
- Ensure all content remains available when JavaScript fails.
- Respect `prefers-reduced-motion`; disable smooth scrolling, parallax, and nonessential transitions for those users.
- When Canvas, WebGL, or substantial scroll choreography is used, also provide an obvious manual static-effects control and a complete static fallback.
- Avoid scroll hijacking, pointer-following gimmicks, autoplay audio, and effects that obscure reading.
- A step-through component must use explicit controls and state text; never consume ordinary page scroll or keyboard navigation to force progression.

## Implementation constraints

- Produce valid HTML with a viewport meta tag, a descriptive title, and no build step by default.
- Keep CSS and JavaScript inline for a single-file deliverable. Copy required assets locally and split them out only when images, fonts, or the user's requested project structure require it.
- Avoid adding libraries for effects that are simple in native CSS or JavaScript.
- If external dependencies are necessary, pin versions, minimize their number, and make the dependency obvious in the handoff.
- Render untrusted source text as text, not raw HTML. Never interpolate it into JavaScript.
- Preserve supplied claims as supplied. Verify and record authoritative sources before adding current factual assertions about real products, people, organizations, events, specifications, or policies.
- Add print styles when the content resembles a report, guide, brief, or reference document.

## Quality bar

Use the P0–P3 severity model in [Severity-Ranked Quality Checks](references/quality-checks.md), then confirm before delivery:

- The page has a clear opening, narrative progression, and ending.
- Its content mode is evident and all must-preserve material is present.
- The design feels specific to the subject rather than like a generic landing-page template.
- The form source can be traced to the supplied content; unrelated content could not replace it without changing the concept.
- Visuals explain or reinforce the source instead of decorating empty space.
- Every interactive or custom visual block still belongs to a content-led page rather than turning it into a dashboard or generic application.
- Body text remains comfortable to read, with sensible line length and contrast.
- The page works at approximately 375 px and 1440 px widths.
- Keyboard focus is visible and interactive elements have clear affordances.
- Reduced-motion users receive a calm version.
- Missing assets are exposed honestly; identity, evidence, and credibility are not fabricated.
- There are no broken local asset paths, console errors, accidental horizontal scrolling, or placeholder text.
