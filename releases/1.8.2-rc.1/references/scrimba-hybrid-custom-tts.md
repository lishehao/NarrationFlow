# Scrimba Explain hybrid path with custom TTS

Status: design guidance for NarrationFlow. Scrimba's public/plugin interfaces currently expose authored narration text, slide content and image attachments, but no custom-audio upload/replace input.

## Current Explain Video Generator inputs exposed to ChatGPT

The installed plugin exposes four actions:

1. Start an explainer stream with title, description and visibility.
2. Append authored OPML chunks. The model can author narration text plus structured teaching content such as Mermaid diagrams, LaTeX math, code walkthroughs and before/after diffs.
3. Attach a user-shared image to the open explainer. The current connector accepts conversation images (png/jpeg/webp/gif) and returns an attachment id for an image slide.
4. Finish the stream.

The phrase "custom narration" in the connector means custom narration **script/content**, not an external audio waveform.

On Scrimba's own web composer, supported teaching inputs also include code/source files, text/Markdown, PDFs, images and Jupyter notebooks.

## Current TTS boundary

Scrimba synthesizes narration as slides arrive. Its public docs allow narration regeneration while keeping the script/slides unchanged, but regeneration chooses Scrimba's voice again. The current ChatGPT plugin does not expose:
- audio file upload as narration;
- external TTS URL;
- voice-clone id;
- per-word externally supplied timestamps;
- replace-audio endpoint.

Therefore a custom TTS cannot currently be treated as a native Scrimba narration provider through the exposed plugin contract.

## Why naive audio replacement drifts

The Scrimba visual timeline and pointer choreography are authored/rendered against Scrimba's own synthesized narration timing. Replacing the final audio track with a different TTS voice changes:
- total slide duration;
- pause placement;
- word duration;
- emphasis timing;
- sentence boundary timing.

Even when total durations happen to match, pointer-to-word timing can still feel wrong inside a slide.

## Supported hybrid strategy

If custom voice quality matters more than native Scrimba synchronization:

```text
author exact narration script
→ render Scrimba explainer with that script
→ export Scrimba video (+ captions when available)
→ synthesize the same script with custom TTS
→ forced-align Scrimba audio and custom TTS to the same words
→ derive slide / phrase anchors
→ piecewise time-remap the video
→ replace audio
→ cursor/transition QC
```

Do not simply replace the audio track and keep the original video timestamps.

## Retiming granularity

Recommended engineering heuristics, not Scrimba guarantees:

- <= ~3% duration difference and very similar pauses: a single light time-stretch may be acceptable after visual QC.
- ~3–8% difference: retime at least per slide.
- > ~8–10%, or noticeably different pauses/emphasis: use phrase/sentence anchors.
- repeated local changes above ~15–20%: prefer re-authoring the pacing or rendering in NarrationFlow with custom TTS as the master clock.

When time-remapping a 60fps UI/diagram video, moderate segment speed changes are usually visually tolerable, but abrupt segment boundaries can create cursor acceleration discontinuities. Smooth segment timing or re-render attention when possible.

## Best-quality alternative

Use Scrimba as a rapid storyboard/reference renderer and NarrationFlow as the final renderer:

```text
NarrationFlow script + custom TTS
        ↓
audio timings become canonical
        ↓
Scrimba-style slide/attention grammar
        ↓
NarrationFlow / Remotion render
        ↓
1080-class 60fps master
```

This preserves custom voice timing exactly and avoids post-hoc synchronization repair, at the cost of implementing more of the visual system ourselves.
