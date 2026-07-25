# Severity-Ranked Quality Checks

Use this reference during the representative-slice review and before delivery. Fix higher-severity problems before visual polish.

## P0 — release blockers

Do not deliver while any P0 issue remains:

- meaningful source claims, numbers, quotations, qualifications, or attribution are missing or materially altered;
- invented evidence, identity, citations, interface states, or metrics appear factual;
- a newly added current claim about a real product, person, organization, event, specification, or policy lacks a recorded authoritative source;
- required local assets, fragment links, or primary document structure are broken;
- a visible image fails to load or decode, or a control has no accessible name;
- essential content depends on animation, JavaScript, hover, color alone, or an unavailable external service;
- a control cannot be reached or operated by keyboard;
- content is clipped, overlaps, or creates unrecoverable horizontal overflow at a target width;
- an informative image lacks a text alternative, or generated imagery could be mistaken for documentary evidence;
- untrusted source content is interpolated as executable HTML or JavaScript.

## P1 — comprehension and accessibility failures

Resolve P1 issues unless the user knowingly accepts a documented limitation:

- the opening does not establish purpose or the reading path is unclear;
- body measure, type size, contrast, heading order, or focus visibility impairs reading;
- terminology, capitalization, or bilingual naming drifts across sections in a way that changes meaning or forces the reader to relearn the same concept;
- a diagram, table, comparison, or interaction loses its labels or relationships on mobile;
- motion distracts, delays reading, lacks reduced-motion behavior, or cannot settle into a complete state;
- geometry-dependent motion begins before fonts and layout measurements are stable, leaving stale or displaced annotations;
- print output drops evidence, captions, source URLs, or essential context in a report-like page;
- remote dependencies lack an honest offline or failure behavior appropriate to the request;
- a screenshot crop removes interface text or state required by the accompanying claim.
- a recognition-critical brand or product asset is approximated despite an official or supplied asset being required;
- a geographic or route visual implies accuracy without real locations/geometry, source status, direct labels, and a readable static fallback;
- a metric or ranking omits its unit, definition, time context, supplied/source status, or comparable baseline.

## P2 — system and craft problems

Fix P2 issues when they visibly weaken the result:

- typography, palette, radius, imagery, or motion drifts away from the selected recipe without a declared reason;
- palette tokens are assembled from incompatible bundles, or a signal color is used as ambient decoration rather than meaning;
- the stated form source is only a generic style label, or unrelated content could replace the source without changing the design;
- three or more consecutive sections repeat the same composition and density without communicative benefit;
- alignment spines, spacing scales, caption positions, or grouped media treatments are inconsistent;
- a composition contract is used without the content it requires, such as a comparison without shared dimensions;
- grouped evidence media uses inconsistent ratios, scale, framing, or caption logic that prevents comparison;
- a sourced hero or evidence asset was accepted without checking authority, relevance, resolution, crop safety, consistency, and attribution status;
- a generated embedded asset includes page chrome, fake interface state, or important text that belongs in HTML/SVG;
- animation uses one generic reveal everywhere instead of reflecting section relationships;
- a proposed visual direction depends on unavailable photography, illustration, 3D, particles, or organic material and is replaced with visibly degraded generic CSS effects;
- decorative metadata, cards, icons, or effects add no reading value;
- a section label, kicker, folio, or running header merely duplicates the adjacent heading;
- a high-energy or inverse section is visually loud without carrying consequential content.

## P3 — optional polish

Address after P0–P2:

- refine optical alignment, line breaks, crop position, easing, and small-screen spacing;
- remove minor repetition and strengthen captions or transitions;
- optimize accepted images and reduce nonessential dependency weight;
- add subtle print, selection, hover, or loading refinements that do not affect comprehension.

## Inspect in this order

1. Compare the output against the source-preservation list.
2. Run `python3 scripts/check_html.py <path-to-html>` and resolve every P0 plus relevant P1/P2 findings.
3. Inspect at approximately 375 px, 768 px, and 1440 px; include unusually long headings and URLs. When Python Playwright and Chromium are available, run `python3 scripts/review_html.py <path-to-html>`, read `contact-sheet.png` first, then open individual captures for craft detail and check `review-report.json`. Treat any `hiddenContent` entry as a P0 until proven deliberate: it means a substantial block stayed invisible after the page settled.
4. Navigate by keyboard and verify visible focus, reading order, control labels, and state announcements.
5. Test reduced motion. For effects-heavy pages, also test the manual static mode and JavaScript-disabled content state.
6. Inspect print preview for reports, guides, briefs, and reference pages.
7. Check the console, local asset paths, remote failures, and accidental horizontal scrolling.
8. Run the five-lens design critique in the Design Playbook only after structural failures are resolved.

## Diagnose before patching

| Symptom | Likely cause | Prefer this fix |
| --- | --- | --- |
| Section feels crowded | wrong contract or too much source assigned | split or select a higher-capacity composition before shrinking type |
| Page feels monotonous | cadence repeats composition and energy | change the relationship or insert a justified quiet/focus beat |
| Page feels incoherent | recipe tokens or motifs drift | restore the dominant recipe and remove unassigned secondary influences |
| Visual feels decorative | device has no reader question | replace it with evidence, explanation, or whitespace |
| Mobile diagram is tiny | desktop geometry was merely scaled | stack, simplify, or provide an explicit state sequence |
| Screenshot looks polished but untrustworthy | source was reconstructed unnecessarily | restore or programmatically reframe the original |
| Motion looks busy | elements animate individually without semantic grouping | animate the relationship as one recipe or remove motion |
| Spacing fixes keep multiplying | composition or content capacity is wrong | revisit the contract instead of accumulating local margins |
