import json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/"scripts"/"validate_production_polish.py"
PROFILE=ROOT/"templates"/"production_polish_profile.json"

def run_report(tmp_path, report):
    p=tmp_path/"report.json"
    p.write_text(json.dumps(report), encoding="utf-8")
    return subprocess.run([sys.executable, str(SCRIPT), str(p), "--profile", str(PROFILE)], capture_output=True, text=True)

def good_report():
    return {
      "output":{"aspect":"9:16","width":1080,"height":1920,"fps":60,"codec":"h264","crf":18,"video_bitrate_mbps":10,"duration_s":120},
      "typography":{"min_effective_font_px":30},
      "attention":{"cursor_heavy":True,"circle_events":3,"cursor_text_occlusion_max_ratio":0.04},
      "transitions":{"count":8,"crossfade_only":2,"shared_element_opportunities":4,"shared_element_used":2},
      "review":{"contact_sheet":True,"motion_samples":True,"transition_samples":True}
    }

def test_good_report_passes(tmp_path):
    r=run_report(tmp_path, good_report())
    assert r.returncode==0, r.stdout+r.stderr

def test_low_resolution_fails(tmp_path):
    x=good_report(); x["output"]["width"]=540; x["output"]["height"]=960
    r=run_report(tmp_path,x)
    assert r.returncode==2 and "resolution" in r.stdout

def test_low_bitrate_fails(tmp_path):
    x=good_report(); x["output"]["video_bitrate_mbps"]=0.1
    r=run_report(tmp_path,x)
    assert r.returncode==2 and "h264_bitrate" in r.stdout

def test_circle_overuse_fails(tmp_path):
    x=good_report(); x["attention"]["circle_events"]=20
    r=run_report(tmp_path,x)
    assert r.returncode==2 and "circle_frequency" in r.stdout
