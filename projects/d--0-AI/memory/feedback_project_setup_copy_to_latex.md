---
name: Copy repo files to latex/ on project setup
description: When cloning a GitHub repo for a new research project, copy all files into the local latex/ folder
type: feedback
---

When setting up a research project from GitHub, copy all files from the cloned repo into `latex/` (the local working folder).

**Why:** The user works in `latex/` for local compilation and editing. Without the tex files, style files, bib files, figures, and tables there, the local folder is incomplete and unusable.

**How to apply:** After cloning the repo into `[Project]/[repo-name]/`, immediately copy everything (`cp -r repo/* latex/`) so `latex/` has all tex files, style files, bib, figures, tables, etc.
