---
name: proofread
description: Run proofreading on a paper or section. Checks grammar, typos, notation consistency, and academic writing quality. Reports findings for review-only requests; supports applying corrections when the user requests repair. For AI-generated / machine-sounding prose tells, use writing-deslop.
argument-hint: "[filename or section, e.g. 'main.tex' or 'introduction']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Task"]
---

# Proofread

Run the proofreading protocol on the specified file or section. Produces a detailed report. **Review-only requests produce a report without edits. If repair was requested, use the findings to apply scoped corrections and verify the result.**

## Steps

1. **Identify what to review:**
   - If `$ARGUMENTS` is a filename: read that file
   - If `$ARGUMENTS` is a section name (e.g., "introduction"): find and read that section in the context-resolved current manuscript root
   - Resolve the file or section from the current request, selection, conversation, and live project state; ask only if the target remains materially ambiguous.

2. **Load the house standard.** Read `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Academic.md` in full. Do not work from a remembered summary of it — the guide is 615 lines and changes, and any short list inlined here will drift out of date. Sections §1 (voice and register), §2 (sentence-level patterns), §6 (citations), §9 (LaTeX headings and housekeeping), and §10 (structural rules) are the proofreading-relevant ones.

3. **Launch the `proofreader` agent** on the content. Pass **only** the file path or extracted passage and the target journal — not the drafting conversation or your own account of what the text is trying to do. A reviewer starting cold outperforms one carrying the author's framing.
   The agent checks:
   - Grammar (agreement, articles, prepositions, tense)
   - Typos (misspellings, duplicated words, artifacts)
   - Notation consistency (symbol used for two things, subscript inconsistency)
   - Academic writing quality, against the guide as loaded in step 2
   - LaTeX issues (overfull hbox, undefined references)
   - **Not** AI-tell prose, register, or rhythm — that is `writing-deslop`'s lane, and duplicate flags on the same em-dash help nobody.

4. **For a requested audit or substantial review, save the report** to:
   `quality_reports/[filename_without_ext]_proofread_YYYY-MM-DD.md`

5. **Complete the requested mode.** For repairs, apply supported corrections, preserve project tracking, and verify the edited artifact before reporting. Skip a separate report for a micro typo repair unless requested. For review-only work, leave sources unchanged.

**Present summary** to user:
   - Total issues found
   - Breakdown by category
   - Most critical issues highlighted
   - Path to full report, when a report was required and saved

For a repair request, the main agent applies supported findings and performs project verification before delivery; delegated reviewers remain read-only. Routine micro repairs need no separate report or repeated audit. If a requested independent reviewer is unavailable, perform a clearly labeled self-review and continue unless independence itself is a required deliverable.
