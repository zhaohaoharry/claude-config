---
name: lit-review
description: Structured literature search and synthesis on a topic, with multi-source search, citation traversal, relevance screening, gap identification, and BibTeX entries. Use when starting a new project or section, or when looking for related work.
argument-hint: "[topic, research question, paper title, or 'what cites X']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "WebSearch", "WebFetch", "Task"]
---

# Literature Review

Conduct a structured literature search and synthesis on the given topic.

**Input:** `$ARGUMENTS` — a topic, research question, paper title, or phenomenon.

**Core principle:** Cast a wide net across sources, then triage with an explicit rubric. Precision over volume — surface papers that actually bear on the research question, not just topically adjacent ones. Never fabricate a citation.

## Steps

1. **Parse the query** from `$ARGUMENTS`. Extract core concepts, synonyms (e.g. "minimum wage" ≈ "wage floor"; "DiD" ≈ "difference-in-differences"), method terms (IV, RD, event study, shift-share), JEL-adjacent fields, and any date/author/journal constraints. Note terms that should EXCLUDE papers (false-positive traps).

2. **Search across sources** (start local, then go wide):
   - **Project literature/** — list PDFs in the `literature/` folder; read `literature/LiteratureIndex.json` if present.
   - **Project `.bib`** — read the project's `.bib` for papers already in scope (these double as seed papers for traversal in Step 4).
   - **OpenAlex** — keyword + concept search, returns DOIs, citation counts, references, and citing-works in one API; good first wide net.
     `WebFetch` `https://api.openalex.org/works?search=QUERY&per-page=50&sort=relevance_score:desc`
   - **Semantic Scholar** — abstracts, `externalIds` (DOI/arXiv), references and citations; primary engine for Step 4 traversal.
     `WebFetch` `https://api.semanticscholar.org/graph/v1/paper/search?query=QUERY&fields=title,year,abstract,authors,externalIds,citationCount&limit=50`
   - **Google Scholar** — broadest coverage incl. grey literature; via `WebSearch` (`QUERY site:scholar.google.com` or topic query). Use for recall, not as a clean API.
   - **arXiv econ.*** — working papers in `econ.EM` (econometrics), `econ.GN` (general), `econ.TH` (theory).
     `WebFetch` `http://export.arxiv.org/api/query?search_query=cat:econ.*+AND+all:QUERY&max_results=30`
   - **NBER** — working-paper series; `WebSearch`/`WebFetch` `https://www.nber.org/papers?q=QUERY`.
   - **SSRN** — econ/finance working papers; `WebSearch` `QUERY site:papers.ssrn.com`.
   - Deduplicate across sources by DOI (fallback: arXiv ID, then normalized title + year).

   *Rate limits:* OpenAlex/Semantic Scholar free tiers throttle — batch fields in one call (`?fields=...`), use `limit/per-page` to fetch more per request, and pace requests (~500ms apart; longer if running parallel subagents — see Step 6).

3. **Triage with a relevance rubric.** Score every abstract 0-10 before reading full text:
   - **Topic/keyword match (0-3):** core concept present? synonyms?
   - **Contribution match (0-4):** does it deliver what the project needs — a result, an identification strategy, a dataset, an estimator, a theoretical mechanism — vs. background only?
   - **Specificity (0-3):** primary research on the exact question (3), method/measurement paper (2), broad review (1). Apply exclusion terms: if a trap term dominates, score 0.

   | Score | Meaning | Action |
   |-------|---------|--------|
   | 0-4 | Not relevant | Note one-line reason, skip |
   | 5-6 | Possibly relevant | Park in a "watch" list, no deep read yet |
   | 7-8 | Relevant | Read full text, extract finding/method, include |
   | 9-10 | Seminal / core | Read, extract, and traverse its citations (Step 4) |

   For ambiguous topics, calibrate first: score 5-10 candidate abstracts, show the user the predicted vs. expected calls, and adjust weights/exclusion terms before bulk screening. Report progress as you go — never screen silently.

4. **Traverse citations from seed papers** (every paper scoring ≥7, especially ≥9):
   - **Backward (references):** what the seed cites — anchors the seminal/foundational work.
     `WebFetch` `https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}/references?fields=title,year,abstract,externalIds,contexts,intents&limit=100`
   - **Forward (citing works):** newer papers that build on, replicate, or challenge the seed — catches the recent frontier OpenAlex/Scholar keyword search may miss.
     `WebFetch` `https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}/citations?fields=title,year,abstract,externalIds&limit=100`
   - Re-score each discovered paper with the Step 3 rubric; only queue those scoring ≥5. Use citation `contexts`/`intents` (methodology vs. background) as a relevance signal.
   - **Limit the blast radius:** traverse only from ≥7 seeds, follow at most 2 levels deep, dedupe against everything already seen, and pause to confirm with the user past ~50 papers. Forward-from a recent, highly cited paper is usually the highest-yield single move.

5. **Organize and synthesize.** Sort surviving papers by relevance, then group into:
   - **Theoretical contributions** — models, mechanisms, frameworks.
   - **Empirical findings** — key results, effect sizes, data sources, identification strategies.
   - **Methodological innovations** — new estimators, identification designs, inference methods.
   - **Open debates** — where findings conflict or remain unresolved.

   Then identify gaps: unanswered questions, conflicting findings, and data/methods that could resolve them.

6. **(Optional) Parallel subagent screening for large pools.** When the candidate pool is large (>50 abstracts) and screening is the bottleneck, dispatch the work via the `Task` tool:
   - Split the candidate list into batches of ~15-25 papers with NO overlap.
   - Dispatch subagents in a single message (parallel), 5-10 at most. Give each the SAME rubric (Step 3) and ask it to return JSON only — `{paper_id, doi, score, status, one_line_reason}` — and to update no shared files.
   - Consolidate the returned JSON yourself: dedupe by DOI, sort by score, sanity-check that batches have comparable hit rates (a wildly off batch signals inconsistent scoring — re-screen it).
   - Skip subagents for small pools (<20) — manual screening is faster and the overhead is not worth it.

7. **Extract BibTeX** for every paper you include in the report. Use the DOI/arXiv metadata captured during search — do not hand-type fields from memory. Mark anything you could not verify with `[VERIFY: ...]`.

8. **Save report** to `quality_reports/lit_review_[sanitized_topic]_YYYY-MM-DD.md`.

9. **Validate the BibTeX.** Recommend the user run `/bib-validate` on the extracted entries (or the project `.bib` after they paste them in) to catch hallucinated DOIs, wrong years, mismatched author lists, and malformed entries before anything is cited. State this explicitly in the closing summary.

## Output Format

```markdown
# Literature Review: [Topic]
**Date:** YYYY-MM-DD
**Sources searched:** [literature/ folder, project .bib, OpenAlex, Semantic Scholar, Google Scholar, arXiv econ.*, NBER, SSRN]
**Papers screened / included:** [N screened, M included]

## Summary
[2-3 paragraph overview of the state of the literature]

## Key Papers

### [Author (Year)] — [Short Title]
- **Main contribution:** [1-2 sentences]
- **Method:** [Identification strategy / data]
- **Key finding:** [Result with effect size if available]
- **Relevance to our project:** [Why it matters]
- **Source / score:** [e.g. Semantic Scholar, score 9; forward-cited from Card-Krueger]

[5-15 papers, ordered by relevance]

## Thematic Organization

### Theoretical Contributions
### Empirical Findings
### Methodological Innovations
### Open Debates

## Gaps and Opportunities
1. [Gap 1]
2. [Gap 2]

## Suggested Next Steps
- [Papers to read, data to obtain, methods to consider]

## BibTeX Entries
[BibTeX for all papers mentioned]

## Validation
Run `/bib-validate` on the entries above before citing — checks DOIs, years, and author lists against source metadata.
```

## Important
- Never fabricate citations. If unsure of a paper's details, flag it: "[VERIFY: ...]" — never invent a DOI, year, or author to fill a gap.
- Distinguish working papers from published versions (NBER/SSRN/arXiv preprints often have a later journal version — prefer and note the published one).
- Prioritize recent work (last 5-10 years), but always include seminal older papers that the field still cites.
- Triage before reading: score abstracts with the rubric first; only deep-read papers scoring ≥7.
- Always traverse forward citations from at least the top seed paper — keyword search alone misses the recent frontier.
- Dedupe by DOI across every source before reporting; a paper from OpenAlex, Scholar, and the project `.bib` is one paper.
- Always end by recommending `/bib-validate` on the extracted BibTeX.
