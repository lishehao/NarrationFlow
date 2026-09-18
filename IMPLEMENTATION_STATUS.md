# Implementation Status — v1.8.1-rc.1

## Implemented and regression-tested
- Light Keynote theme tokens and visual constraints.
- Six slide archetypes as a constrained composition layer.
- Narration-owned Attention contract with cursor, pen, spotlight and reveal.
- Seek-safe deterministic cursor evaluator with minimum-jerk paths, click pulse and pointer anchors.
- Pen underline/circle/path-trace state output.
- Typed `attention_overlay` workflow slot with `human-teaching-attention` and `static-focus-overlay` fallback.
- Canva remains an optional template/style provider; when absent, Light Keynote is the preferred local fallback.
- Platform/plugin matrix still compiles 343/343 declared combinations.

## Reference-implemented but not fully production-certified
- Remotion `HumanTeachingAttention.tsx` compiles against a local type stub and follows frame-derived animation rules; it has not been rendered through every supported renderer/host combination.
- 60fps is preferred for cursor-heavy output, but 30fps fallback is supported.

## Contract-only / incomplete
- Native Mermaid semantic extraction and geometry measurement.
- Shiki line/identifier geometry and complete diff adapter.
- KaTeX named-term geometry extraction.
- Manim moving-target track adapter.
- Automatic semantic-target extraction from arbitrary Canva pages.
- Universal Canva pixel export/materialization.

Do not describe contract-only items as production-complete.
