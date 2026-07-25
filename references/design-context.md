# Design Context and Provenance

Use this reference when a page must belong to an existing brand, product, publication, organization, or design system, or when new claims about a current real-world subject will be added beyond the supplied source.

## Contents

1. Know when context is required
2. Gather context in priority order
3. Separate source claims from added facts
4. Create a context record
5. Resolve gaps and conflicts

## Know when context is required

Run this workflow when any of these is true:

- the user requests an on-brand page;
- a real product, organization, or publication is the visual subject;
- the user provides a brand guide, codebase, UI kit, reference site, screenshots, or existing materials;
- the page will use identity-critical logos, product imagery, interfaces, or exact brand tokens;
- the design adds current specifications, dates, status, or other externally verifiable claims.

Do not require a logo or brand audit merely because an organization is mentioned incidentally in prose. Editorial mention and visual identity are different responsibilities.

## Gather context in priority order

1. **User-provided system:** guidelines, design tokens, components, fonts, templates, and explicit prohibitions.
2. **User-provided assets:** logos, product images, screenshots, diagrams, prior publications, and approved campaigns.
3. **In-scope codebase:** token files, global CSS, font loading, layout scaffold, and two or three representative components or pages.
4. **Official public sources:** current brand or press pages, product pages, documentation, media kits, and verified repositories.
5. **Supplied references:** use the user's declared relationship—direct, style, palette, or composition.
6. **Selected page recipe:** use only as a fallback grammar after the available context is understood.

Extract exact values and observable patterns rather than describing the context from memory. Record source and date for externally retrieved material.

When a brand or product is the visual subject, prioritize recognition-critical assets before cosmetic token matching: official logo, physical product imagery, or current product UI as applicable. Colors and fonts support recognition but do not replace the subject itself. Follow [Asset Sourcing and Selection](asset-sourcing.md) to compare, verify, and record files. Do not impose this requirement on an incidental editorial mention.

For a codebase, capture the smallest sufficient set:

- color and spacing tokens;
- font stacks and real available weights;
- radius, border, and shadow behavior;
- page shell and alignment spines;
- image, icon, caption, and control treatment;
- one or two signature interactions or compositional moves;
- explicit accessibility and responsive conventions.

Do not bulk-copy a component system into an editorial page. Translate its visual vocabulary to the content-led form.

## Separate source claims from added facts

Treat supplied text as the source to preserve, not as permission to silently rewrite its claims. If the user did not request fact-checking, retain its attribution and wording without presenting new verification claims.

Verify before adding any external factual assertion about a current named product, person, organization, event, specification, version, price, availability, or policy. Prefer official or primary sources; record uncertainty rather than filling gaps from memory.

Keep these categories distinct:

- **Supplied claim:** present in the source; preserve and attribute as provided.
- **Verified addition:** added for context and supported by a recorded source.
- **Editorial inference:** a synthesis drawn from the source; label or phrase it as interpretation.
- **Placeholder:** explicitly unresolved and not presented as fact.

Never fabricate a product screen, logo, quotation, metric, testimonial, or source to make the page feel complete.

## Create a context record

For a substantial brand-sensitive project, create `design-context.md` beside the output:

```markdown
# Design Context

## Scope
- Subject and page purpose:
- Context collected on:
- Completeness: complete | partial | inferred

## Facts
- Supplied claims:
- Verified additions and source URLs:
- Unresolved or intentionally unverified:

## Core assets
- Logo variants and allowed placement:
- Product or documentary imagery:
- UI or artifact screenshots:
- Attribution and licensing notes:

## Tokens
- Color roles and exact values:
- Typography and available weights:
- Spacing, radius, borders, and shadows:

## Visual vocabulary
- Alignment and composition patterns:
- Image and caption treatment:
- Motion and interaction behavior:
- Signature details worth preserving:

## Prohibitions and gaps
- Explicitly forbidden treatments:
- Missing assets or unresolved conflicts:
```

Connect CSS variables and asset paths to the record instead of retyping approximate values throughout the page. A context record is useful only when implementation actually follows it.

## Resolve gaps and conflicts

- If a required identity asset is missing, ask for it or use an explicit placeholder; do not redraw it from memory.
- If official sources disagree with supplied materials, identify the exact conflict and let the user choose when it affects identity or meaning.
- If marketing and product interfaces use different but legitimate systems, select the one matching the page's purpose and record that choice.
- If a downloaded asset has the wrong file signature, inadequate dimensions, stale interface state, watermarks, or demonstration-brand contamination, reject it even when the URL appears official.
- If a reference conflicts with the user's brand, assign responsibilities explicitly—for example, brand controls tokens while the reference contributes composition only.
- If no context exists, say so in the Design Read and proceed with a content-led recipe rather than pretending the result is on-brand.
