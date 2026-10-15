---
name: Compile in latex folder only
description: Never compile LaTeX in the repo folder — it syncs to Overleaf and must stay clean. Compile locally in latex/ only.
type: feedback
---

Never compile LaTeX in the GitHub/Overleaf repo folder. The repo folder syncs to Overleaf, so it must contain only source files (tex, bib, sty, bst, figures, tables).

**Why:** Compilation artifacts (aux, log, bbl, pdf, etc.) would pollute the Overleaf sync.

**How to apply:** After editing `[repo]/main.tex`, copy it (plus bib, sty files) to `latex/` and compile there. This applies to ALL research projects, not just Carbon Batteries. Update the CLAUDE.md compilation instructions accordingly.
