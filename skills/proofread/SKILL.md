---
name: proofread
description: Run proofreading on a paper or section. Checks grammar, typos, notation consistency, and academic writing quality. Produces a report without editing files. For AI-generated / machine-sounding prose tells, use writing-deslop.
argument-hint: "[filename or section, e.g. 'main.tex' or 'introduction']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Task"]
---

# Proofread

Run the proofreading protocol on the specified file or section. Produces a detailed report. **Does NOT edit any source files.**

## Steps

1. **Identify what to review:**
   - If `$ARGUMENTS` is a filename: read that file
   - If `$ARGUMENTS` is a section name (e.g., "introduction"): find and read that section in main.tex
   - If no argument: ask the user which file to proofread

2. **Load the house standard.** Read `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Academic.md` in full. Do not work from a remembered summary of it — the guide is 615 lines and changes, and any short list inlined here will drift out of date. Sections §1 (voice and register), §2 (sentence-level patterns), §6 (citations), §9 (LaTeX headings and housekeeping), and §10 (structural rules) are the proofreading-relevant ones.

3. **Launch the `proofreader` agent** on the content. Pass **only** the file path or extracted passage and the target journal — not the drafting conversation or your own account of what the text is trying to do. A reviewer starting cold outperforms one carrying the author's framing.
   The agent checks:
   - Grammar (agreement, articles, prepositions, tense)
   - Typos (misspellings, duplicated words, artifacts)
   - Notation consistency (symbol used for two things, subscript inconsistency)
   - Academic writing quality, against the guide as loaded in step 2
   - LaTeX issues (overfull hbox, undefined references)
   - **Not** AI-tell prose, register, or rhythm — that is `writing-deslop`'s lane, and duplicate flags on the same em-dash help nobody.

4. **Save the report** to:
   `quality_reports/[filename_without_ext]_proofread_YYYY-MM-DD.md`

5. **Present summary** to user:
   - Total issues found
   - Breakdown by category
   - Most critical issues highlighted
   - Path to full report
