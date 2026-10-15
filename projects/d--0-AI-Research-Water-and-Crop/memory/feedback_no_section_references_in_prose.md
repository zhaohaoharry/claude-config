---
name: feedback-no-section-references-in-prose
description: "Bare parenthetical cross-references are bad — INCLUDING object refs (Figure X)/(Table Y), not just (Section/Appendix). Write the ref into the sentence; prefer 'as Figure X shows' at first reference; use '(see X)' only if a parenthetical is unavoidable"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6de2f577-1ca3-423f-8df3-7772a79528ba
---

The global rule lives at `~/.claude/rules/cross-references.md`. Summary:

- **Natural-sentence cross-refs are fine.** *"Appendix X documents the conventions"* / *"described in Section Y"* / *"Section Z reports the estimates"* — all normal academic prose. Keep them.
- **Bare parenthetical cross-refs are not fine.** Do not write `(Appendix X)` or `(Section Y)` as a standalone tag inside a sentence.
- **If a parenthetical is needed, write it out:** `(see Appendix X for details)`, not the bare `(Appendix X)`.
- **Object refs are NOT exempt** (user re-clarified 2026-06-16, with irritation). A bare `(Figure~\ref{fig:X})` / `(Table~\ref{tab:Y})` is also bad. Write it into the sentence (`Figure~\ref{fig:X} shows...`), prefer `as Figure~\ref{fig:X} demonstrates/illustrates/shows` at the FIRST reference, and use `(see Figure~\ref{fig:X})` only if a parenthetical is unavoidable.
- **External bibliographic refs** (DWR Bulletin 132, Hanak et al. 2019 Table 3) are not internal navigation — fine in any form.

## History on this project

- Original feedback was triggered by "(Section~\ref{sec:sensitivity})" in §7.3 autarky paragraph (2026-06-04).
- Initial rule (mine) was too broad — I dropped natural-sentence appendix refs across the manuscript on 2026-06-05.
- User clarified the same day: only bare parentheticals are bad; natural-sentence refs are fine and often necessary.
- Restored the natural-sentence refs; kept the bare-parenthetical drops; promoted the rule to global.

Applies across all research projects via `~/.claude/rules/cross-references.md`.
