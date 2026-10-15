---
name: claude-config-sync-repo
description: Private GitHub repo that mirrors ~/.claude config for cross-computer sync
metadata: 
  node_type: memory
  type: reference
  originSessionId: a5fabaad-740c-45c6-879d-7fad327dfe38
---

Claude Code config is synced across the user's computers via a **private** GitHub
repo: **https://github.com/zhaohaoharry/claude-config** (created 2026-07-02).

The git repo lives **at `C:\Users\haozh\.claude` itself**, using an *allowlist*
`.gitignore` (ignore everything; re-include only chosen paths). Tracked: `CLAUDE.md`,
`settings.json`, `statusline.py`, `register-zotero-mcp.py`, `rules/`, `skills/`,
`agents/`, `hooks/`, and `projects/*/memory/` only. Excluded: `.credentials.json`
(OAuth token) and all session transcripts/caches (`projects/*` except memory,
`file-history/`, `telemetry/`, etc.).

**Update after config changes** (from `~/.claude`): `git add -A && git commit -m "..." && git push`.

**Set up on a new machine**: `cd ~/.claude`, `git init`, `git remote add origin <url>`,
`git fetch origin`, `git checkout -f main` (overwrites tracked config, leaves local
credentials/transcripts untouched). Requires the machine to use username `haozh`
and the same `Documents\Dropbox_Chapman\0.AI` path, else the absolute paths in
`settings.json` and the encoded `projects/*/memory/` folder names won't resolve.
Pulling a private repo needs GitHub auth on that machine too (gh or GCM).

`gh` CLI (2.95.0) is installed at `C:\Program Files\GitHub CLI\gh.exe`; not on the
default shell PATH until a new shell picks up the updated PATH. Related: [[portable_setup_2026_06]].
