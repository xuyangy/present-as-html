# Media Framing and Fidelity

Use this reference when the page includes supplied images, screenshots, scans, diagrams, or generated raster assets. Decide where the media must work before cropping, reframing, sourcing, or generating it.

When media must be found outside the supplied project, use [Asset Sourcing and Selection](asset-sourcing.md) before accepting a source file.

## Contents

1. Define the slot first
2. Choose a fidelity mode
3. Process supplied screenshots
4. Set crop and fit behavior
5. Coordinate with generated imagery
6. Verify every slot

## Define the slot first

Record a contract for every consequential media slot:

```yaml
slot-id: s03-mechanism-specimen
purpose: show the interface state discussed in the adjacent paragraph
necessity: essential
source-type: user-supplied screenshot
fidelity: preserve
desktop-placement: right side of annotated specimen
mobile-placement: full-width before numbered notes
ratio: 16:10
minimum-size: 1600x1000
fit-policy: framed
focal-safe-area: entire interface must remain visible
caption: required
alt-text: describe the visible state and relevant control
sensitive-content: none identified
```

Use stable semantic IDs rather than page numbers alone so assets survive section reordering. The slot controls asset treatment; do not generate or crop an image and then force the page to accommodate its accidental shape.

Classify necessity before treatment: **essential** media carries evidence or explanation, **supporting** media materially improves context or atmosphere, and **ornamental** media changes neither meaning nor useful context and should normally be omitted.

## Choose a fidelity mode

- **Preserve:** keep every pixel and all meaningful text visible. Use for evidence, UI, code, charts, documents, and identity-critical material.
- **Crop:** remove nonessential edges while protecting the declared focal safe area. Use for documentary or atmospheric images.
- **Reframe:** place the unchanged source inside a deliberate target-ratio canvas with recipe-consistent background, padding, alignment, and optional truthful caption.
- **Reconstruct:** redesign or regenerate the media because the user wants a conceptual rendering or the source cannot serve the intended explanation. Disclose the change and never present the result as the original.

Default supplied screenshots, charts, documents, and interfaces to **preserve** or **reframe**. Do not send them through image generation merely to make them stylistically consistent.

## Process supplied screenshots

1. Inspect the actual pixel dimensions, legibility, sensitive information, and required details.
2. Match the screenshot to a composition contract and destination slot.
3. Preserve it directly when its ratio and resolution fit.
4. Otherwise reframe it programmatically: create the target-ratio canvas, scale proportionally, use intentional padding, and align according to the adjacent text or callouts.
5. Split a very long screenshot into a small sequence of same-sized truthful excerpts only when the surrounding prose identifies what each excerpt shows.
6. Use reconstruction only when the user authorizes redesign or the artifact is explicitly illustrative rather than evidentiary.

Never fabricate browser chrome, product states, notifications, numbers, or UI labels. Never crop away the very control, label, or outcome discussed by the text.

### Record screenshot-framing semantics

When a screenshot needs reframing, record these choices instead of applying a universal mockup treatment:

| Parameter | Typical values | Decide from |
| --- | --- | --- |
| `ratio` | slot ratio or exact dimensions | destination composition, not source dimensions |
| `background` | plain, paper, wash, grid, blurred-source | recipe and evidence status |
| `padding` | compact, standard, spacious | screenshot density and legibility |
| `inset` | none, subtle, balanced | separation needed from the background |
| `shadow` | none, soft, editorial | recipe; Swiss and raw-document modes usually use none |
| `corners` | square, small, medium | recipe, never generic app-card fashion |
| `alignment` | center, top-left, top-right, bottom-left, bottom-right | adjacent copy, callouts, and the screenshot's focal region |
| `background-intensity` | quiet, low, medium | screenshot always remains the focal evidence |

The background is a support field, not a second illustration. Keep the screenshot's destination area quiet, avoid text, logos, devices, people, frames, or directional focal subjects, and make the field safe for all declared responsive crops. When the screenshot aligns toward a corner, keep that corner especially calm.

Useful treatment families:

- **Editorial:** paper or low-contrast blurred-source field, standard padding, small corners, optional restrained editorial shadow.
- **Swiss/technical:** plain, grid, or wash field, square corners, no shadow, hairline separation, low-area signal color only.
- **Evidence/raw:** plain or transparent field, generous contain behavior, no cosmetic chrome that could be mistaken for part of the artifact.

For very tall pages, code, dashboards, or narrow mobile screens, first try spacious framing and a side alignment. If meaningful content becomes too small, split the source into two or three same-sized truthful excerpts before considering reconstruction.

## Set crop and fit behavior

- Use `cover` for photography and illustration only when the focal safe area survives all intended widths.
- Use `contain` for interfaces, diagrams, charts, documents, and any image containing essential text.
- Use **framed** for preserved media that needs a consistent ratio without cropping; let the surrounding canvas absorb the mismatch.
- Set `object-position` from the identified subject, not from a universal top-center rule.
- Reserve intrinsic width and height or an `aspect-ratio` to prevent layout shift.
- When overlaying HTML text, record a safe area and test the crop at both narrow and wide widths.

For grouped media, use consistent ratio, scale logic, edge treatment, caption position, and visual density. Consistency is not permission to crop away evidence; use framed placement when source shapes differ materially.

## Coordinate with generated imagery

Pass the slot contract into [Image Generation](image-generation.md): purpose, output ratio or dimensions, focal safe area, intended crop, responsive behavior, and forbidden embedded chrome. Keep headings, captions, interface labels, facts, and citations in HTML whenever possible.

Generated imagery must not impersonate documentary evidence. Label an illustration when context could otherwise make its status ambiguous.

When writing generation prompts, use the purpose patterns in [Image Prompt Patterns](image-prompt-patterns.md). Generated assets are embedded media, not precomposed pages: forbid headers, footers, titles, page numbers, browser frames, signatures, decorative borders, and other page chrome.

## Verify every slot

- The media answers the reader question named in the section brief.
- Its necessity class still holds after the deletion test.
- The chosen fidelity mode is visible and honest.
- Essential subjects, text, and labels survive desktop and mobile.
- Captions, alt text, attribution, and generation status agree with the actual asset.
- No sensitive or identity-critical detail was altered unintentionally.
- Missing assets remain explicit placeholders with the correct contract rather than counterfeit content.
