# Palette Families

Use this reference only when the selected recipe's default palette needs a content-appropriate variant. Choose a complete bundle and map it to the recipe's semantic tokens; do not assemble a palette from favorite individual swatches.

## Contents

1. Choose a palette as a system
2. Derive color from the subject
3. Editorial paper-and-ink bundles
4. Swiss signal-color bundles
5. Apply and verify

## Choose a palette as a system

- Preserve semantic roles: `paper`, `ink`, `muted`, `line`, `wash`, `accent`, and `accent-on`.
- Use one bundle across the page. A bounded inverse section may swap paper and ink; it does not introduce a second palette.
- Treat the recipe as authoritative for material behavior. A Press palette may use paper texture and editorial shadow; a Swiss palette keeps flat fills, square edges, and no gradients.
- User or brand colors outrank these presets. When brand colors are supplied, derive the missing semantic roles and check contrast instead of rejecting the brand.
- Accent is a signal, not ambient decoration. Use it for active conclusions, exceptions, paths, or one meaningful comparison state.

## Derive color from the subject

Treat preset values as fallback anchors, not a reason to give unrelated subjects identical palettes. Use three steps:

1. **Sample:** take candidate colors from supplied brand assets, authentic subject imagery or artifacts, and the subject's real material or cultural context. Do not sample demonstration brands inside a product screenshot as though they belong to the product itself.
2. **Converge:** reduce the system to one neutral scale plus two or three chromatic roles. Use OKLCH to create perceptually ordered lightness steps and controlled chroma; avoid a bag of unrelated hex values.
3. **Justify:** write one sentence explaining the source and treatment of each consequential color. If the rationale is only “it looks good,” the palette is not yet content-led.

Example:

```css
:root {
  --subject-hue: 32;
  --paper: oklch(.95 .025 var(--subject-hue));
  --wash: oklch(.89 .035 var(--subject-hue));
  --ink: oklch(.19 .018 var(--subject-hue));
  --muted: oklch(.46 .025 var(--subject-hue));
  --accent: oklch(.55 .12 var(--subject-hue));
}
```

For paper or print character, keep large surfaces low-chroma and reserve stronger chroma for small signals. Cultural associations depend on lightness, saturation, material, and context—not hue names alone. A muted mineral red and a high-chroma retail red communicate different worlds.

Do not create dark mode by inverting the light palette. Re-derive surface, text, muted, line, accent, image, and focus roles for the dark context, then verify them separately. Omit dark mode when it has no reader or brand purpose.

## Editorial paper-and-ink bundles

These fit Press Editorial, Archival Field Guide, Raw Document, and restrained Evidence-led pages.

### Ink Classic

Neutral, versatile, and publication-like.

```css
--ink: #0a0a0b;
--paper: #f1efea;
--wash: #e8e5de;
--inverse: #18181a;
--muted: #65625c;
--line: #c5c0b7;
```

### Indigo Porcelain

For research, engineering, technical culture, and deep analysis.

```css
--ink: #0a1f3d;
--paper: #f1f3f5;
--wash: #e4e8ec;
--inverse: #152a4a;
--muted: #586576;
--line: #bdc6d0;
```

### Forest Ink

For ecology, place, culture, and longform nonfiction.

```css
--ink: #1a2e1f;
--paper: #f5f1e8;
--wash: #ece7da;
--inverse: #253d2c;
--muted: #637067;
--line: #c8c3b7;
```

### Kraft Paper

For history, books, craft, archives, and warm human stories.

```css
--ink: #2a1e13;
--paper: #eedfc7;
--wash: #e0d0b6;
--inverse: #3a2a1d;
--muted: #756654;
--line: #c6b399;
```

### Dune

For art, architecture, fashion, and design criticism.

```css
--ink: #1f1a14;
--paper: #f0e6d2;
--wash: #e3d7bf;
--inverse: #2d2620;
--muted: #6e6558;
--line: #c9bda9;
```

Add one low-area accent only when the source needs a signal. Derive it from a real subject, material, annotation convention, or brand rather than choosing it at random.

## Swiss signal-color bundles

These fit Swiss Structured and other rational modernist pages. The neutral system remains fixed; select exactly one accent and its corresponding foreground.

```css
--paper: #fafaf8;
--ink: #0a0a0a;
--wash: #f0f0ee;
--line: #d4d4d2;
--muted: #737373;
```

| Signal | Accent | `accent-on` | Useful for |
| --- | --- | --- | --- |
| IKB blue | `#002fa7` | `#ffffff` | technology, design, institutions, general use |
| Cadmium lemon | `#ffd500` | `#0a0a0a` | youth, retail, activity, warnings on a light signal |
| Highlighter green | `#c5e803` | `#0a0a0a` | ecology, future systems, emerging technology |
| Safety orange | `#ff6b35` | `#ffffff` | industry, urgency, decisions, physical systems |

Swiss constraints:

- no gradients, translucent accent fog, colored shadows, or mixing two signal colors;
- use straight edges and flat fills; an accent block should not also depend on shadow or glass effects;
- keep accent area low. Large accent fields must carry a major structural or semantic role;
- use `accent-on` exactly as declared and still verify text contrast at the actual font size and weight.

## Apply and verify

1. Copy the chosen bundle into the page tokens and record its name in the Design Read or project design context.
2. Derive any missing RGB or alpha values from the token; do not introduce untracked hex colors throughout the stylesheet.
3. Check paper/ink, muted/paper, accent/paper, and accent-on/accent combinations.
   Target at least 4.5:1 for ordinary text and 3:1 for large text and essential graphical boundaries, unless a stricter project standard applies.
4. Inspect normal, inverse, print, and reduced-motion captures. Paper texture, animation, or blending must not be required for contrast.
5. Search for stray literal colors and either assign them a semantic role or remove them.
