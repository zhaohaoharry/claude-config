---
name: feedback-verify-references
description: Always verify reference/citation information online (Google Scholar, journal homepage, author CV) before updating bibtex entries — even when the user provides the new info verbatim.
metadata:
  type: feedback
---

When updating any reference (bibtex entry, citation key, title, author list, venue, year, volume, issue, pages, DOI), **verify online before applying the change**, even if the user provides the new information verbatim.

**Why:** Users may have second-hand or outdated information. Trusting verbatim has caused at least one near-miss already (Liu-Lu-Peng-Wang paper title and venue). The user explicitly said: "I need you to be very careful about references. when I offer you new information, you should double check online before applying the changes."

**How to apply:**
- Before any reference edit, run a WebSearch with quoted exact-match author names + a distinctive title word: `"Author1" "Author2" "DistinctiveTitleWord" journal`.
- Cross-check with at least one author homepage or CV when possible (Google Scholar, university faculty page).
- For "forthcoming" claims, look at the journal's accepted-papers list or the author's most recent CV (university page often has the latest).
- If the user's info conflicts with the web evidence, flag the discrepancy back to the user before editing.
- Document the verification in the response: "Confirmed via [source X] and [source Y]."

**Scope:** All papers under `Research/`. Also applies to coauthor name spellings, page numbers, and DOIs.

**Related:** [[feedback-no-ai-punctuation]] (writing rule).
