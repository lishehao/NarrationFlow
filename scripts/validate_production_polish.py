#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def add(bucket, code, message):
    bucket.append({"code": code, "message": message})

def main():
    p=argparse.ArgumentParser()
    p.add_argument("report")
    p.add_argument("--profile", default="templates/production_polish_profile.json")
    args=p.parse_args()
    report=load(args.report)
    profile=load(args.profile)
    fails=[]; warns=[]

    out=report.get("output", {})
    aspect=out.get("aspect")
    w=int(out.get("width") or 0); h=int(out.get("height") or 0)
    minimum=profile["minimum_resolution"].get(aspect)
    if not minimum:
        add(fails,"unknown_aspect",f"Unsupported/missing aspect: {aspect!r}")
    elif w < minimum[0] or h < minimum[1]:
        add(fails,"resolution",f"{w}x{h} is below {aspect} production minimum {minimum[0]}x{minimum[1]}")

    fps=float(out.get("fps") or 0)
    attention=report.get("attention", {})
    cursor_heavy=bool(attention.get("cursor_heavy"))
    static_fallback=bool(attention.get("static_focus_fallback"))
    if cursor_heavy and fps < profile["cursor_heavy_min_fps"] and not static_fallback:
        add(fails,"cursor_fps",f"Cursor-heavy output requires {profile['cursor_heavy_min_fps']}fps or an explicit static-focus fallback")

    codec=str(out.get("codec") or "").lower()
    crf=out.get("crf")
    bitrate=out.get("video_bitrate_mbps")
    if codec in {"h264","libx264","avc","avc1"}:
        if crf is not None and float(crf) > profile["h264"]["preferred_crf_max"]:
            add(fails,"h264_crf",f"H.264 CRF {crf} exceeds production max {profile['h264']['preferred_crf_max']}")
        if bitrate is not None:
            floor=profile["h264"]["hard_bitrate_floor_mbps_60fps"] if fps >= 50 else profile["h264"]["hard_bitrate_floor_mbps_30fps"]
            if float(bitrate) < floor:
                add(fails,"h264_bitrate",f"H.264 bitrate {bitrate} Mbps is below {floor} Mbps floor for this frame rate")

    typo=report.get("typography", {})
    min_font=float(typo.get("min_effective_font_px") or 0)
    hard=profile["typography"]["hard_min_effective_font_px"]
    warn=profile["typography"]["warn_min_effective_font_px"]
    if min_font and min_font < hard:
        add(fails,"font_size",f"Minimum effective font {min_font}px is below hard floor {hard}px")
    elif min_font and min_font < warn:
        add(warns,"font_size",f"Minimum effective font {min_font}px is below preferred {warn}px")

    duration=float(out.get("duration_s") or 0)
    circles=float(attention.get("circle_events") or 0)
    if duration > 0:
        cpm=circles/(duration/60.0)
        if cpm > profile["attention"]["fail_circle_events_per_minute"]:
            add(fails,"circle_frequency",f"{cpm:.2f} circle events/min exceeds fail threshold")
        elif cpm > profile["attention"]["warn_circle_events_per_minute"]:
            add(warns,"circle_frequency",f"{cpm:.2f} circle events/min exceeds preferred threshold")

    occ=float(attention.get("cursor_text_occlusion_max_ratio") or 0)
    if occ > profile["attention"]["fail_cursor_occlusion_ratio"]:
        add(fails,"cursor_occlusion",f"Cursor occlusion ratio {occ:.3f} exceeds fail threshold")
    elif occ > profile["attention"]["warn_cursor_occlusion_ratio"]:
        add(warns,"cursor_occlusion",f"Cursor occlusion ratio {occ:.3f} exceeds preferred threshold")

    tr=report.get("transitions", {})
    count=int(tr.get("count") or 0); cross=int(tr.get("crossfade_only") or 0)
    if count:
        ratio=cross/count
        if count >= 4 and ratio > profile["transitions"]["fail_crossfade_only_ratio"]:
            add(fails,"crossfade_ratio",f"{ratio:.0%} of transitions are crossfade-only")
        elif ratio > profile["transitions"]["warn_crossfade_only_ratio"]:
            add(warns,"crossfade_ratio",f"{ratio:.0%} of transitions are crossfade-only")
    opp=int(tr.get("shared_element_opportunities") or 0)
    used=int(tr.get("shared_element_used") or 0)
    if opp >= 3 and used/opp < profile["transitions"]["warn_shared_element_use_ratio"]:
        add(warns,"shared_element_usage",f"Only {used}/{opp} detected shared-element opportunities were used")

    review=report.get("review", {})
    if profile["review"]["contact_sheet_required"] and not review.get("contact_sheet"):
        add(fails,"contact_sheet","Production review requires a whole-video contact sheet")
    if duration > profile["review"]["motion_samples_required_over_seconds"] and not review.get("motion_samples"):
        add(fails,"motion_samples","Long-form production review requires motion samples")
    if count and profile["review"]["transition_samples_required_when_transitions_exist"] and not review.get("transition_samples"):
        add(fails,"transition_samples","Transition samples are required when transitions exist")

    result={"passed":not fails,"failures":fails,"warnings":warns}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if fails else 0

if __name__ == "__main__":
    raise SystemExit(main())
