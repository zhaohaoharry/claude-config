---
name: cite-verify
description: Check whether each citation in a manuscript actually supports the claim it is attached to — the finding, number, method or fact the sentence attributes to the cited paper. Reads the source in the user's Zotero library first (abstract, then the PDF pages), falls back to CrossRef, OpenAlex and Semantic Scholar, and returns a verdict per claim (SUPPORTED, PARTIAL, MISMATCH, UNCERTAIN, UNVERIFIABLE) with the passage that decides it and a minimal fix. Use before submission, after AI-assisted drafting of an introduction or literature section, or when asked "do my citations support what I wrote". Not for checking that references exist or that their metadata is right (that is bib-validate), and not for finding new literature (that is lit-review).
argument-hint: "[path to .tex or .md] [--bib path] [--section intro|lit|all]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "WebFetch", "WebSearch", "Agent"]
---

# cite-verify — does the cited paper say what the sentence says it says?

Adapted from `lit-review-verify` in amatray/claude-skills-public (MIT), rebuilt on the user's
Zotero library and the public scholarly APIs instead of a private lookup server.

## Steps

1. **Extract claim-citation pairs.** Read the manuscript (follow `\input`/`\include`). For every
   sentence with `\cite`, `\citet`, `\citep` or a variant (or an inline "Author (Year)" in
   Markdown), record the claim text, the cite keys, and the section and opening words of the
   paragraph (never a line number in the report). Skip bare "see also" lists, data-source
   acknowledgements and self-citations. Classify each pair:
   - **FINDING** — attributes a result, sign or magnitude to the paper: strict.
   - **FACTUAL** — a fact or statistic sourced to the paper: medium; the number must appear in the
     source or follow from it directly.
   - **METHOD** — the paper is cited for an estimator, design or data construction: lenient; flag
     only a clear mismatch.
   - **GENERAL** — a pointer to a literature: lenient; flag only if the paper is off-topic.
   Do not stop for review after extraction; run the whole pipeline.

2. **Resolve each cite key.** Read the `.bib` entry (title, authors, year, DOI). Look the paper up
   in Zotero first with `tools/zotero_lookup.py` (`--doi`, then `--title`, then `--author` with
   `--year`; run with `python -I`). It copies `zotero.sqlite` and its WAL file before querying and
   returns the abstract, PDF paths and the Better BibTeX cite key. Only for papers not in Zotero:
   CrossRef (`https://api.crossref.org/works/<DOI>` or `?query.bibliographic=`), then Semantic
   Scholar (`https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>?fields=title,abstract,year`),
   then OpenAlex (`https://api.openalex.org/works/doi:<doi>`, abstract in `abstract_inverted_index`).

3. **Verify against the abstract.** Assign a verdict per pair:
   | Verdict | Meaning |
   |---|---|
   | SUPPORTED | the source states what the sentence attributes to it |
   | PARTIAL | related, but the sentence overstates, understates, shifts the population or setting, or turns a correlation into a cause |
   | MISMATCH | the source contradicts the sentence or is about something else |
   | UNCERTAIN | the abstract cannot settle it |
   | UNVERIFIABLE | no text of the source could be retrieved |
   Prefer UNCERTAIN to MISMATCH when only the abstract was read; abstracts omit most results.

4. **Read the PDF for every PARTIAL and UNCERTAIN pair, and for every FINDING or FACTUAL pair that
   quotes a number.** Extract text with PyMuPDF (`py -3.12`, `import pymupdf`): the abstract and
   introduction pages first, then the table or section the claim points to. For many pairs,
   dispatch subagents in parallel (up to five at once), each given only the claim, the citation
   metadata and the PDF path, returning a verdict with the page number and the quoted passage.
   A verdict that changes after the PDF read records the page.

5. **Suggest the minimal fix** for each PARTIAL and MISMATCH: soften or correct the sentence to
   what the source says (smallest span that changed, in the user's own wording), or point to the
   right paper when the Zotero library or a quick OpenAlex search shows an obviously better
   source. Never add a cite key to the `.bib` and never insert a new citation into the manuscript
   unless the user explicitly asks; list the candidate instead.

6. **Report.** Save `quality_reports/cite_verify_YYYY-MM-DD.md` and show the user only the
   problems: a summary count by verdict, then one numbered item per PARTIAL, MISMATCH, UNCERTAIN
   and UNVERIFIABLE pair with location (section and paragraph opening words), the claim, the cited
   paper, the deciding passage with its page, and the suggested fix. State which APIs were
   unreachable. Do not list SUPPORTED pairs.

7. **Apply on request.** When the user says "apply 2 and 5", edit the manuscript with the
   track-changes macros (`~/.claude/rules/manuscript-track-changes.md`), minimal span, and
   recompile.

## Important

- Every verdict rests on text actually retrieved. Never infer what a paper says from its title or
  from memory; the user's rule is that sources, not memory, back every claim.
- Query Zotero only through a copy of the database plus its WAL file; never open the live file.
- A citation that is right for a different claim in the same sentence is still flagged, with the
  clause it fits.
- Cross-reference: metadata and existence go to `bib-validate`; a referee-level read of the
  literature positioning goes to `review-paper`.
