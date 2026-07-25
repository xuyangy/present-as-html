# Motion Grammar for Editorial Pages

Use this reference when motion intensity is 5 or higher, several sections change state, or the page uses scrollytelling, shared-element transitions, Canvas, or complex focus choreography. For restrained entrances and feedback, the Design Playbook is sufficient.

## Contents

1. Write a motion brief
2. Shape rhythm and easing
3. Choose a semantic pattern
4. Implement reliable states
5. Verify the calm version

## Write a motion brief

For each animated section, record:

```yaml
reader-purpose: show how the route accumulates evidence
semantic-units: stop, connecting segment, annotation
stable-anchor: route baseline and prior stops
trigger: intersection threshold | explicit control | state change
initial-state: complete static route at low emphasis
changed-state: current stop and segment focused
final-state: complete labeled route
interruptibility: normal scroll remains available
reduced-motion: stacked static stages
javascript-failure: complete final state
```

Animation is allowed to focus or sequence meaning; it may not create the only copy of that meaning.

## Shape rhythm and easing

A substantial sequence needs contrast among orientation, build, focus, resolution, and rest. Do not distribute identical movement or information density across the whole page. Let the reader settle before and after the highest-information change.

Use a small easing vocabulary:

```css
:root {
  --ease-settle: cubic-bezier(.16, 1, .3, 1);
  --ease-emphasis: cubic-bezier(.34, 1.56, .64, 1);
  --ease-standard: cubic-bezier(.4, 0, .2, 1);
}
```

- **Settle:** entrances, panels, focus transitions, and shared geometry.
- **Emphasis:** rare tactile feedback or a small overshoot; never long prose or large camera moves.
- **Standard:** symmetric state changes where start and end have equal weight.
- **Linear:** only for genuinely constant progress, rotation, or time; not ordinary entrances.

Use short holds around consequential results so the reader can register the change. Avoid `transition: all`; name the properties and durations that carry meaning.

## Choose a semantic pattern

### Shared-element continuity

Use FLIP, View Transitions, or measured transforms when the same object changes location or scale. Preserve identity instead of cross-fading between two unrelated copies.

### Staged accumulation

Reveal a few semantic siblings in order, keeping prior units visible. Derive the number of columns, steps, or marks from the data rather than duplicating a JavaScript count in fixed CSS.

### Focus transfer

Reduce secondary contrast, saturation, or sharpness while the focal unit strengthens. Keep the background readable enough to preserve context, and avoid a flash that could trigger photosensitivity.

### Process, path, or causal trace

Draw or highlight the primary relationship while muted secondary connections remain visible. Do not animate arrows that imply causality absent from the source.

### State comparison

Keep the baseline fixed and animate only the changed attributes. Update corresponding labels and values together; never hide the reference state needed for comparison.

### Chunk or phrase reveal

For generated or narrated text, reveal meaningful phrases or chunks rather than individual letters. The complete text must already exist accessibly and appear immediately under reduced motion.

### Responsive geometric transformation

Let a code-native motif reorganize across breakpoints only when the transformation expresses the subject. Test each breakpoint as an intentional composition, not merely a scaled desktop frame.

## Implement reliable states

- Give every absolutely positioned layer an intentional positioned ancestor.
- Wait for `document.fonts.ready` and one animation frame before measurements tied to glyph or layout geometry.
- Prefer `transform` and `opacity`; animate layout properties only when the behavior genuinely requires reflow.
- Keep initial HTML readable. Add enhancement classes from JavaScript after initialization instead of hiding content by default.
- Use `IntersectionObserver` for entry/exit awareness and explicit buttons for reader-controlled stages.
- Seed or remove randomness when visual states must be reproducible for review.
- Cancel animation frames, observers, timers, and autoplay when static mode or reduced motion is active.
- Avoid rare Unicode glyphs unless the selected fonts demonstrably contain them; use labeled HTML shapes for control keys or symbols when needed.
- Keep scene transitions spatially continuous. Crossfade around a stable anchor instead of creating accidental blank intervals.

For complex timelines, separate state calculation from playback so a given state or time produces a deterministic frame. This makes debugging, screenshots, resizing, reduced motion, and manual controls reliable.

## Verify the calm version

- Every fact, label, relationship, and control remains available without animation.
- Normal scrolling, space, and arrow keys are not trapped by a sequence.
- Focus order and state announcements match the visible change.
- Resizing does not leave stale measurements or off-canvas layers.
- Fonts are loaded before geometry-dependent motion begins.
- The sequence can be interrupted and resumed without replaying irrelevant entrances.
- Reduced motion removes parallax, camera travel, autoplay, and large transforms rather than merely shortening them.
- Static mode produces a deliberately composed frame, not an animation frozen at an arbitrary instant.
