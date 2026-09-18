# GitHub Canonical Sync

## Purpose

Chat threads do not share a guaranteed filesystem, attachment mount, hidden execution state, or `/mnt/data` path. A Skill can be installed in multiple chats while the files created by one chat remain scoped to that conversation/runtime. Therefore cross-thread recovery must use an external canonical source rather than assuming another thread's local artifacts are readable.

## Canonical source

Repository: `lishehao/lishehao`

Fixed bootstrap path:

`tools/anything-to-explainer/BOOTSTRAP.md`

Fixed latest manifest:

`tools/anything-to-explainer/latest.json`

Current versioned root:

`tools/anything-to-explainer/releases/1.8.1-rc.1/`

## Recovery algorithm

1. First use an installed GitHub connector/app if available. Fetch `tools/anything-to-explainer/latest.json` from `lishehao/lishehao`.
2. Read `version`, `release_root`, `required_text_files`, and `sha256`/content hashes if present.
3. Fetch `SKILL.md` and only the references necessary for the requested stage.
4. Do not treat a GitHub URL as a local render asset. If a binary or renderer input is required, materialize it through the host's supported download/file mechanism and record a receipt.
5. If GitHub connector access is unavailable, use normal web access to the same public raw files when possible.
6. If neither path is available, ask for the required file rather than reconstructing it from memory.
7. Never overwrite a newer local project state with an older GitHub release without comparing versions/hashes first.

## Recommended files to recover first

- `SKILL.md` — operational contract and routing rules.
- `SYNC_CONTEXT.md` — condensed architecture/state handoff for new chats.
- `references/teaching-system-design.md` — semantic scene and Attention architecture.
- `references/light-keynote-and-teaching-attention.md` — current visual defaults.
- `references/scrimba-pointer-and-canva-adapter.md` — pointer and Canva integration rules.
- `references/platform-optimization-v1.6.md` — host-specific execution behavior.
- `references/plugin-architecture.md` — typed plugin slots and compatibility model.

## What GitHub does not solve automatically

GitHub restores canonical text/specification and source snapshots. It does not automatically restore:

- another chat's hidden conversation context;
- uncommitted local edits;
- local browser login/session state;
- temporary `/mnt/data` files;
- secrets, API keys or cookies;
- rendered media that was never uploaded;
- an active Control Plane runtime unless its state was committed/exported.

For important projects, export a hash-bound handoff package and, when appropriate, commit the text manifests/state files to a project repository.
