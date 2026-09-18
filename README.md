# NarrationFlow — Narration-Aligned Teaching Visual System

Version **1.8.1-rc.1**.

NarrationFlow turns research, documents, code, diagrams, screenshots and structured data into narration-first explainer videos. Its core production model is:

```text
claims + narration + real audio timing
                ↓
semantic teaching targets + aspect layouts
                ↓
unified Attention score
(pointer / pen / reveal / dim / focus)
                ↓
renderer or cross-platform handoff
```

## Current direction

- **Light Keynote** is the default visual system: bright background, low chrome, strong typography, one dominant accent, progressive disclosure.
- A single **Attention Director** aligns cursor, pen, spotlight, reveal and focus transfers to narration cues.
- Mermaid, code, formula, image, data and vector systems are pluggable scene providers; they do not own timing.
- Canva is an optional template/style provider, not the animation clock.
- ChatGPT Chat, ChatGPT Work, Codex and Claude Code use different host strategies but share the same project artifacts and contracts.
- GitHub is the canonical cross-thread source/state recovery layer.

## Cross-thread recovery

Start with:

```text
BOOTSTRAP.md
latest.json
SKILL.md
SYNC_CONTEXT.md
```

The ChatGPT Skill technical id remains `anything-to-explainer` for backward compatibility. The repository/product name is **NarrationFlow**.

## Status

Implemented at the current RC layer: teaching target contracts, cue-aligned state, Light Keynote defaults, humanized cursor reference, Canva strategy adapter, platform-aware routing, typed plugin graph, multi-aspect reflow and hash-bound handoff.

Still incomplete: full production adapters for every Remotion/HyperFrames grammar, native Mermaid semantic extraction, Shiki diff integration, KaTeX term geometry, Manim object tracks and arbitrary Canva semantic-target extraction.

See `IMPLEMENTATION_STATUS.md`, `CHECKS.md`, and `references/` for details.
