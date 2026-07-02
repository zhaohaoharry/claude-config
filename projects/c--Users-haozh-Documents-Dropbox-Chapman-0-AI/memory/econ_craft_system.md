---
name: econ-craft-system
description: "The positive prose-craft layer added 2026-06-06 — EconCraft guide, exemplar library, econ-craft skill, and auto-injecting hook"
metadata: 
  node_type: memory
  type: project
  originSessionId: 20d1a03d-3473-4e85-9554-c7ff2c743ac0
---

Built 2026-06-06 to fix the root cause of mechanical paper prose: the writing setup was almost entirely *negative* (the stop-sign list in `AI_Writing_Guide_Academic.md` removes AI tells) with no *positive* craft layer teaching what good econ prose does.

The system (all under `0.AI/Claude Master/` unless noted):
- `AI_Writing_Guide_EconCraft.md` — 18 craft principles (flow, rhythm, voice, intuition-first, number-argument), an 8-category idiom bank, a per-paper-type cheat sheet, and a reconciliation appendix. Subfield-tagged. Banner: "clarity is the floor; sounding like a specific economist is the ceiling." Defers to the academic guide on every surface conflict.
- `econ_prose_exemplars.md` — 16 verified-verbatim passages (Akerlof, Coase ×2, Card-Krueger, Cochrane, Cengiz et al., Finkelstein, Autor-Dorn-Hanson, Chetty et al., Varian, Friedman, Sword, Angrist-Pischke, Krugman, Leamer, Deaton), each tagged with the one move it shows.
- `_research/econ_writing_craft_brief.md` + `_research/econ_writing_craft_evidence.json` — provenance. Every quote traces to a verified source URL.
- Skill `~/.claude/skills/econ-craft/SKILL.md` — model-invoked on write/draft/revise/polish/tighten of paper prose. Default = applies the craft in place (edits the .tex); `--audit` = report only.
- Hook `~/.claude/hooks/econ-craft-reminder.py` (registered under `UserPromptSubmit` in `settings.json`) — auto-injects a load-the-craft-layer reminder when a writing intent is detected in the 0.AI workspace. Keyword lists are at the top of the script for tuning; fires on (write-verb AND prose-noun) OR intent-phrase, gated to the workspace, silent on code prompts.

**Why:** clean prose with no tells can still read like a competent machine. The craft layer is the difference between passing a detector and sounding like a real economist.

**How to apply:** when writing/refining prose, load both writing guides and the exemplars and apply the craft, or run `econ-craft`. The academic guide stays authoritative on surface rules. Lanes: `writing-deslop` removes tells, `journal-fit` is house style, `proofread` is correctness, `econ-craft` builds register. Both `CLAUDE.md` files and the academic guide's cross-references point to this system. Related: [[skills_upgrade_2026_05]], [[project_setup]].
