# NarrationFlow 1.8.2-rc.1

Production Polish Gate release.

Adds:
- 1080-class minimum production resolution for every supported aspect ratio;
- 60fps preference for cursor/pen-heavy teaching scenes;
- H.264 CRF 17–20 guidance plus bitrate hard floors when CRF is unavailable;
- typography floor checks;
- circle-frequency and cursor-occlusion review;
- transition continuity review with shared-element opportunity tracking;
- mandatory whole-video contact sheet and motion/transition samples;
- `scripts/validate_production_polish.py` and `templates/production_polish_profile.json`.

A preview can still render at lower resolution, but it cannot be labeled production until the polish gate passes.
