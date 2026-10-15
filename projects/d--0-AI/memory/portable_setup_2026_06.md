---
name: portable-setup-2026-06
description: "Portable Setup installer rebuilt 2026-06-11 — full setup transfer package for coauthor + laptop, lives in ClaudeFiles\\Portable Setup"
metadata: 
  node_type: memory
  type: project
  originSessionId: f326134a-aad3-488a-b55d-70a72ea3b7f5
---

`0.AI\ClaudeFiles\Portable Setup\` is the transfer package for replicating the full Claude Code setup on other machines (coauthor's computer, Hao's laptop). Rebuilt fresh on 2026-06-11 from the live setup (22 skills, 6 hooks, 6 rules, 2 agents, statusline, settings template, writing guides, Research Project Template). The pre-2026-06 stale version is in `_archive_2026-06-11\` inside it.

Layout: `claude-home\` mirrors the portable parts of `~/.claude`; `workspace\` holds the 0.AI-side files (only needed on non-Dropbox machines, i.e. the coauthor's). Install pattern: open the folder in Claude Code on the target machine and paste `SETUP_PROMPT_COAUTHOR.md` or `SETUP_PROMPT_LAPTOP.md` — Claude there copies files and fixes hardcoded paths (12 package files contain `haozh` paths; the prompts say to grep and fix all hits). `settings.template.json` uses `{{PYTHON}}`/`{{CLAUDE_HOME_FWD}}`/`{{HOME_FWD}}`/`{{WORKSPACE}}` placeholders; model pin deliberately excluded.

Deliberately excluded from the package: credentials, memory/sessions, `Claude Master\journal_exemplars\` (~199 MB raw PDFs — distilled guides already ship inside the journal-fit skill), `_research\`.

Side fix on 2026-06-11: `AI_Writing_Guide_Email.md` was missing from the live `Claude Master\` (referenced by global CLAUDE.md but existed only in the old portable archive) — restored it to `Claude Master\`.

When the live setup changes, rebuild the package before re-installing elsewhere — it is a snapshot, not a sync. Related: [[project-setup]], [[skills-upgrade-2026-05]].
