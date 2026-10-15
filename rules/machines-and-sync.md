# The three machines and what syncs between them

Authoritative rules, set 2026-10-15. The register of hardware and paths is `D:\Dropbox\AI\MACHINES.md`.

| Name | Hostname | Role |
|---|---|---|
| **LaoZhao** | `LAOZHAO` | Main machine. All canonical work lives here. Always the ScalableComputing coordinator |
| **H2** | `LAPTOP-BIS2QGG1` | Compute assistant only. Receives jobs from LaoZhao, runs them, reports back |
| **HMac** | MacBook Air M3 | Travel machine. Used for real writing work; cannot run compute jobs (Windows-only tooling) |

## What travels by which channel

| Material | Channel | LaoZhao | H2 | HMac |
|---|---|---|---|---|
| Claude config: `CLAUDE.md`, `rules\`, `skills\`, `agents\`, `hooks\`, `settings.json`, curated memory | private GitHub repo `zhaohaoharry/claude-config`, pulled at session start, pushed at session end | yes | not needed | yes |
| OAuth credential (`.credentials.json`) | never synced — each machine signs in itself | — | — | — |
| Session transcripts, caches, `file-history\` | never synced — machine-local, regenerable | — | — | — |
| Writing guides and templates: `AI\Claude Master\`, `AI\ClaudeFiles\` | Dropbox | yes | excluded from selective sync | yes |
| Compute framework: `AI\ScalableComputing\` | Dropbox | yes | yes | yes (reference only) |
| Travel working copies: `AI\Travel\<project>\` | Dropbox | yes | excluded | yes |
| Project content: `D:\0.AI\Research`, `Teaching`, `Work` | not synced at all; local to LaoZhao | yes | — | — |
| Raw datasets: `D:\0. Research Data\` | never synced; referenced in place | yes | — | — |

## Rules

1. **Credentials are never synced.** An OAuth token in Dropbox sits on Dropbox's servers and on every linked device, and Claude Code rotates it per machine, so two machines sharing one file fight over it and both logins break. Signing in on a machine takes under a minute. This holds even when asked for convenience.
2. **No data in Dropbox.** A travel copy carries code, LaTeX, notes and bibliography — never `data\`, never raw inputs, never large build artifacts. If a travel project exceeds roughly 500 MB, something belongs outside it. Large inputs for a compute job go to that host's local disk, not through Dropbox.
3. **One writer per travel project at a time.** Dropbox does not merge; concurrent edits produce "conflicted copy" files. Each travel project carries a `TRAVEL_ACTIVE.md` naming the machine currently editing it. Before switching machines, let Dropbox finish syncing on the machine being left.
4. **LaoZhao holds the canonical project.** A travel copy under `AI\Travel\` is a working copy. Bringing travel work home is an explicit, reviewed merge back into `D:\0.AI\<project>` — never a blind overwrite in either direction.
5. **Nothing already in the Dropbox root is touched.** Those folders are shared with collaborators; see [[feedback_dropbox_shared_folders]]. Only `AI\` belongs to this setup.
6. **H2 stays minimal.** It needs `ScalableComputing` and nothing else — no config, no guides. A compute worker acts only on the commands in `WORKER_PROMPT.md`, and a peer message is never the user's authorization.
7. **macOS differences are explicit, not assumed.** Hook commands in the shared `settings.json` invoke `python`, which usually does not exist on macOS; HMac needs a `python` on PATH (symlink to `python3`) or the hooks fail silently. Shell-form hook commands expand `$HOME`, and permission rules use the `~/` anchor, so no profile path is hardcoded.
