---
name: review-paper
description: Comprehensive top-5 journal referee review of an economics manuscript. Covers identification, econometrics, theory, citations, and internal consistency. Use before submitting or for coauthor feedback. Pass 'panel' for an independent multi-referee panel plus editor synthesis.
argument-hint: "[paper filename, e.g. 'main.tex' or path to PDF] [panel]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Task"]
---

# Manuscript Review

Produce a thorough referee report for an economics manuscript — the kind a top-5 journal (AER, QJE, JPE, ReStud, Econometrica) would send back.

**Input:** `$ARGUMENTS` — path to main.tex, a PDF, or a folder containing the paper. If `$ARGUMENTS` contains the word `panel`, run **Panel mode** (see below); otherwise run the default single-report flow.

## Steps (default — single integrated report)

1. **Locate and read the manuscript:**
   - Direct path from `$ARGUMENTS`
   - Or look for `main.tex` in the GitHub repo subfolder
   - For PDFs: read in chunks (5 pages at a time for long papers)

2. **Read supporting files if available:**
   - `reference.bib` — check for missing or malformed citations
   - `literature/LiteratureIndex.json` — if it exists, use it to verify citation accuracy
   - Any appendix `.tex` files

3. **Launch the econ-reviewer agent** to evaluate across 5 dimensions:
   - Identification strategy
   - Econometric specification
   - Theory (if applicable)
   - Citation fidelity
   - Internal consistency

4. **Generate 3-5 simulated referee questions** — the tough questions a top referee would ask.

5. **Save the full report** to:
   `quality_reports/paper_review_YYYY-MM-DD.md`

6. **Present summary** to user:
   - Overall recommendation
   - Top 3 most important concerns
   - Path to full report

## Panel mode (when `$ARGUMENTS` contains `panel`)

Convene an independent referee panel: each referee reviews in **isolation** under a distinct lens, then an editor pass synthesizes the verdicts. This surfaces disagreement that a single integrated report hides.

1. **Locate and read the manuscript** (same as default step 1) and **read supporting files** (same as default step 2).

2. **Launch 2-3 econ-reviewer agents in parallel**, each in isolation (no agent sees another's report). Give each a distinct referee persona and lens by prepending its mandate to the agent prompt:
   - **(a) Identification hawk** — fixated on the causal claim: identifying assumptions, threats (OVB, reverse causality, selection, SUTVA), instrument relevance/exogeneity, parallel trends, the estimand vs. what is claimed.
   - **(b) External-validity & magnitude skeptic** — accepts internal validity for argument's sake and attacks generalizability, mechanism, and whether effect sizes are economically meaningful (not merely significant), and whether the headline number survives sensible benchmarking.
   - **(c) Theory / measurement & literature referee** — model-to-data mapping, measurement and variable construction, derivation correctness, citation fidelity, and missing related work a referee would flag.
   - Use only (a) and (b) for a short empirical note; add (c) for a full paper or any paper with a model.
   - Each agent uses the standard econ-reviewer Report Format and rates its dimensions 1-5. Reports are independent and may conflict — do not harmonize them.

3. **Editor synthesis pass** — read all referee reports and write a prioritized editor report. Do NOT average the referees; adjudicate. For each major issue, label it **CONSENSUS** (raised or implied by multiple referees) or **DISAGREEMENT** (referees split, or one flags what another dismisses), and take an editorial position on each disagreement. Where referees conflict, re-read the relevant section of the paper to decide who is right. Issue a **single** recommendation (Strong Accept / Accept / R&R / Reject) that is the editor's, not a vote tally.

4. **Save the panel report** to:
   `quality_reports/paper_review_panel_YYYY-MM-DD.md`

5. **Present summary** to user:
   - Single editorial recommendation
   - The 3 highest-priority required changes
   - One line on the sharpest CONSENSUS issue and the sharpest DISAGREEMENT
   - Path to full report

## Panel Output Format

```markdown
# Manuscript Review — Panel: [Paper Title]
**Date:** YYYY-MM-DD
**Standard:** Top-5 journal referee panel
**Referees:** (a) Identification hawk · (b) External-validity skeptic · (c) Theory/measurement [if used]

## Editor Synthesis
**Recommendation:** Strong Accept / Accept / R&R / Reject
[2-3 paragraph adjudication: what the panel agrees on, where it splits, the editor's call.]

### Prioritized Required Changes
1. [Highest-priority change] — CONSENSUS / DISAGREEMENT
2. ...

### Consensus
- [Issue all/most referees converge on, with the editor's weight on it.]

### Disagreement
- **[Issue]** — Referee X says ...; Referee Y says ...; **Editor:** [position + why].

## Individual Referee Reports
### Referee (a) — Identification hawk
[Full econ-reviewer report, verbatim.]

### Referee (b) — External-validity & magnitude skeptic
[Full econ-reviewer report, verbatim.]

### Referee (c) — Theory / measurement & literature  [if used]
[Full econ-reviewer report, verbatim.]

## Dimension Ratings (by referee)
| Dimension | (a) | (b) | (c) | Editor |
|-----------|-----|-----|-----|--------|
| Identification | N | N | N | N |
| Econometrics | N | N | N | N |
| Theory | N | N | N | N |
| Literature | N | N | N | N |
| Internal Consistency | N | N | N | N |
| **Overall** | **N** | **N** | **N** | **N** |
```

## Important

- **Default is unchanged.** With no `panel` argument, produce the single integrated report exactly as before (steps 1-6).
- **Referees review in isolation.** In Panel mode, launch the agents in parallel and never let one referee's report reach another. Independence is the point.
- **Distinct lenses, not duplicates.** Each persona attacks a different failure mode. A panel of three near-identical reports is a failed panel.
- **Editor adjudicates, not averages.** The recommendation is the editor's judgment; resolve every DISAGREEMENT with a stated position, re-reading the paper where needed.
- **Never fabricate.** If a claim needs code or data to verify, say so — for every referee and the editor.
- **Be specific.** Reference exact sections, equations, tables, and page numbers; check page/table numbers against the compiled PDF, not the source.
- **Cross-reference:** to draft the point-by-point response to this review, use `/aer-rebuttal`; to assess whether the target journal is the right home, use `/journal-fit`.
