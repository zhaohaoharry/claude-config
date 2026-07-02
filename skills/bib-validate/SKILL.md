---
name: bib-validate
description: Verify each entry in a .bib file or reference list against CrossRef, OpenAlex, and Semantic Scholar, flagging hallucinated, chimeric, and incorrect citations. Use before submission, after drafting a bibliography with AI assistance, or when checking that every reference actually exists. Checks whether references EXIST and metadata is correct, not whether the paper characterizes them accurately (that is review-paper).
argument-hint: "[path to .bib file or reference list]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "WebSearch", "WebFetch"]
---

# Bibliography Validation

Verify that every reference in a `.bib` file (or a pasted reference list) corresponds to a real publication, and check its metadata against authoritative scholarly databases. Produce a status table and offer corrected BibTeX. **Does NOT edit the source `.bib` file unless the user explicitly asks.**

**Input:** `$ARGUMENTS` — a path to a `.bib` file. If a `.tex` file is given, read it and follow `\bibliography{}` / `\addbibresource{}` to the `.bib`. If no argument, ask the user for the file (or accept a pasted reference list).

## Steps

1. **Parse the bibliography.** Extract every entry. For each, capture: cite key, entry type, `title`, `author` (tokenize on `and`, keep surnames), `year`, `journal`/`booktitle` (venue), and `doi` if present. For a pasted list, parse each line/block into the same fields as best you can. Number the entries so the report and the source line up.

2. **Verify each entry against three sources.** Query in this order and stop early once a confident match is found, but record which sources were checked:
   - **CrossRef** — `WebFetch https://api.crossref.org/works?query.bibliographic=<title author year>&rows=3` (or resolve a stated DOI directly: `https://api.crossref.org/works/<DOI>`).
   - **OpenAlex** — `WebFetch https://api.openalex.org/works?search=<title>` (or `https://api.openalex.org/works/doi:<DOI>`).
   - **Semantic Scholar** — `WebFetch https://api.semanticscholar.org/graph/v1/paper/search?query=<title>&fields=title,authors,year,venue,externalIds`.
   - Fall back to `WebSearch` for the title in quotes plus first author when an API returns nothing, to confirm whether the work exists anywhere (publisher page, arXiv, repository).

3. **Compare metadata field by field** against the best match. For the top result, score:
   - **Title** — agreement (close paraphrase counts as match; reordered words OK; a different paper is a mismatch).
   - **First-author surname** — match against the database record.
   - **Year** — exact, or off by ±1 (preprint vs. published).
   - **Venue** — journal/booktitle agreement (allow arXiv→journal upgrades).
   - **DOI** — if the entry has one, confirm it resolves to *this* record, not an adjacent paper.

4. **Classify each entry** using the matrix below. Apply judgment; do not force a weak match to fill a cell, and budget at most one reworded query per entry before recording the verdict.

   | Title | First author | Verdict |
   |-------|-------------|---------|
   | match | match | **VERIFIED** (year/venue diffs noted as MISMATCH details) |
   | match | mismatch | **CHIMERIC** — real title glued to wrong authors |
   | mismatch | match | **CHIMERIC** — real authors attached to an invented title |
   | mismatch | mismatch | **CHIMERIC or severely miscited** |
   | no usable result in any source | — | **HALLUCINATED** — plausible structure, no real publication |
   | match + match, but year/venue/DOI wrong | | **INCORRECT** — real work, bad metadata |

   - **VERIFIED** — confirmed in ≥1 source with title and first author matching, no decisive conflict.
   - **MISMATCH / INCORRECT** — the work exists but one or more fields (year, venue, DOI, author list) are wrong.
   - **CHIMERIC** — internally plausible but stitched together: right title + wrong authors, or right authors + invented title. Common in AI-drafted bibliographies.
   - **HALLUCINATED / NOT-FOUND** — no real publication matches; the entry appears fabricated.
   - **UNVERIFIABLE** — `@misc`, `@unpublished`, theses, or works with legitimately patchy coverage; mark explicitly rather than guessing.

5. **Surface the headline.** If a large share of entries (>10%) flag as HALLUCINATED or CHIMERIC, lead the report with a one-line warning (e.g., "7 of 51 entries are hallucinated or chimeric — review before submission").

6. **Offer corrected BibTeX (optional).** For INCORRECT and CHIMERIC entries where a confident match was found, prepare a corrected entry — **keep the user's original cite key**, fix only the metadata around it. Present these for confirmation; do not write to the `.bib` unless the user says so.

## Output Format

```markdown
# Bibliography Validation Report
**File:** [path]    **Date:** YYYY-MM-DD    **Entries:** [N]

[One-line warning here if >10% are hallucinated/chimeric.]

## Summary
| Status | Count |
|--------|-------|
| Verified | 0 |
| Mismatch / Incorrect | 0 |
| Chimeric | 0 |
| Hallucinated / Not found | 0 |
| Unverifiable | 0 |

## Per-Entry Status
| # | Cite key | Status | Sources checked | Issue |
|---|----------|--------|-----------------|-------|
| 1 | smith2020 | VERIFIED | CrossRef, OpenAlex | — |
| 2 | jones2019 | INCORRECT | CrossRef | year 2018→2019; venue wrong |
| 3 | lee2021 | CHIMERIC | CrossRef, OpenAlex, S2 | title real, authors do not match |
| 4 | doe2022 | HALLUCINATED | all three + web | no matching publication found |
| 5 | wp2023 | UNVERIFIABLE | — | working paper, no index coverage |

## Details
For each non-verified entry: the claimed metadata, the best database match (with the URL queried and the matched title/authors/year/DOI), and what conflicts.

## Suggested Corrections (optional)
[Corrected BibTeX for INCORRECT/CHIMERIC entries, original cite keys preserved. Offers only — not applied.]
```

## Important
- Never invent evidence. Every CHIMERIC / HALLUCINATED / INCORRECT verdict must cite at least one URL actually queried plus the matched (or absent) record. If a source is unreachable (timeout, 404, rate limit), record that and lean toward UNVERIFIABLE — never treat a failed fetch as proof of fabrication.
- A DOI that does not resolve is suspicious but not conclusive on its own — confirm via title/author search before calling an entry HALLUCINATED.
- Preserve the user's cite keys. They are canonical; correct the metadata around a key, never rename it to a "standard" format.
- Distinguish off-by-one years (preprint vs. published) from genuinely wrong years — the former is at most a MISMATCH note.
- `@misc`, `@unpublished`, theses, and working papers often have no database coverage. Mark these UNVERIFIABLE rather than HALLUCINATED unless a positive red flag is present.
- Process API/web fetches in small batches to avoid rate limiting.
- Do not edit the `.bib` file or add corrections without explicit user confirmation.
