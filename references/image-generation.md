# Raster Image Generation

Use this workflow only after the editorial plan establishes that generated raster imagery materially improves the page. Do not generate an image merely because a backend is available.

Define the destination through [Media Framing and Fidelity](media-framing.md) before writing a prompt. The page slot—not a backend's favorite dimensions—determines aspect ratio, safe area, crop, and responsive behavior.

## Resolve the backend

Use this order:

1. If the user requests a specific available backend, use it.
2. Otherwise, prefer the runtime-native image-generation skill or tool. Read and follow its current invocation, reference-image, editing, and output instructions.
3. Otherwise, use the single already-available external image backend, if one exists.
4. If several external backends are available and the choice materially affects cost, quality, privacy, or capabilities, ask the user once.
5. If no backend is available, choose the best honest fallback:
   - use supplied or properly sourced imagery;
   - use HTML, CSS, SVG, or Canvas when the need is diagrammatic;
   - reserve an accurately sized placeholder when a raster asset is still required;
   - ask the user only when generated raster imagery is essential to the requested result.

Never claim an image was generated, sourced, licensed, or verified when it was not. Do not install a backend, probe credentials, or invoke an undocumented CLI fallback merely because no native tool exists.

## Create a reproducible asset record

Use this structure inside the page project when generated images are needed:

```text
assets/
├── image-plan.md
├── prompts/
│   ├── 01-hero-night-garden.md
│   └── 02-editorial-pollinator.md
├── references/
│   └── 01-user-reference.png
└── images/
    ├── 01-hero-night-garden.webp
    └── 02-editorial-pollinator.webp
```

Use stable names in the form `NN-{role}-{slug}`. Do not overwrite an accepted image during iteration; create a new candidate suffix such as `-v2` until the replacement is approved.

In `image-plan.md`, record for each image:

- position and communication purpose;
- semantic slot ID and composition contract;
- prompt path and intended output path;
- aspect ratio or dimensions;
- fit policy, focal safe area, and mobile behavior;
- fidelity mode and whether the result must be labeled as illustration;
- reference assets and their roles (`direct`, `style`, `palette`, or `composition`);
- intended crop and responsive behavior;
- alt text, caption, and attribution requirements;
- selected backend and generation status.

## Save prompts before generation

Write each final prompt to its own file before invoking a backend. Include enough structure to reproduce the visual:

```markdown
---
id: 01
role: hero
slot_id: s01-opening-hero
output: ../images/01-hero-night-garden.webp
aspect_ratio: "16:9"
fit_policy: cover
focal_safe_area: central subject; right third remains quiet for adjacent HTML copy
mobile_behavior: use a separate 4:3 crop only if the subject remains intact
backend: auto
references:
  - path: ../references/01-user-reference.png
    usage: palette
---

PURPOSE: Establish a nocturnal habitat without presenting invented evidence.
SUBJECT: ...
COMPOSITION: Match the declared slot, focal safe area, and responsive crop...
VISUAL LANGUAGE: ...
COLOR AND LIGHT: ...
DO NOT INCLUDE: logos, labels, fabricated data, decorative UI
```

Include only references that exist. Treat color names and hex values as rendering guidance, not visible text. Keep important facts, labels, quotations, and interface copy in HTML or accessible SVG rather than inside the bitmap.

Choose a communication-purpose scaffold from [Image Prompt Patterns](image-prompt-patterns.md) when useful. Always adapt it to the selected recipe and slot rather than copying a generic visual style. The output is an embedded asset, not a precomposed page: explicitly forbid webpage or slide chrome, browser frames, mastheads, title bars, headlines, footers, page numbers, signatures, and decorative borders.

## Generate and verify

1. Settle the complete image plan and destination slots before the first generation call.
2. Save and verify every prompt file and direct reference needed for the next batch.
3. Generate independent images in batches when the selected tool supports it.
4. Record the actual backend and output path after each successful result.
5. Retry a failed item once from its saved prompt without regenerating successful items.
6. Inspect subject accuracy, composition, crop safety, style consistency, and unintended text or symbols.
7. Regenerate flawed content from a revised prompt; do not paint over bad text or identity details programmatically.
8. Optimize the accepted file for the page, preserve a suitable source copy, and connect its alt text, caption, and attribution.

When several generated images share a world, start from the selected page recipe's **Image prompt DNA** and define a short visual bible in `image-plan.md`: palette, material, lighting, texture, typography character, subject treatment, and forbidden drift. Regenerate divergent assets instead of disguising inconsistency with unrelated decoration.
