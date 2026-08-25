---
name: writing-deslop
description: Pre-submission audit of an English economics manuscript or section for prose a referee would register as machine-written. Flags house stop-sign terms, AI-tell prose (delve, "it is important to note", uniform tricolons, hedging clusters, metronomic rhythm, em-dashes), and overclaiming (scope widening, tense drift, dropped qualifiers), while respecting standard economics phrasing. Scores the draft and gives hand-rewrites. Use before submitting a draft or when a section reads machine-generated. Produces a report without editing files.
argument-hint: "[filename or section, e.g. 'main.tex' or 'introduction']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Task"]
---

# writing-deslop — audit economics prose for machine-written register

Audit an English economics manuscript or section for prose that reads as machine-written, score it, and hand back concrete rewrites. **English only. Does NOT edit any source files — it produces a report.**

This is distinct from `proofread` (grammar, typos, notation, LaTeX) and from `journal-fit` (framing and house style). Defer grammar/notation issues to `proofread` and house-style/abstract conventions to `journal-fit`; do not duplicate their findings here.

**The target is a human referee, not a detector.** AI-text detectors key on dataset-specific artifacts, degrade sharply out of domain, and systematically over-flag polished formal academic prose and non-native English writers — which is to say they over-flag exactly what a good economics manuscript looks like. Optimizing toward a lower detector score pushes prose *away* from proper register. Audit for what a referee would notice, and never treat a detector score as evidence.

## Precedence — the academic guide wins

`AI_Writing_Guide_Academic.md` is authoritative on every surface rule. Where this file and the guide disagree, follow the guide and note the override in the report. The known cases:

**Precedence order:** the author's own recorded rules in `AI_Writing_Guide_Personal.md` outrank the academic guide, which outranks the craft guide, which outranks anything generic. A rule the author stated while looking at real output beats a rule stated in the abstract.

| Rule | This skill's older reading | Authoritative reading |
|---|---|---|
| Em-dashes, colons, semicolons in prose | an em-dash density quota; colons unmentioned | Flag all three for review. The default is to remove, but roughly 15–25% legitimately stay. Keep an em-dash when a parenthetical already contains commas, or for one strong rhetorical contrast. Keep a semicolon joining two short tightly coupled clauses. Keep a colon before a list or a defined term. **The fix is a rewrite, not a substitution** — see below |
| "Notably", "Importantly", "Crucially", "Furthermore" | flagged on sight as glue | **Legitimate econ register. Do not flag in isolation.** Flag only when three or more land in one paragraph, or when the marker claims an emphasis the sentence does not earn. Flow markers like "I first look at", "I next examine", "Turning to" are *required* between topic shifts, not tolerated |
| Passive voice | acceptable throughout methods | Acceptable where the agent is genuinely unknown. Standard method formulas ("standard errors are clustered at the state level") stay; "it is shown that" does not |

**On punctuation, never substitute mechanically.** Replacing an em-dash with a comma at the same break point produces run-ons, duplicated appositives ("a feature — the appointment of leaders — provides X" becoming "a feature provides X. That feature is the appointment of leaders"), and bureaucratic padding from over-inserted "Specifically,". Restructure instead: fold the appositive into the main clause, convert it to a relative clause, or drop it when context already carries it. The goal is prose that reads as if it never had an em-dash, not prose that visibly used to have one. After any punctuation sweep, re-read the passage. If the replacement reads worse, restore it.

## Steps

1. **Identify what to review:**
   - If `$ARGUMENTS` is a filename: read that file.
   - If `$ARGUMENTS` is a section name (e.g., "introduction"): find and read that section in `main.tex` or `paper_skeleton.tex`.
   - If no argument: ask the user which file or section to audit.

2. **Load the writing guides as FLAGGING SOURCES, not just rewrite constraints.**

   First read `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Personal.md`. It is authoritative and it reverses several defaults you would otherwise apply. In particular, **do not flag a 40-word cumulative sentence as a run-on** — that is the author's target register for body paragraphs, and short declaratives are the defect he actually complains about. Do not flag discourse or flow markers in isolation. Do not propose mechanical punctuation substitutions.

   Then read `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Academic.md` in full. Two parts of it are audit input, and they carry priority over the generic list below:
   - **§0 Stop-sign list** (50 rows) — every match is a defect, by the guide's own words. This is the author's own documented register: "near-nominal", "headline result", "a 39% lift", "well within", "dislodge", "in the spirit of", "a soft signal that", "the honest reading is", "should be read as", manager-speak verbs, precision soup, author-decision meta-sentences.
   - **§12 Appendix: common AI phrases to avoid** (45 rows).

   These are the tells this author actually produces. The generic vocabulary list in this file (delve, tapestry, realm) catches a different and largely disjoint set. **Sweep for both.** A §0 match outranks a generic match when ranking severity, because the author has already ruled on it.

   The guide also governs the rewrites (no equations in abstracts, actual numbers not "near-nominal", no boldface in running text, no bullets in body, "et al." for 3+ authors).

3. **Launch the `deslop-auditor` agent** on the content. Give it **only** the file path or the extracted passage, the target journal if known, and the one-sentence paper contract. Do **not** pass the drafting conversation, your reasoning about the passage, or any explanation of what the author was trying to do.

   A review session carrying no production history outperforms same-session self-review *and* a context-aware subagent review (Song 2026, arXiv 2603.12123: F1 28.6% vs. 24.6% vs. 23.8%; reviewing twice in the same session does not help, so the gain is context separation, not a second look). Passing your own framing along is the condition that measurably loses.

   The agent flags across the categories below, scores six dimensions, and writes hand-rewrites — while respecting the economics allow-list so legitimate academic phrasing is not flagged.

4. **Save the report** to:
   `quality_reports/[filename_without_ext]_deslop_YYYY-MM-DD.md`

5. **Present summary** to the user:
   - Overall score (out of 50) and verdict.
   - Counts by category and severity.
   - The three worst passages with their rewrites inline.
   - Path to the full report.

## What counts as an AI tell

- **House stop-sign matches (check FIRST, rank highest).** Any row from guide §0 or §12. These are the author's own ruled-on defects, so a match is never a judgment call and never belongs under "Respected". Quote the stop sign and the guide's prescribed replacement.
- **Vocabulary tells.** delve, tapestry, realm, beacon, testament to, intricate/interplay, vibrant, showcase, underscore (verb), pivotal, crucial (as filler), landscape (metaphor), embark, foster, leverage (verb where "use" fits), seamless, robust (as vague praise, not the statistical sense), navigate (metaphor).
- **Throat-clearing and emphasis crutches.** "it is important to note that", "it is worth noting", "needless to say", "at the end of the day", "in today's world", "plays a crucial/vital/pivotal role".
- **Copula avoidance.** "serves as", "stands as", "represents", "boasts", "features" where "is" or "has" is correct.
- **Superficial -ing analyses.** Trailing participles that add no content: "highlighting its importance", "underscoring the need", "reflecting broader trends", "contributing to the literature".
- **Uniform tricolons / rule-of-three abuse.** Mechanical "A, B, and C" triads, three in a row, or three parallel sentences. Two items, or one full clause, is usually better.
- **Hedging clusters.** Stacked epistemic cushions in one claim ("may potentially suggest that ... could have the ability to ..."). Simplify to ONE appropriate hedge — do not strip hedging entirely (see allow-list). **Run this check AFTER the overclaim sweep below, never before**: the two pull in opposite directions, and a hedge that the overclaim sweep marks as load-bearing is not a cluster to be thinned. Thin only genuine stacks within a single claim.
- **Overclaiming.** LLM-drafted summaries carry broad generalizations at nearly five times the human rate (Peters & Chin-Yee, *R. Soc. Open Sci.* 2025: OR 4.85, 95% CI [3.06, 7.70]), and **prompting for accuracy does not fix it** — several models still overgeneralized in 26–73% of cases. So this is a mechanical sweep, not a reminder to be careful. Three shapes, each checked against the paper's own estimation sample:
  - *Scope widening.* The subject of a claim is broader than what was estimated. An effect estimated on one Chinese province becomes a claim about developing countries. Flag every abstract, introduction, and conclusion sentence whose subject outruns the sample.
  - *Tense drift.* A past-tense finding restated as a present-tense generic ("higher water prices reduce perennial acreage" for what was "acreage fell"). The paper's own mitigation is indirect past-tense reporting.
  - *Dropped qualifier.* A conditional estimate that loses its condition between the results section and the abstract or introduction. Diff the hedges: any hedge present on a claim in Results and absent on the same claim upstream is a flag, and the fix is to restore it, not to remove the Results hedge.
- **Em-dashes in prose.** Flag **every** em-dash in running prose. The house default is zero (guide §0), not a density quota. Also flag colons and semicolons chaining clauses, which the guide caps at one per page and defaults to zero. Replace with a comma, parentheses, or two sentences.
- **Choppy additive rhythm — the author's primary complaint, and the opposite of what you would guess.** In body paragraphs, flag runs of short declaratives where each fact takes its own sentence, and especially any sentence opening by restating the previous one ("This distortion...", "The same role..."). Fold qualifications, corroborations, and consequences into subordinate clauses. The measured target from paragraphs he accepted is four to five sentences per paragraph averaging **about 40 words**, one main clause plus a subordinate chain. A rejected draft of the same content ran seven sentences averaging 21 words, which he called "awful". **Never flag a long cumulative sentence as a run-on.** Separately, flag genuine uniformity, meaning sentence lengths clustered tightly with no long-setup-then-short-verdict cadence. Flag the pattern, never the length.
- **Inflation and generic conclusions.** "a pivotal moment in the evolving landscape", "the future looks bright", "marks a turning point", significance puffery on routine results.
- **Synonym cycling and false ranges.** Rotating "households / agents / individuals / consumers" to avoid repetition; "from X to Y" pairings that span nothing meaningful.
- **Formatting tells.** Title-Case headings, bold-first bullets, "Despite these challenges..." formulas, em dashes in headings.

## RESPECT legitimate economics phrasing — do NOT flag these

Economics has its own register. The following are correct academic writing, NOT AI tells. Flag them ONLY when stacked in excessive clusters or used with no supporting result/citation.

- **Standard reporting verbs and frames.** "the paper finds", "we estimate", "we show", "we document", "the results indicate", "Table 3 reports", "column (2) shows", "the coefficient on X is", "we instrument X with Z".
- **Standard hedges (keep one per claim).** "suggests", "is consistent with", "is associated with", "we interpret this as", "may reflect", "likely". Economics requires epistemic caution; do not strip a single appropriate hedge.
- **Passive voice in methods/data.** "data were collected", "standard errors are clustered at the state level", "the sample is restricted to", "regressions are weighted by". Passive is correct and expected in methods.
- **Causal and identification language.** "identifies the causal effect", "the exclusion restriction requires", "parallel trends", "exogenous variation", "the estimand", "intent-to-treat".
- **Transitions and flow markers — these are required, not tolerated.** "In contrast", "Conversely", "Specifically", "Moreover", "Notably", "Importantly", "Crucially", "Furthermore", and especially the econ flow markers "I first look at", "I begin with", "I next examine", "Consider first", "Turning to". Prose without them reads mechanical and abrupt, dropping the reader into each new topic with no warning, which is itself an AI tell. Flag only when three or more stack in one paragraph, or when a marker claims an emphasis the sentence does not deliver. Never strip a transition without supplying another. Colloquial openers ("So,", "Now,", "Well,") are wrong register and stay flagged.
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
| Scope discipline | Do claims stay inside the estimation sample, in past tense, with their qualifiers intact? |
| Authenticity | Reads like a specific economist wrote it, or like an LLM? |

Total below 42/60: the draft needs a deslop pass before submission.

**Score the draft, do not iterate on the score.** Report the dimensions as a diagnostic checklist. Never run a revise-until-the-number-rises loop: LLM judges are unstable on long-form output, and a loop that optimizes a scalar converges on prose that games the rubric. Also **never ask whether the prose "sounds like the author"** — that judgment correlates at |r| < 0.07 with independent stylometric measures, so it is noise dressed as a verdict.

## Output Format

```markdown
# Deslop Audit: [Filename or Section]
**Date:** YYYY-MM-DD
**Score:** NN/60 — [Clean / Light pass / Needs deslop]

## Score by Dimension
| Dimension | Score (1-10) |
|-----------|--------------|
| Directness | N |
| Rhythm | N |
| Specificity | N |
| Restraint | N |
| Scope discipline | N |
| Authenticity | N |
| **Total** | **NN/60** |

## Flags by Category
| # | Category | Location ("opening words...") | Flagged text | Rewrite | Severity |
|---|----------|-------------------------------|--------------|---------|----------|
| 1 | House stop sign (§0) | Sec 4, "The effect is well within..." | "well within" | "within 2 percentage points of" | Critical |
| 2 | Overclaim — scope | Abstract, "Water pricing reduces..." | subject is "developing economies"; sample is one province | name the province | Critical |
| 3 | Vocabulary tell | Sec 1, "We delve into..." | "we delve into" | "we examine" | Major |

Severity: Critical (house stop sign, or an overclaim a referee would challenge) / Major (fix before submit) / Minor (polish).

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
5. **Rhythm over vocabulary.** Uniform sentence and paragraph length is what a referee registers first — weight low variance heavily even when the word choice is clean. Flag the uniformity, never the 15–25 word band itself.
5b. **The house list outranks the generic list.** A §0 or §12 match is a ruled-on defect and goes to Critical. A generic-LLM vocabulary match is a judgment call and rarely exceeds Major.
5c. **Overclaims are corrected by restoring scope, not by adding hedges.** Narrow the subject to the estimation sample, restore the past tense, and put back the dropped qualifier. Do not paper over a widened claim with a new "may".
6. **Quote specifics.** Every flag cites the offending text and a location by section + opening words (never line numbers).
7. **Recommend rewrite-from-scratch** when a passage trips 3+ categories and has uniform rhythm — patching individual words will not fix AI-generated structure.
8. **Do not duplicate `proofread` or `journal-fit`.** Stay in the AI-tell lane; cross-reference them for everything else.
