# GitHub Canonical Sync

## Purpose

Chat threads do not share a guaranteed filesystem, attachment mount, hidden execution state, or `/mnt/data` path. NarrationFlow therefore uses a dedicated GitHub repository as its canonical cross-thread recovery source.

## Canonical source

Repository: `lishehao/NarrationFlow`

Fixed bootstrap path: `BOOTSTRAP.md`

Fixed latest manifest: `latest.json`

Current versioned root: `releases/1.8.1-rc.1/`

## Recovery algorithm

1. Use an installed GitHub connector/app if available and fetch `latest.json` from `lishehao/NarrationFlow`.
2. Read `version`, `release_root`, and `required_text_files`.
3. Fetch the versioned `SKILL.md`, `SYNC_CONTEXT.md`, and only the references necessary for the requested stage.
4. Compare versions before allowing GitHub state to replace a newer local handoff.
5. A GitHub URL is not a local render asset. Binaries must be materialized separately and recorded with a receipt.
6. If connector access is unavailable, use the public raw GitHub files when possible.
7. If neither route is available, ask for the missing artifact rather than reconstructing it from memory.

## What GitHub restores

- canonical Skill instructions;
- condensed cross-thread context;
- architecture and platform rules;
- visual-system and Attention conventions;
- versioned release metadata.

## What GitHub does not restore automatically

- hidden conversation context;
- uncommitted local edits;
- browser login/session state;
- temporary `/mnt/data` files;
- secrets, API keys or cookies;
- rendered media that was never uploaded;
- a running Control Plane process.

The old compatibility mirror at `lishehao/lishehao/tools/anything-to-explainer/` is intentionally retained for now, but this dedicated repository is the preferred canonical source.
