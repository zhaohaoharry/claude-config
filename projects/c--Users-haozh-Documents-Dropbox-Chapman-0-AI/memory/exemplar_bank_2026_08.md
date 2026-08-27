---
name: exemplar-bank-2026-08
description: Zotero-backed literature index and the section-indexed top-5 exemplar bank that conditions prose generation (built 2026-08-25)
metadata: 
  node_type: memory
  type: project
  originSessionId: 02cf2403-b5af-47c6-a3c7-8492bfbb29e7
  modified: 2026-08-25T13:52:35.958Z
---

The writing setup now conditions generation on real top-5 applied prose instead of only filtering
finished text. Built 2026-08-25.

**Zotero is the corpus, not the `literature/` folders.** `C:\Users\haozh\Zotero` holds 1,122
journal articles with curated metadata and 1,405 stored PDFs, against 416 scattered PDFs in the
project folders. `Claude Master\tools\index_zotero.py` reads a copy of `zotero.sqlite` directly
(Zotero locks the live file) and needs no network, because the library already carries a
hand-checked title, journal, year, DOI, and author list. It yields **83 top-5 papers from 2018 on**
where the folder-only pass yielded 13.

**Roughly a third of top-5 papers are the wrong model.** Of 91 top-5 papers with a PDF on disk, 36
are theory or econometric-methods papers. `extract_exemplars.py` excludes them by counting
`Proposition|Lemma|Theorem` occurrences and by title, and reports the exclusions rather than
quietly shrinking the corpus.

**Section headings do not locate sections.** Top-5 papers name sections substantively — "Empirical
Step 1: Railroads and Trade Costs", not "Results" — so a heading search finds a Results section in
under half of them. The extractor falls back to searching everything after the introduction.

**The measured numbers.** 34 curated passages from 21 applied papers: **24.9 words per sentence in
paragraphs of 6.5 sentences**. Abstracts run near 22, with the best applied ones at 12 to 20. This
sits against the 40-word cumulative target in [[feedback_cumulative_sentences_and_verbs]], which
was measured on the author's own accepted paragraphs. Both were left standing in
`AI_Writing_Guide_Personal.md` §1.2 with the conflict flagged; **the author has not yet ruled on
it.** What is settled either way: 40 words is not what top-5 papers do, and the subordination rule
(never open a sentence by restating the previous one) is independent of word count.

**Where it is wired in.** `econ-craft` step 3b and `econ-introduction` step 6 both require reading
the matching section of `Claude Master\econ_exemplars_modern\README.md` *before* composing, and the
`econ-craft-reminder` hook injects the same instruction. The reason is in the skill text: every
other writing tool here runs on text that already exists, and filtering machine prose yields
de-slopped machine prose.

**Rebuild:** `index_zotero.py --merge-master` → `extract_exemplars.py` → `build_exemplar_bank.py`.
The curation (which passages, and the "mechanic" note on each) lives in `SELECTION` inside
`build_exemplar_bank.py`; passages are pulled from `_candidates.json` at build time so they cannot
drift from the source PDFs.

**Copyright:** `econ_exemplars_modern\` holds verbatim published passages for personal style study.
Keep it local; never push it to a public repository. See also [[econ_craft_system]] and
[[research_data_repository]].
