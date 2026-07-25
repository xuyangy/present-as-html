# Asset Sourcing and Selection

Use this reference when a page needs real logos, product images, interface captures, documentary photographs, scans, maps, or other externally sourced media. Collect candidates before committing the composition.

## Contents

1. Decide what is actually required
2. Search in a trustworthy order
3. Build and score a candidate set
4. Treat identity assets differently
5. Verify and record accepted files

## Decide what is actually required

Start from the semantic slots in [Media Framing and Fidelity](media-framing.md). For each slot, state the reader question, necessity class, subject, fidelity, ratio, safe area, minimum useful resolution, and attribution needs.

Do not collect “an image per section.” Search only for slots where real media supplies evidence, identity, orientation, comparison, or irreplaceable atmosphere. A missing essential asset changes the composition; a missing ornamental asset should usually disappear.

## Search in a trustworthy order

Use the highest applicable source:

1. user-supplied and already approved files;
2. official brand, product, press, documentation, repository, app-store, or institutional sources;
3. primary archives, museums, libraries, public agencies, research repositories, or Wikimedia Commons;
4. reputable stock or editorial collections with suitable usage terms;
5. generated illustration for non-identity-critical, non-documentary purposes;
6. an honest sized placeholder when none of the above meets the slot.

For a current real product or identity, verify existence, version, date, and official source before downloading. Save accepted assets locally; do not hotlink a fragile remote URL.

## Build and score a candidate set

Do not use the first plausible result. Gather enough distinct candidates to make selection meaningful, then keep only the few that serve different narrative jobs. Record:

```yaml
candidate-id: ferry-view-03
slot-id: s02-place-anchor
source-page: https://example.org/item/123
direct-file: https://example.org/files/123-large.jpg
creator: supplied or verified name
rights-and-attribution: public domain | license | permission | unresolved
dimensions: 3200x2133
date-or-version: when relevant
scores:
  truth-and-authority: 10
  relevance: 9
  resolution: 9
  crop-safety: 8
  visual-consistency: 8
  independent-narrative-value: 9
decision: accepted | reserve | rejected
reason: establishes the actual site and leaves a quiet left third
```

Use a ten-point judgment, not false mathematical precision. A hero or evidence asset should normally be excellent across truth, relevance, and technical quality; a supporting asset should still clear a strong quality bar. Prefer one excellent image to several mediocre ones. When a candidate would lower trust or visual coherence, use less media or a placeholder.

Inspect candidates together, not one by one. Check whether lighting, perspective, color, historical period, interface version, scale, and caption treatment can form one visual world without disguising factual differences.

## Treat identity assets differently

When a brand or product is the visual subject, recognition-critical assets outrank approximate color styling:

- use the exact official logo rather than redrawing it;
- use official product imagery for a physical product;
- use current authentic UI for a digital product;
- preserve supplied identity assets unless the user authorizes transformation;
- obtain light/dark or horizontal/stacked variants only from approved sources.

Do not require identity assets for an incidental editorial mention. If a required logo, product image, or UI state cannot be found or verified, ask for it or use an explicit placeholder; do not fabricate a substitute.

## Verify and record accepted files

Before use:

- confirm the downloaded file type rather than trusting its extension;
- verify pixel dimensions, SVG `viewBox`, transparency, and visible content;
- reject HTML error pages, tiny thumbnails, watermarked previews, corrupt files, and stale UI versions;
- inspect for private data, demonstration-brand contamination, or misleading crops;
- record creator, source page, direct file, retrieval date, rights/status, required credit, and any edits;
- retain the original and create derived crops or optimized versions under separate stable filenames.

Connect the accepted file to its slot record, alt text, caption, and attribution. If status is unresolved, keep that uncertainty visible rather than silently treating the asset as cleared or authoritative.
