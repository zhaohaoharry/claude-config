---
name: Always follow the Research Project Template exactly
description: When setting up or migrating a project, use the exact folder structure from ClaudeFiles/Research Project Template/CLAUDE.md — no improvising
type: feedback
---

Never improvise folder names or structure when setting up a research project. Always follow the template in `ClaudeFiles/Research Project Template/CLAUDE.md` exactly.

**Why:** User had to correct a setup where I created flat top-level folders (rawdata/, graph/, log/) instead of the correct nested structure. The template is strict and all projects must match.

**How to apply:** Key rules:
- `data/raw/` for original data (never modified), `data/clean/` for processed data, `data/temp/` for intermediate
- Figures go in `latex/figures/`, NOT a top-level `graph/` folder
- Tables go in `latex/tables/`
- `program/sandbox/` for experimental code, `program/[lang]/` for production, `program/archive/` for retired
- No top-level rawdata/, graph/, log/, sandbox/ folders
- When migrating old projects, map old folder contents into the correct template locations
