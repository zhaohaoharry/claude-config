---
name: Two-Folder LaTeX Workflow
description: Each research project has a local latex/ folder and a GitHub repo folder — how they relate
type: project
---

Key design decision for research projects: two LaTeX locations.

1. `latex\` — local only, never pushed. Programs save figures/tables here. ClaudeAnswer.tex lives here.
2. `[project-name-repo]\` — GitHub/Overleaf repo. main.tex + bib + style files + figures + tables live here.

**How to apply:** When user says "push to GitHub" or "share with coauthor" — run /sync-to-github first (copies figures/tables from latex/ to the repo folder), then commit and push the repo folder. The main.tex editing always happens directly in the repo folder.

First real project: `Research\Double Clinching Auction\Double-Clinching-Auction\` — already has main.tex, reference.bib, paper.sty, appendix_online.sty, bibliography.bst.
