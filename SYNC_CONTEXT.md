# Anything to Explainer — Cross-thread Context

Current canonical version: **1.8.1-rc.1**.

## Core architecture

Anything to Explainer is narration-first. Real audio owns time; visual providers create semantic scene objects; one unified Attention Director aligns pointer, pen, reveal, spotlight and focus to narration cues; renderers consume a frozen runtime plan.

The current default visual system is **Light Keynote / minimal teaching**: warm-white or very light backgrounds, strong typography, one dominant accent color, low chrome, six slide archetypes, progressive disclosure, object permanence and purpose-driven transitions. Decorative dark-tech grids, glowing circles, random particles and perpetual camera movement are not defaults.

## Current teaching primitives

Content grammars: diagram, code, formula, vector, image, data.

Slide archetypes: hero, insight, diagram, comparison, image_annotation, conclusion.

Attention primitives: pointer travel, click, hover/dwell, underline, circle, trace/path, spotlight, reveal and focus transfer. Humanized cursor behavior is narration-bound and optional; 60fps is preferred when the renderer genuinely supports it, with static focus as fallback.

## Plug-in model

Media/template providers are hot-pluggable and must normalize outputs into semantic scene packages. Image generation is an optional asset provider. Canva is a template/style provider, not the attention clock. Mermaid is a structural scene provider, not the final visual authority. Missing plugins must degrade explicitly and semantically.

## Platform model

ChatGPT Chat: research, file analysis, planning, previews and production packs.
ChatGPT Work: long browser workflows and background/multi-step web work.
Codex: repository-backed implementation, shell, renderers, tests and QC.
Claude Code: terminal/MCP production and controlled headless workflows.

Platform names do not prove a capability exists; capability probing and a platform strategy are required.

## Continuity rule

If a new thread cannot see prior files, fetch the canonical GitHub bootstrap/manifest instead of guessing prior state. Conversation-local artifacts remain conversation-local until explicitly externalized.
