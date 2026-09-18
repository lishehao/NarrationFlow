# Hot-Pluggable Plugin Architecture

Anything to Explainer v1.4 separates the stable production contract from optional providers.

## Stable core vs plugins

The core always owns: brief, evidence ledgers, narration, timing contract, semantic shots, visual hierarchy, layout, attention, motion, runtime compilation, review gates and delivery manifest.

Plugins occupy typed slots:

- `web_discovery`
- `web_materialization`
- `transcription`
- `tts`
- `alignment`
- `visual_source`
- `video_broll`
- `renderer`
- `review`
- `storage`
- `editor_handoff`

Every plugin declares capabilities, artifact inputs and outputs, supported hosts/workflows, cost, privacy boundary, quality tier, retry scope, roles and fallbacks. A plugin may not read undeclared artifacts or silently invoke another provider.

## Execution-plan compiler

The compiler consumes:

```text
capabilities.json
+ workflow recipe
+ platform profile
+ free/quality/privacy policy
+ user approvals and actual inputs
```

It produces `control/execution_plan.json`. Selection happens by typed artifacts rather than tool names. A renderer cannot be selected until its required `runtime_plan` and visual artifacts exist. Image generation can cover hero/metaphor/fiction roles but cannot cover evidence.

## Selection modes

- `exclusive`: one provider owns the slot.
- `role-cover`: select the smallest compatible set that covers required visual roles.
- `all-compatible`: select at most two complementary providers; prevents module sprawl.

## Fallback closure

Every required slot must end in a local or planning-safe fallback. A missing external service may lower delivery from rendered video to project or planning package, but it may not leave the pipeline in an ambiguous half-state.

## Single-writer rule

Plugin outputs are immutable artifacts. The core runtime compiler is the only component allowed to merge them. Plugins never edit each other’s files.

## Runtime commands

```bash
python3 scripts/validate_plugin_registry.py --root .

python3 scripts/compile_execution_plan.py \
  --root . \
  --capabilities capabilities.json \
  --workflow product-teardown \
  --host codex \
  --policy free-first \
  --output control/execution_plan.json

python3 scripts/validate_execution_plan.py \
  control/execution_plan.json --root .
```
