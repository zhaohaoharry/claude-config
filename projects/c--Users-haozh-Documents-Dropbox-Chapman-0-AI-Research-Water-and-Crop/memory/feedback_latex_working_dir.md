---
name: Work in latex/ not repo folder
description: All working tex files and compilation should happen in latex/, not the Shared-farm-ownership-and-water-traffic/ repo folder
type: feedback
---

All working LaTeX files and compilation should happen in the `latex/` folder, not the `Shared-farm-ownership-and-water-traffic/` repo folder. The repo folder is for syncing with Overleaf only.

**Why:** The repo folder syncs to GitHub/Overleaf. Working files, drafts, and compilation should stay local in `latex/` to avoid pushing unfinished work.

**How to apply:** When creating new tex files, editing drafts, or compiling, always use `latex/` as the working directory. Only use the repo folder when syncing final versions via `/sync-to-github`.
