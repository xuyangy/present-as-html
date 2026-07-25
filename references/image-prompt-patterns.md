# Image Prompt Patterns

Use this reference only after [Media Framing and Fidelity](media-framing.md) defines the destination slot and [Raster Image Generation](image-generation.md) resolves the workflow. These are purpose patterns, not mandatory aesthetics; combine them with the selected recipe's Image prompt DNA.

## Contents

1. Write asset-first prompts
2. Select by communication purpose
3. Reusable prompt patterns
4. Keep truth and typography outside the bitmap

## Write asset-first prompts

Every prompt should declare:

- communication purpose and subject;
- target ratio or dimensions and focal safe area;
- crop behavior and where adjacent HTML copy needs quiet space;
- shared visual bible when the image belongs to a set;
- visual language, palette, material, lighting, and density;
- forbidden drift and evidence status.

End with an asset-only constraint adapted to the job:

```text
Create only the embedded visual asset. Do not add a webpage, slide, browser frame, masthead, title bar, headline, footer, page number, logo, signature, decorative border, or surrounding presentation chrome. Keep the central subject and declared safe area intact at the target crop.
```

For a group, add:

```text
This belongs to a matched set. Keep the same ratio, subject scale, margins, line weight, label density, palette, texture, and camera or projection logic as the other assets.
```

## Select by communication purpose

| Reader need | Pattern | Prefer code-native instead when |
| --- | --- | --- |
| Feel a real setting or human situation | Documentary editorial image | the source requires a specific real event, person, or place and no authentic image is available |
| Understand an abstract concept | Editorial explanatory illustration | exact nodes, labels, or state must remain editable and accessible |
| Follow ordered stages | Process illustration | arrows, labels, or branching logic carry the meaning |
| Compare two worlds or conditions | Comparative visual | exact shared dimensions or values must align |
| See a system as a whole | System-relations illustration | the connections are factual and must be directly inspectable |
| Present a redesigned interface concept | UI scenario illustration | the original screenshot is evidence or its text/state must remain exact |
| Create a visual field around verified data | Data-poster backdrop | the number, unit, source, or chart must be accurate; keep those in HTML/SVG |

## Reusable prompt patterns

Replace bracketed fields and append the slot, recipe, and asset-only constraints.

### Documentary editorial image

```text
PURPOSE: Ground the passage in a plausible human or physical setting without claiming documentary proof.
SUBJECT: [scene, people, action, place].
COMPOSITION: [ratio], [subject placement], quiet [side/region] for adjacent HTML copy, natural depth and unforced gesture.
VISUAL LANGUAGE: restrained editorial documentary photography, natural light, believable materials, moderate density, no commercial staging.
STATUS: illustrative unless it depicts a supplied and verified reference accurately.
DO NOT INCLUDE: invented brands, logos, watermarks, sci-fi interfaces, conspicuous AI tropes, embedded text.
```

### Editorial explanatory illustration

```text
PURPOSE: Make [concept] intuitively visible before the reader encounters the exact HTML explanation.
SUBJECT: [metaphor, components, spatial relationship].
COMPOSITION: [ratio], clear primary relationship, ample negative space, central 70% crop-safe.
VISUAL LANGUAGE: [recipe materials], restrained annotation marks without legible prose, medium information density.
DO NOT INCLUDE: fake measurements, pseudo-technical labels, decorative arrows that imply unsupported causality.
```

### Process illustration

```text
PURPOSE: Show the physical or conceptual transition from [start] through [stages] to [result].
COMPOSITION: [ratio], one unambiguous direction, distinct stages, stable baseline, room for HTML step labels.
VISUAL LANGUAGE: [recipe], consistent scale and line logic, secondary detail muted.
DO NOT INCLUDE: generated headings, long labels, extra stages, closed loops unless recurrence is part of the source.
```

### Comparative visual

```text
PURPOSE: Contrast [A] and [B] along the shared idea of [dimension].
COMPOSITION: [ratio], balanced paired fields, matched viewpoint and subject scale, a visible neutral baseline, quiet space for HTML labels.
VISUAL LANGUAGE: [recipe], identical rendering logic on both sides; difference comes from the source, not arbitrary styling.
DO NOT INCLUDE: unequal framing that implies magnitude, before/after claims absent from the source, embedded verdict text.
```

### System-relations illustration

```text
PURPOSE: Establish the character of [system] and the relationship among [parts].
COMPOSITION: [ratio], clear primary path, coherent groups, subdued secondary connections, direct-label safe zones.
VISUAL LANGUAGE: [recipe], crisp separations, no ornamental network noise.
DO NOT INCLUDE: fabricated nodes, random connectors, tiny illegible text, generic glowing-tech mesh.
```

### UI scenario illustration

```text
PURPOSE: Illustrate a conceptual workspace for [task]; this is not a faithful screenshot.
COMPOSITION: [ratio], one primary workflow, a few legible structural regions, generous outer margins.
VISUAL LANGUAGE: [recipe], consistent straight or softly editorial framing as declared by the slot.
DO NOT INCLUDE: real brand logos, plausible-but-fake metrics, account identities, notifications, dense generated interface copy.
```

### Data-poster backdrop

```text
PURPOSE: Create a visual field that amplifies the verified metric [meaning] while the exact number, unit, source, and qualification remain in HTML.
COMPOSITION: [ratio], strong empty region for the HTML metric, one supporting motif derived from [subject].
VISUAL LANGUAGE: [recipe], restrained rules, material texture, or abstract scale cue.
DO NOT INCLUDE: numbers, axes, labels, citations, fake charts, or decorative dashboard panels.
```

## Keep truth and typography outside the bitmap

- Generated text is not an authoritative label. Put important words, values, axes, captions, and citations in HTML or accessible SVG.
- Do not generate a real product interface from memory. Preserve or programmatically reframe the supplied screenshot.
- Do not let an illustration resemble evidence accidentally. Label it when context could confuse its status.
- Inspect every result for unintended glyphs, logos, watermarks, faces, extra limbs, false UI, and crop-sensitive subjects before accepting it.
