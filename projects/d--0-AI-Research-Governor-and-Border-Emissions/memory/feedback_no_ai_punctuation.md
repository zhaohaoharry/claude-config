---
name: feedback-no-ai-punctuation
description: User-wide writing rules across all academic papers — minimize em-dashes/semicolons/colons (AI tells), and use American spelling (neighbor, summarize, minimize).
metadata:
  type: feedback
---

## Spelling: American (default for all papers)

The user prefers **American spelling** across all papers: `neighbor` (not neighbour), `summarize` (not summarise), `minimize` (not minimise), `characterize` (not characterise), `behavior` (not behaviour), `analyze` (not analyse), `favor` (not favour), `organize` (not organise), `recognize` (not recognise). When sweeping a manuscript for spelling consistency, unify on American.

## Punctuation: minimize em-dashes, semicolons, colons

In academic writing across all the user's papers, minimize use of em-dashes (`---`), semicolons (`;`), and colons (`:`). These three punctuation marks are characteristic of AI-style prose when overused. Default to commas, periods, or "and" instead.

**Why:** The user identified these as a writing tell of AI-assisted drafting and wants their manuscripts to read more naturally. They explicitly stated: "this is the rule of writing for all papers."

**How to apply:**
- **Em-dashes (`---`):** Keep only when a parenthetical contains commas internally so commas around it would be ambiguous, or for a single strong rhetorical contrast. Otherwise convert to commas (for parentheticals) or periods (for an attached extension).
- **Semicolons (`;`):** Keep only when joining two short, tightly coupled independent clauses where a period would feel jarringly choppy. Default to a period and two sentences.
- **Colons (`:`):** Keep only when introducing a vertical list, a formal block, or a single defined term that follows the colon. Avoid using colons to attach a follow-up sentence or explanation — use a period instead.
- A reasonable target ratio is ~15-25% KEEP, ~75-85% REPLACE when sweeping a manuscript.
- When applying changes with track-changes markup, use `\del{old}\add{new}` *outside* existing `\add{}` blocks; for punctuation inside existing `\add{}` blocks, modify inline (the surrounding `\add` already marks the change as added).

**CRITICAL: preserve flow after the substitution.** A bare period-replacement often kills transition or rhetorical setup. For each REPLACE, check the result in context:
- A colon introducing a question or quotation has setup work — replacing with a period leaves the next sentence hanging. Either keep the colon, OR add a transition phrase ("Specifically,", "That is,", "In particular,", "Concretely,", "Namely,").
- A semicolon joining two closely-coupled clauses signals tight logical connection — bare-period replacement may make the connection invisible. Add a connector ("Moreover,", "In turn,", "As a result,") OR restore the semicolon if the connection genuinely needs to be tight.
- An em-dash introducing emphasis or contrast often needs a connector word ("In fact,", "Indeed,") to preserve the rhetorical force.
- After every sweep, re-read the affected passages to confirm the prose still reads naturally. If a replacement reads worse than the original, restore or smooth — don't leave it.

**Watch for resulting long sentences.** When an em-dash becomes a comma, the sentence can pick up three or four comma-separated clauses and become hard to parse. When a semicolon becomes a comma, the result can be a run-on. After substitution:
- Count clauses. If the sentence now has 3+ clauses separated by commas, or covers more than one main idea, **split it into two sentences**.
- A natural breakpoint is often where the original em-dash/semicolon was — drop the dash, replace with a period, and start the next sentence with a brief connector ("This", "These", "Such", "In turn,", "The result is that...").
- Prefer two short clear sentences over one long correct one. Readability beats compactness in academic prose.

**CRITICAL: Don't mechanically replace — REWRITE thoughtfully.** Dropping punctuation can damage prose if you just substitute commas/periods at the original break point. Common mistakes:
- **Splitting at the em-dash repeats content.** If the em-dash sets off an appositive that defines a noun, splitting like "X is Y. That Y is X-defined" creates duplicate phrasing (e.g., "a unique feature... — the appointment of leaders — provides..." → "...a unique feature provides... That feature is the appointment of leaders." — "feature" appears twice and the definition is recycled).
- **Awkward transitions.** "The result is that...", "That feature is...", "This X is..." sentences feel mechanical when overused.
- **Wordy padding.** Adding "Specifically," or "In particular," everywhere makes the prose sound bureaucratic.
For each potential punctuation replacement, ASK: would a *thoughtful human writer* phrase this without the punctuation? Common alternative moves:
  - **Restructure the appositive into the main clause.** Instead of "X — the Y feature — produces Z", try "Y produces Z" (lead with the feature) or "Z follows from the Y feature of X" (lead with the result) or "X's Y feature produces Z" (genitive/possessive).
  - **Convert appositive to relative clause.** "X — which has Y — does Z" → "X, which has Y, does Z".
  - **Drop redundant content.** If a definition is already clear from context, just remove the appositive.
  - **Use commas** when the appositive is short and reads cleanly.
The goal is prose that reads as if it never had an em-dash, not prose that visibly used to have one. **Quality and naturalness beat strict adherence to the no-punctuation rule.**

**Related:** [[feedback-track-changes-markup]] (not yet written — covers the `\del`/`\add` workflow and the `\hl`-vs-`\sout` nesting pitfalls).
