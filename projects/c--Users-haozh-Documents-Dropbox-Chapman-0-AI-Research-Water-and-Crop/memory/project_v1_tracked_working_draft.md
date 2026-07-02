---
name: project-v1-tracked-working-draft
description: manuscript_v1.tex (colored tracks) is the working draft; v1_clean is a derived flattened render; never put \cite inside \del
metadata: 
  node_type: memory
  type: project
  originSessionId: 1c9297a7-78e0-4e12-8f2f-e99f8375927e
---

As of 2026-06-10 the working manuscript is `latex/manuscript_v1.tex`, the version with colored change-tracking (`\add` green, `\del` red strikeout, `\delx` red + [del] tag without strikeout). `latex/manuscript_v1_clean.tex` shares the same tracked body and differs ONLY in the 9 preamble macro definitions (clean renders `\add{x}` as plain x and `\del{x}` as nothing). Edit v1 first; regenerate v1_clean by copying v1 and swapping the macro block.

**Why:** The user explicitly said "I dont like working on the v1_clean. I still want to work on v1 with all those tracks."

**How to apply:**
- All manuscript edits go into `manuscript_v1.tex` with tracking marks: prose changes to base text as `\del{old}\add{new}`; edits inside an existing `\add{}` swap content in place; equations, tables, tabnotes, and notation update silently (apparatus, per the file's own convention).
- This applies to EVERY content edit, no matter how small. Dropping one word = `\del{word }`; swapping one word = `\del{old}\add{new}`. Do NOT make a clean replacement even for a single word — the user reviews changes in tracked form and reminded me 2026-06-17 to "use the delete and add tracker" after I made several clean word-drops. Mechanical fixes (whitespace, typos) are NOT content edits and stay silent.
- Tracks show base → current; do not stack intermediate wordings.
- NEVER put `\citet`/`\citep` inside `\del{}` — ulem's `\sout` breaks at compile once the .bbl resolves. Use `\delx{...}` for deletions containing citations.
- One-shot merge script archived at `latex/archive/2026-06-10_pre-panel-fixes/merge_v1_tracked.py` — do not re-run (it would flatten marks). Pre-merge backup: `latex/manuscript_v1.preR8merge.tex`.

Related: [[feedback-latex-working-dir]]
