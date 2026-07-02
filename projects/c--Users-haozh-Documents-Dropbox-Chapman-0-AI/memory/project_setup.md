---
name: Claude Setup Architecture
description: The full Claude Code setup built in April 2026 — file locations, two-source design, and what each component does
type: project
---

Claude Code setup completed 2026-04-05. Hybrid of Kown's system (coauthor) and Sant'Anna's psantanna.com framework.

**Why:** User is new to Claude Code and wanted a comprehensive setup for research, teaching, work, and ad hoc tasks.

**Architecture:**
- `~/.claude/CLAUDE.md` — global config (user identity, universal rules, LaTeX/Stata rules)
- `~/.claude/settings.json` — global permissions + hooks (pre-compact, log-reminder)
- `~/.claude/rules/` — plan-first-workflow, session-logging
- `~/.claude/agents/` — proofreader, econ-reviewer
- `~/.claude/skills/` — compile-latex, sync-to-github, proofread, review-paper, lit-review, research-ideation, interview-me
- `~/.claude/hooks/` — pre-compact.py, log-reminder.py
- `0.AI/CLAUDE.md` — workspace overview
- `0.AI/Claude Master/` — AI_Writing_Guide_Academic.md, master_catalogue.md (from coauthor Kown)

**How to apply:** When user opens any project, global rules auto-load. For research projects, project-level CLAUDE.md adds project state (HANDOFF.json) and folder layout. User never needs to type "START".
