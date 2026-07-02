---
name: writing-deslop
description: Pre-submission anti-AI-detection audit of an English economics manuscript or section. Flags AI-tell prose (delve, "it is important to note", uniform tricolons, hedging clusters, mechanical sentence rhythm, em-dash overuse) while respecting standard economics phrasing, scores the draft, and gives hand-rewrites. Use before submitting a draft or when a section reads machine-generated. Produces a report without editing files.
argument-hint: "[filename or section, e.g. 'main.tex' or 'introduction']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Task"]
---

# writing-deslop — anti-AI-tell audit for economics prose

Audit an English economics manuscript or section for AI-generated writing tells, score it, and hand back concrete rewrites. **English only. Does NOT edit any source files — it produces a report.**

This is distinct from `proofread` (grammar, typos, notation, LaTeX) and from `journal-fit` (framing and house style). This skill targets *AI-tell prose* only. Defer grammar/notation issues to `proofread` and house-style/abstract conventions to `journal-fit`; do not duplicate their findings here.

## Steps

1. **Identify what to review:**
   - If `$ARGUMENTS` is a filename: read that file.
   - If `$ARGUMENTS` is a section name (e.g., "introduction"): find and read that section in `main.tex` or `paper_skeleton.tex`.
   - If no argument: ask the user which file or section to audit.

2. **Load the writing guide.** Read `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Academic.md` so flagged rewrites obey house prose rules (no equations in abstracts, actual numbers not "near-nominal", no boldface in running text, no bullets in body, "et al." for 3+ authors).

3. **Launch the deslop-auditor agent** on the content. The agent flags AI tells across the categories below, scores five dimensions, and writes hand-rewrites — while respecting the economics allow-list so legitimate academic phrasing is not flagged.

4. **Save the report** to:
   `quality_reports/[filename_without_ext]_deslop_YYYY-MM-DD.md`

5. **Present summary** to the user:
   - Overall score (out of 50) and verdict.
   - Counts by category and severity.
   - The three worst passages with their rewrites inline.
   - Path to the full report.

## What counts as an AI tell

- **Vocabulary tells.** delve, tapestry, realm, beacon, testament to, intricate/interplay, vibrant, showcase, underscore (verb), pivotal, crucial (as filler), landscape (metaphor), embark, foster, leverage (verb where "use" fits), seamless, robust (as vague praise, not the statistical sense), navigate (metaphor).
- **Throat-clearing and emphasis crutches.** "it is important to note that", "it is worth noting", "needless to say", "at the end of the day", "in today's world", "plays a crucial/vital/pivotal role".
- **Copula avoidance.** "serves as", "stands as", "represents", "boasts", "features" where "is" or "has" is correct.
- **Superficial -ing analyses.** Trailing participles that add no content: "highlighting its importance", "underscoring the need", "reflecting broader trends", "contributing to the literature".
- **Uniform tricolons / rule-of-three abuse.** Mechanical "A, B, and C" triads, three in a row, or three parallel sentences. Two items, or one full clause, is usually better.
- **Hedging clusters.** Stacked epistemic cushions in one claim ("may potentially suggest that ... could have the ability to ..."). Simplify to ONE appropriate hedge — do not strip hedging entirely (see allow-list).
- **Em-dash overuse.** Flag density above roughly one per 1,000 words; flag em dashes used as a default clause break where a comma, period, or parentheses fit.
- **Mechanically uniform rhythm.** Most sentences 15–25 words, every paragraph the same length, metronomic pacing. This is the strongest detector signal — flag it even when the vocabulary is clean.
- **Inflation and generic conclusions.** "a pivotal moment in the evolving landscape", "the future looks bright", "marks a turning point", significance puffery on routine results.
- **Synonym cycling and false ranges.** Rotating "households / agents / individuals / consumers" to avoid repetition; "from X to Y" pairings that span nothing meaningful.
- **Formatting tells.** Title-Case headings, bold-first bullets, "Despite these challenges..." formulas, em dashes in headings.

## RESPECT legitimate economics phrasing — do NOT flag these

Economics has its own register. The following are correct academic writing, NOT AI tells. Flag them ONLY when stacked in excessive clusters or used with no supporting result/citation.

- **Standard reporting verbs and frames.** "the paper finds", "we estimate", "we show", "we document", "the results indicate", "Table 3 reports", "column (2) shows", "the coefficient on X is", "we instrument X with Z".
- **Standard hedges (keep one per claim).** "suggests", "is consistent with", "is associated with", "we interpret this as", "may reflect", "likely". Economics requires epistemic caution; do not strip a single appropriate hedge.
- **Passive voice in methods/data.** "data were collected", "standard errors are clustered at the state level", "the sample is restricted to", "regressions are weighted by". Passive is correct and expected in methods.
- **Causal and identification language.** "identifies the causal effect", "the exclusion restriction requires", "parallel trends", "exogenous variation", "the estimand", "intent-to-treat".
- **Legitimate single-word transitions.** "Notably", "Importantly", "In contrast", "Conversely", "Specifically", "Moreover" — fine in isolation; flag only when three or more land in one paragraph.
- **"Robust" in its technical sense.** "robust standard errors", "robust to alternative specifications", "the result is robust" are correct. Flag "robust" only as vague praise ("a robust framework").
- **Domain terminology is precision, not jargon.** "instrumental variable", "fixed effects", "marginal effect", "general equilibrium" are exact terms — never flag them.

When in doubt, ask: is the phrase doing real economic work (reporting a result, defending identification, stating a method), or is it puffery/filler? Flag only the latter.

## Scoring

Rate the draft 1–10 on each dimension:

| Dimension | Question |
|-----------|----------|
| Directness | States findings, or announces and inflates them? |
| Rhythm | Varied sentence/paragraph length, or metronomic? |
| Specificity | Numbers, names, and exact terms, or vague declaratives? |
| Restraint | Appropriate hedging and tone, or puffery/stacked hedges? |
| Authenticity | Reads like a specific economist wrote it, or like an LLM? |

Total below 35/50: the draft needs a deslop pass before submission.

## Output Format

```markdown
# Deslop Audit: [Filename or Section]
**Date:** YYYY-MM-DD
**Score:** NN/50 — [Clean / Light pass / Needs deslop]

## Score by Dimension
| Dimension | Score (1-10) |
|-----------|--------------|
| Directness | N |
| Rhythm | N |
| Specificity | N |
| Restraint | N |
| Authenticity | N |
| **Total** | **NN/50** |

## Flags by Category
| # | Category | Location ("opening words...") | Flagged text | Rewrite | Severity |
|---|----------|-------------------------------|--------------|---------|----------|
| 1 | Vocabulary tell | Sec 1, "We delve into..." | "we delve into" | "we examine" | Major |

Severity: Critical (detector magnet) / Major (fix before submit) / Minor (polish).

## Worst Passages — hand-rewrites
> **Before:** [quoted passage]
> **After:** [rewrite preserving the argument, results, and an appropriate hedge]
> **Why:** [one line — which tell, why it reads as AI]

## Respected (NOT flagged)
Note any constructions that look AI-ish but are legitimate economics phrasing here, so the author knows they were considered and kept.

## Cross-references
- Grammar/typos/notation: run `proofread`.
- House style / abstract / target-journal framing: run `journal-fit`.
```

## Important

1. **Never edit source files.** Produce the report only.
2. **English only.** If the text is not English, say so and stop.
3. **Respect the economics allow-list.** A false positive on "we estimate" or a needed "suggests" is worse than a missed minor tell. When unsure, list it under "Respected", not "Flags".
4. **Preserve meaning and hedging.** Every rewrite keeps the economic claim, the numbers, and one appropriate hedge intact. Do not over-edit strong prose into the very uniformity you are removing.
5. **Rhythm over vocabulary.** Mechanically uniform sentence and paragraph length is the top detector signal — weight it heavily even when the word choice is clean.
6. **Quote specifics.** Every flag cites the offending text and a location by section + opening words (never line numbers).
7. **Recommend rewrite-from-scratch** when a passage trips 3+ categories and has uniform rhythm — patching individual words will not fix AI-generated structure.
8. **Do not duplicate `proofread` or `journal-fit`.** Stay in the AI-tell lane; cross-reference them for everything else.
