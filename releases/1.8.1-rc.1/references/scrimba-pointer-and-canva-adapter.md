# Scrimba-style pointer choreography and Canva connector adapter

Status: v1.7.0-rc.1 design + browser reference implementation. The exact Scrimba production source is proprietary; sections marked **inference** describe a compatible implementation, not Scrimba's disclosed internal code.

## 1. What Scrimba officially exposes

Scrimba Explain describes an explainer as live-rendered typed slide content rather than a recorded screen. Code, diff and diagram slides expose real semantic objects, and the narration moves a pointer to the identifier, line, node or arrow being discussed. Explain streams slides as they arrive and synthesizes narration per slide.

The public docs do not publish the pointer renderer, easing curve, exact browser framework or export frame rate. Do not claim an exact library or FPS from appearance alone.

## 2. Why the pointer feels unusually smooth

**Inference from the disclosed live-rendering model:**

1. The slide is DOM/SVG content, not a flat video frame.
2. Each visible teaching object has a semantic target and measurable bounds.
3. Narration cues resolve to target IDs.
4. A screen-space cursor overlay moves between target anchors using a time-based curve.
5. The browser can update that overlay on `requestAnimationFrame`, normally at display refresh, while exported video can use 60fps when the renderer supports it.
6. Only `transform`, opacity and SVG stroke progress need change; the layout stays frozen during motion.

Perceived smoothness depends at least as much on path design, acceleration/deceleration, target dwell and low visual noise as on nominal frame rate.

## 3. Humanized teacher cursor contract

The cursor is part of the unified Attention Layer, never a scene plugin's private animation.

```json
{
  "cue_id": "C07",
  "target_id": "node:trade-remedy",
  "gesture": "click",
  "path": "minimum-jerk-bezier",
  "min_travel_ms": 180,
  "max_travel_ms": 520,
  "preferred_export_fps": 60
}
```

State machine:

```text
hidden → travel → arrive → hover/click/draw → dwell → clear → travel
```

Rules:

- use deterministic, seek-safe paths; no unseeded randomness;
- accelerate and decelerate with zero velocity at endpoints;
- use a restrained curved path, not perfectly straight robotic motion;
- arrival click may use a short scale/ripple, never repeated pulsing;
- underline/circle/trace moves the pen tip along the actual path;
- the cursor may travel slightly before the next spoken word, but future content may not reveal early;
- once the explanation settles, keep the cursor still or hide it;
- the global camera stays locked while the cursor is the primary focus;
- live HTML uses browser refresh; MP4 uses 60fps when supported, otherwise 30fps with longer travel and no micro-jitter.

Performance rules:

- animate `transform`, `opacity`, and SVG stroke progress only;
- pre-measure target geometry and freeze the layout;
- use subpixel cursor motion but integer-pixel text;
- do not query layout every frame;
- do not use CSS transitions whose state depends on playback history;
- evaluate every visual state from absolute time/frame.

## 4. Fallback ladder

```text
humanized cursor + drawing
→ simple pointer move
→ static focus box / spotlight
→ textual callout
→ no attention primitive
```

A renderer must declare the supported level. It cannot silently omit cursor or pen actions and report full fidelity.

## 5. Canva's role

Canva is a **template/style provider**, not the attention clock.

When the Canva connector is available, the workflow may:

- search brand templates;
- list brand kits;
- use an existing Canva design as a visual reference;
- generate a presentation shell from a reviewed outline;
- read design metadata, pages, text and page thumbnails when supported.

Canva may own:

- theme direction;
- base page background;
- typography and card style reference;
- page archetype inspiration;
- brand kit selection.

Anything to Explainer retains ownership of:

- claims and narration;
- semantic target IDs;
- cue timing;
- cursor, pen, reveal and spotlight choreography;
- final multi-aspect reflow;
- evidence/provenance;
- render and QC receipts.

## 6. Remote design is not a local render asset

The connected tool may expose template selection and design generation without exposing a guaranteed export/download action. Therefore:

```text
Canva template/design found
→ remote_design_reference
→ derive style tokens and page archetypes
```

Only when a separate export/materialization capability succeeds:

```text
remote design
→ exported page asset
→ local path + SHA-256 + receipt
→ renderer input
```

Without that receipt, use Canva as a style/layout reference and recreate the page in the deterministic renderer. Never pass a secured Canva URL to a renderer and call it a local file.

## 7. Platform routing

- ChatGPT / ChatGPT Work: use the connected Canva app when available; template choice remains a user-visible decision.
- Codex: use installed plugins/apps when the surface exposes them; otherwise consume a Canva design reference exported from ChatGPT/Work.
- Claude Code: Canva is only available if a trusted Canva MCP/custom integration is explicitly configured; do not infer it from generic MCP availability.

## 8. Current implementation boundary

Implemented in v1.7.0-rc.1:

- deterministic minimum-jerk Bézier cursor in the browser teaching preview;
- click ripple and pen-tip modes;
- cursor gestures compiled from narration beats;
- 60fps recommendation and 30fps fallback warning;
- Canva connector capability strategy compiler;
- optional Canva template-source slot with local preset fallback.

Not yet certified:

- production Remotion/HyperFrames cursor adapter across every grammar;
- pixel-identical Canva slide export and re-import;
- automatic semantic target extraction from arbitrary Canva designs;
- any claim about Scrimba's exact internal animation library or export FPS.
