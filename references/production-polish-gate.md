# Production Polish Gate — v1.8.2 RC

The gate exists because a semantically correct explainer can still look like a prototype. It blocks low-resolution, over-compressed, visually noisy or mechanically transitioned output from being labeled production.

## 1. Resolution and sampling

Production delivery minimums:

| Aspect | Minimum output |
|---|---|
| 16:9 | 1920×1080 |
| 9:16 | 1080×1920 |
| 4:5 | 1080×1350 |
| 3:4 | 1080×1440 |
| 1:1 | 1080×1080 |
| 4:3 | 1440×1080 |

When typography, thin vectors or cursor/pen strokes are prominent, prefer a 2× internal master and downsample to delivery size. A 540×960 vertical file is a draft/preview, not a production master.

## 2. Frame rate

- Cursor/pen-heavy teaching scenes: prefer and validate 60fps.
- 30fps is allowed when the renderer cannot sustain 60fps, but simplify motion: longer travel, no micro-jitter, fewer tiny strokes, and permit static-focus fallback.
- A nominal 60fps file does not pass if motion is quantized, duplicated incorrectly or visibly stutters.

## 3. Encoding quality

For H.264 production masters prefer CRF 17–20. If only bitrate control is available for a 1080-class H.264 output, use at least about 8 Mbps for 60fps or 5 Mbps for 30fps as a hard floor; higher may be appropriate for text-heavy motion. Do not optimize for tiny file size before visual QC.

HEVC/AV1 may use lower bitrates at equivalent quality; validate visually rather than reusing H.264 bitrate floors.

## 4. Typography and line quality

- Hard fail if effective production text falls below 22px on a 1080-class output.
- Warn below 28px unless it is a deliberately secondary source label.
- Thin vectors, focus rings and pen strokes must survive export without crawling, shimmering or compression breakup.
- Use high-quality font rasterization and avoid scaling already-rasterized text.

## 5. Attention polish

Priority for emphasis:

```text
cursor hover
→ soft highlight
→ underline / bracket
→ path trace
→ circle
```

Circle is a low-frequency gesture, not the default highlight. More than ~3 circle events/minute triggers review; >6/minute fails the default profile.

Cursor rules:
- avoid covering the exact text/data being explained;
- use semantic pointer anchors instead of rectangle centers where possible;
- hide or park the cursor when narration no longer needs it;
- no idle wobble;
- max text/target occlusion should remain below the configured threshold.

## 6. Transition continuity

Blanket full-slide crossfade is a fallback. Before each scene transition, detect whether the next scene continues a semantic object from the previous one.

If yes, prefer:
- shared-element carry;
- object-to-title transition;
- chart/diagram morph;
- focus carry-over;
- pointer-led transition.

A high ratio of crossfade-only transitions triggers review. If several clear shared-element opportunities exist and none are used, the gate warns even when the video is technically valid.

## 7. Required visual review

A production render needs:
- a whole-video contact sheet;
- motion samples for videos longer than 30 seconds;
- transition samples when scene transitions exist;
- encoded-output inspection, not only source-code review.

The review should check typography, density, cursor occlusion, circles/annotations, scene continuity, compression, color consistency and whether future information appears early.

## 8. Gate artifact

Write:

`review/production_polish_report.json`

Validate with:

```bash
python3 scripts/validate_production_polish.py \
  review/production_polish_report.json \
  --profile templates/production_polish_profile.json
```

A failed report blocks the final production label. Warnings are review items, not silent passes.
