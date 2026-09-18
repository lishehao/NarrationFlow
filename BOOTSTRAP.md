# Anything to Explainer — GitHub Bootstrap

This directory is the canonical cross-thread recovery mirror for Anything to Explainer.

Current release: **1.8.1-rc.1**

## For a new ChatGPT / Work / Codex / Claude Code thread

1. Read `latest.json` first.
2. Fetch the versioned `SKILL.md` and `SYNC_CONTEXT.md` from the release root declared there.
3. Fetch only the mirrored reference files needed for the current task.
4. If the current conversation also contains a newer project handoff/ZIP, compare versions and hashes before choosing which state wins.
5. Never assume files from another thread's `/mnt/data`, browser session, hidden state, or uploads are available here.
6. GitHub is the canonical text/spec recovery layer. Render assets, secrets, browser login state, full source snapshots and uncommitted project files still require explicit materialization or handoff.

## Fixed paths

- Bootstrap: `tools/anything-to-explainer/BOOTSTRAP.md`
- Latest manifest: `tools/anything-to-explainer/latest.json`
- Current release: `tools/anything-to-explainer/releases/1.8.1-rc.1/`

## Recovery priority

1. `SKILL.md`
2. `SYNC_CONTEXT.md`
3. `references/github-canonical-sync.md`
4. `references/light-keynote-and-teaching-attention.md`
5. `references/scrimba-pointer-and-canva-adapter.md`
6. `references/platform-optimization-v1.6.md`
7. `references/plugin-architecture.md`

The full source package contains additional references and implementation files; this GitHub mirror is intentionally the minimum reliable recovery core.
