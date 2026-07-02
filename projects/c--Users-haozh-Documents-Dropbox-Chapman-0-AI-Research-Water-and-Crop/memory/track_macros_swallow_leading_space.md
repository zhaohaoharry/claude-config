---
name: track-macros-swallow-leading-space
description: In manuscript_v1.tex the \add/\delx/\addblock track-change macros swallow a LEADING space inside the argument, so word.\add{ Next} renders as word.Next; put spaces OUTSIDE the macro
metadata:
  type: project
---

The track-change macros in `latex/manuscript_v1.tex` are color wrappers:
`\newcommand{\add}[1]{{\color{addgreen}#1}}` (and `\delx`, `\addblock` similar).

**Gotcha (verified by rendering 2026-06-17):** a LEADING space inside the braced
argument is swallowed at render. TRAILING spaces are preserved.
- `investment.\add{ As a result}`  -> renders "investment.As a result"  (BUG)
- `\add{... second half. }Had`      -> renders "... second half. Had"     (fine)
- `range.}\add{Three patterns}`     -> renders "range.Three patterns"      (BUG, macro abuts macro)

**Rule when writing tracked additions: put the inter-word/inter-sentence space
OUTSIDE the macro, in the black text.**
- Write `investment. \add{As a result}`, NOT `investment.\add{ As a result}`.
- At a macro-to-macro boundary write `range.} \add{Three}`, NOT `range.}\add{Three}`.

Do NOT add a space between a `\del{old}\add{new}` (or `\delx{old}\add{new}`)
REPLACEMENT pair — those must stay adjacent (e.g. `\del{25}\add{22}` = "25->22").
Only period-ending macro closes followed by `\add{Capital}` need the space.

A reusable detector/fixer lives at `program/sandbox/fix_add_spaces.py` (dry-run by
default, `--write` to apply; P1 = leading-space-in-macro, P2 = `.}\add{Capital`).
Detection ground truth is the RENDERED PDF, not `fitz.get_text()` — get_text drops
spaces at every color-span boundary, so it FALSE-positives on `\add{...} Next`
(space after the brace is fine) and needs a glyph-gap/image check to confirm.
On 2026-06-17 this fixed 34 swallowed spaces across the draft. Related:
[[feedback_evaluate_prose_before_showing]].
