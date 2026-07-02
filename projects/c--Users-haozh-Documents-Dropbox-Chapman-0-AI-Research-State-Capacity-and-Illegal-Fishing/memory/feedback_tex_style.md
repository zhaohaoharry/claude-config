---
name: Use existing paper.sty and bibliography.bst
description: All LaTeX files must use the user's paper.sty and bibliography.bst — add packages to sty if needed but never replace the style setup
type: feedback
---

All .tex files must use the user's existing `paper.sty` and `bibliography.bst` style files. These produce a look the user likes.

**Why:** The user has invested in a consistent visual style across projects. Codex's output already uses this setup and looks good.

**How to apply:** When creating or editing .tex files, always use `\usepackage{paper}` and `\bibliographystyle{bibliography}`. If additional LaTeX packages are needed, add them inside `paper.sty` rather than adding `\usepackage{}` calls directly in the .tex file. Never replace or override the style setup.
