---
name: skills-upgrade-2026-05
description: "2026-05-31 upgrade of ~/.claude research skills — added AER pipeline, enhanced review/lit, new method/citation/writing skills"
metadata: 
  node_type: memory
  type: project
  originSessionId: a5e1877c-05e2-42b4-b50e-2a6c388eddd0
---

On 2026-05-31 the global Claude Code research setup was expanded from **8 → 21 skills** (plus 2 agents). Builds on the original setup ([[project_setup]]) and the two-folder workflow ([[two_folder_workflow]]).

**Added — AER submission pipeline (brycewang `50-brycewang-aer-skills`):** `aer-workflow` (router), `aer-topic-selection`, `aer-identification`, `aer-introduction`, `aer-robustness`, `aer-tables-figures`, `aer-replication`, `aer-rebuttal`, `aer-submission`. AER is the user's target journal.

**Added — new skills:** `bib-validate` (citation verification vs CrossRef/OpenAlex/Semantic Scholar), `econometrics-playbook` (consolidated DiD/RD/IV/synth/DML method how-to + Stata/R/Python commands), `writing-deslop` (English anti-AI-detection prose audit), `data-cleaning` (reproducible Stata/R data prep, honors the user's Stata house rules).

**Enhanced in place:** `econ-reviewer` agent (added method-specific causal checklists: staggered DiD/event-study, IV/weak-IV, RDD, SCM, panel FE + AER referee calibration); `review-paper` skill (added optional `panel` mode = independent multi-referee panel + editor synthesis); `lit-review` skill (multi-source search + citation traversal + screening rubric, hands off to bib-validate).

**Dedup:** `aer-tables-figures` reconciled to defer to the `table-figure-format` rule (which forbids `tablenotes`/`figurenotes`). A 3-auditor collision check passed — no two skills duplicate an action; 5 one-line cross-refs added to harden lane boundaries (proofread↔writing-deslop, research-ideation↔interview-me, aer-identification↔econometrics-playbook, aer-replication↔aer-submission, bib-validate↔review-paper).

**Backup:** original 8 skills + 2 agents at `ClaudeFiles\_backup_2026-05-31\`. **Source clones** (large, deletable) at `ClaudeFiles\_skill_sources\`. Plan: `0.AI\quality_reports\plans\2026-05-31_claude-setup-upgrade.md`.

**Not done (optional follow-up):** Stata/R/Jupyter MCP servers (would let Claude *run* the user's Stata/R and read results back — recommended: SepineTam `mcp-for-stata`, Posit `mcptools`, datalayer `jupyter-mcp-server`).
