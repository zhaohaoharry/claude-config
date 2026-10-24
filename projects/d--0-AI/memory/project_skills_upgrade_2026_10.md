---
name: project_skills_upgrade_2026_10
description: "Econ-skills upgrade implemented 2026-10-24 (from amatray skills, StatsClaw, defensive-writing and data-shortcut discussions): what was added and where"
metadata:
  node_type: memory
  type: project
  originSessionId: 289dc0b7-ec4e-49c9-9f91-c985baf50d43
  modified: 2026-10-24T06:32:05.534Z
---

Implemented 2026-10-24 at the user's "go ahead and implement the whole plan". Config syncs via claude-config autosync at session end ([[claude_config_sync_repo]]).

- **New skills:** `verify-code` (StatsClaw pattern, Qin & Xu 2026, MIT: comprehension gate, isolated spec/test-spec/sim-spec, tester never sees source, reviewer tolerance-integrity audit); `model-derivation` (adapted from amatray `solving-model`: one-step derivation, units/limits/SymPy checks, blind re-derivation by fresh subagent; external GPT oracle dropped; no per-phase gates); `cite-verify` (claim-vs-source, Zotero first via `tools/zotero_lookup.py`, which copies sqlite+WAL).
- **Data integrity:** new rule `~/.claude/rules/data-integrity.md` (ledger, coverage cards, sentinel scan, 5%/5%/80% stop thresholds, merge rules, estimation-N reconciliation); helpers `skills/data-cleaning/tools/sample_flow.py` and `sample_flow.do` (both tested); PostToolUse hook `hooks/data-guard.py` flags bare dropna, unvalidated/inner merges, keep(match), nogen, drop-if-missing, na.omit; data-cleaning now covers Python; econometrics-playbook output adds SAMPLE and COVERAGE.
- **Writing:** Personal guide rule 3.8 "No defensive writing" with the deletion test; flag in writing-deslop and deslop-auditor; econ-craft step 5a drafts long redrafts in a fresh subagent without chat history; one line added to the econ-craft-reminder hook.
- **Review/proofread:** econ-reviewer labels FATAL/ADDRESSABLE/TASTE; review-paper desk review (2b) and report quality check (4b); proofread standing feedback at `quality_reports/proofread_standing_feedback.md` and document-wide consistency sweep.
- Not copied: amatray memory/overleaf/compile-latex/pdf-chunker/prompt/skill-creator/review-plan*; StatsClaw brain/shipper/workflows.

**Why:** strengthen verification of AI-produced derivations, code, citations, data handling and prose.
**How to apply:** if the user reports false positives from data-guard or thresholds that are too strict, tune `data-guard.py` patterns or set project thresholds in the project CLAUDE.md. H2's config is a hand copy and does not have these rules (see machines-and-sync 6a).
