# Claude Code config sync

Private mirror of the **configuration** parts of `~/.claude` so the same
Claude Code setup (global instructions, skills, hooks, agents, rules, and
curated memory) can be reused across computers.

This repo uses an **allowlist `.gitignore`**: everything under `~/.claude`
is ignored by default and only the items below are tracked. Secrets and
machine state are never committed.

## What IS tracked

| Path | Contents |
|------|----------|
| `CLAUDE.md` | Global instructions for all projects |
| `settings.json` | Permissions, hooks, statusline, model, env |
| `statusline.py` | Status-line script referenced by settings |
| `register-zotero-mcp.py` | Zotero MCP setup helper |
| `rules/` | Rule files referenced by `CLAUDE.md` |
| `skills/` | Custom skills |
| `agents/` | Custom subagents |
| `hooks/` | Hook scripts (bib-guard, econ-craft-reminder, ...) |
| `projects/*/memory/` | Curated auto-memory only (not transcripts) |

## What is NOT tracked (and why)

- `.credentials.json` — **OAuth token. Secret. Machine-specific.** Never sync.
- `projects/*` except `memory/` — session transcripts (~1.2 GB), per-machine.
- `file-history/`, `telemetry/`, `sessions/`, `shell-snapshots/`, `backups/`,
  `ide/`, `session-env/` — machine-local state / caches, regenerable.
- `settings.local.json`, `settings.backup-*.json` — machine overrides / backups.

## Set up on another computer

> **Requirement:** the other machine should use the **same Windows username
> (`haozh`)** and the same `Documents\Dropbox_Chapman\0.AI` path. The absolute
> paths in `settings.json` and the encoded `projects/*/memory/` folder names
> only resolve if these match. Different username/paths → edit `settings.json`
> and rename the memory folders accordingly.

**First-time setup** (turns the existing `~/.claude` into a clone of this repo
without deleting local credentials/state):

```bash
cd ~/.claude
git init
git remote add origin <REPO-URL>
git fetch origin
git checkout -f main          # brings config into place; ignored files untouched
```

**Ongoing sync**

```bash
cd ~/.claude
git pull        # on the machine that needs the latest config
# after changing config on any machine:
git add -A && git commit -m "update config" && git push
```

Your local `.credentials.json` and transcripts are ignored on every machine,
so pulling never touches your login or history.
