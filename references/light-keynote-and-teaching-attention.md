# Light Keynote + Human Teaching Attention (v1.8 RC)

## Goal
Default to a bright, low-noise teaching canvas. Complexity lives in the production graph, not on the frame.

## Visual default
- Warm-white `#FAFAF8`, white surfaces, dark neutral text.
- One primary accent per slide; semantic warning/success colors only when meaning requires them.
- No default grid, glow orbs, star particles or decorative rings.
- Borders are structural, not decorative. Prefer whitespace before containers.

## Six slide grammars
`hero`, `insight`, `diagram`, `comparison`, `image_annotation`, `conclusion`. A scene provider may be Mermaid, Shiki, KaTeX, Manim, a user image, a web asset, image generation, or a local primitive, but it must emit semantic target IDs before Attention is compiled.

## Attention ownership
Narration alignment owns time. Scene providers own objects and geometry. Attention owns gaze direction. Renderer owns pixels. None may silently take another layer's authority.

### Cursor
Cursor movement is deterministic and seek-safe. Use a minimum-jerk cubic path, subpixel coordinates and short dwell. Prefer 60fps output for cursor-heavy video, but 30fps remains a supported fallback by slowing travel and removing micro-movement.

### Pen
Pen actions are temporary marks: underline, circle, trace. The pen tip follows the actual stroke reveal. Do not leave all annotations on screen forever; clear or dim them when the narration moves on.

### Spotlight
Spotlight reduces surrounding contrast without destroying context. Light Keynote defaults to a restrained dim level (~0.34), not a black vignette.

### Reveal
Future information stays hidden until its cue. A reveal state is not merely opacity metadata for raster images: pre-baked information in screenshots or generated pixels must be cropped/masked or treated as overview context.

## Template providers
Canva, local presets, Figma-derived style tokens and other template connectors are optional providers. They may supply layout/style, but they do not own narration timing, semantic targets, cursor paths or final Attention choreography.
