---
name: present-as-html
description: Transform supplied text, notes, reports, articles, explanations, or structured content into a polished, visually expressive HTML page. Use when Codex needs to present source material as a standalone webpage, visual essay, scrollytelling page, interactive explainer, rich report, or microsite with typography, imagery, diagrams, charts, animations, or lightweight interactions while preserving the source's meaning.
---

# Present as HTML

Turn source material into a memorable web page whose visual structure clarifies the ideas. Treat the text as editorial content, not as copy to pour into generic cards.

## Workflow

1. Read all supplied content and identify:
   - the thesis or central purpose;
   - the intended reader and tone;
   - the narrative sequence;
   - facts, quotes, comparisons, processes, hierarchies, and calls to action;
   - claims that must not be embellished.
2. Choose one coherent visual concept before coding. Derive it from the subject matter, such as field notes, museum labels, a technical blueprint, a magazine feature, or an annotated atlas.
3. Sketch 3–7 purposeful sections. Give every section a distinct communication job and vary the composition across the page.
4. Decide which ideas benefit from a visual form:
   - comparison or repeated values → table, bars, or small multiples;
   - sequence or change → timeline or scroll progression;
   - flow or causality → diagram;
   - hierarchy → tree or nested composition;
   - mood or setting → image or illustration;
   - optional detail → disclosure, tabs, tooltip, or modal.
5. Build the page as a self-contained `index.html` unless the user requests a project or framework. Start from `assets/page-shell.html` when useful, but replace its placeholder visual language rather than merely recoloring it.
6. Inspect the result in a browser at desktop and mobile widths. Fix overflow, collisions, illegible contrast, motion problems, and weak hierarchy.
7. Run `python3 scripts/check_html.py <path-to-html>` and resolve relevant warnings.
8. Deliver the HTML file and briefly describe its visual concept and interactions.

## Preserve the source

- Keep every important fact, constraint, attribution, and qualification.
- Improve headings, ordering, and phrasing only when meaning remains intact.
- Never invent metrics, quotes, dates, sources, testimonials, or citations.
- Visually distinguish quoted material, inferred synthesis, and supporting context.
- If source content is sparse, create atmosphere and hierarchy instead of padding it with fabricated prose.

## Visual direction

Read `references/design-playbook.md` before designing a substantial page or when deciding among images, diagrams, motion, and interactions.

Apply these defaults:

- Make one visual idea dominant. Avoid a dashboard-like grid of interchangeable rounded cards unless the content is actually a dashboard.
- Use a deliberate type system with a display face and a readable body face. Prefer system fonts or gracefully degrading web fonts.
- Establish a restrained palette with named CSS custom properties and one strong accent.
- Use generous spacing and a clear rhythm. Let important elements break the grid intentionally.
- Prefer semantic HTML (`main`, `article`, `section`, `figure`, `nav`) and a logical heading hierarchy.
- Create responsive compositions with `clamp()`, grid/flex layouts, and focused breakpoints; do not shrink a desktop canvas to fit mobile.

## Images and diagrams

- Use images only when they add evidence, orientation, mood, or explanatory value.
- Prefer user-provided images. When image search or generation tools are available and imagery materially improves the page, use them and save output beside the HTML in a clearly named asset folder.
- Provide meaningful `alt` text for informative images and empty `alt` text for decorative ones.
- Use CSS, inline SVG, or Canvas for diagrams. Use HTML/CSS for simple structures and SVG for precise connections, paths, or labeled geometry.
- Keep diagrams legible without animation and on narrow screens. Do not encode essential meaning by color alone.
- Credit external imagery when licensing or attribution requires it. Do not embed hotlinked assets of uncertain provenance.

## Motion and interaction

- Use motion to reveal structure, show causality, establish progression, or provide feedback.
- Favor a few choreographed moments over constant ambient movement.
- Use `IntersectionObserver` for scroll reveals and CSS transitions for state changes.
- Keep controls keyboard accessible and use native elements (`button`, `details`, `dialog`) where possible.
- Ensure all content remains available when JavaScript fails.
- Respect `prefers-reduced-motion`; disable smooth scrolling, parallax, and nonessential transitions for those users.
- Avoid scroll hijacking, pointer-following gimmicks, autoplay audio, and effects that obscure reading.

## Implementation constraints

- Produce valid HTML with a viewport meta tag, a descriptive title, and no build step by default.
- Keep CSS and JavaScript inline for a single-file deliverable. Split assets only when images, fonts, or the user's requested project structure require it.
- Avoid adding libraries for effects that are simple in native CSS or JavaScript.
- If external dependencies are necessary, pin versions, minimize their number, and make the dependency obvious in the handoff.
- Render untrusted source text as text, not raw HTML. Never interpolate it into JavaScript.
- Add print styles when the content resembles a report, guide, brief, or reference document.

## Quality bar

Confirm before delivery:

- The page has a clear opening, narrative progression, and ending.
- The design feels specific to the subject rather than like a generic landing-page template.
- Visuals explain or reinforce the source instead of decorating empty space.
- Body text remains comfortable to read, with sensible line length and contrast.
- The page works at approximately 375 px and 1440 px widths.
- Keyboard focus is visible and interactive elements have clear affordances.
- Reduced-motion users receive a calm version.
- There are no broken local asset paths, console errors, accidental horizontal scrolling, or placeholder text.

