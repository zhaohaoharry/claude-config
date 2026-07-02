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

2. **Launch the proofreader agent** on the content.
   The agent checks:
   - Grammar (agreement, articles, prepositions, tense)
   - Typos (misspellings, duplicated words, artifacts)
   - Notation consistency (symbol used for two things, subscript inconsistency)
   - Academic writing quality (per AI_Writing_Guide_Academic.md rules):
     - No undefined hedges ("near-nominal", "substantial")
     - No equations in abstract
     - No boldface in running text
     - No bullet points in main body
     - "et al." for 3+ authors
     - Table notes left-aligned
   - LaTeX issues (overfull hbox, undefined references)

3. **Save the report** to:
   `quality_reports/[filename_without_ext]_proofread_YYYY-MM-DD.md`

4. **Present summary** to user:
   - Total issues found
   - Breakdown by category
   - Most critical issues highlighted
   - Path to full report
