---
name: No trailing period in \paragraph{...} arguments
description: Never end a \paragraph heading argument with a period. The titleformat for \paragraph in this user's papers auto-appends a period; an internal period creates a double-period in the rendered PDF. Applies to all research projects under 0.AI/Research/.
type: feedback
originSessionId: 78ced47c-e9ad-4b4d-84b1-a497ab260cb9
---
In LaTeX manuscripts where the project uses a custom `\titleformat{\paragraph}` with a trailing punctuation specifier (the `[.]` after-code), the period is appended automatically. Writing `\paragraph{Foo bar.}` then renders as "Foo bar.." with a double period.

**Rule:** never include a trailing period inside `\paragraph{...}`. Examples:

- Correct: `\paragraph{Fact 2: Plot-level crop choices are highly persistent}`
- Wrong:   `\paragraph{Fact 2: Plot-level crop choices are highly persistent.}`

**Why:** The user noticed and flagged this on 2026-05-08 in `paper_revision.tex` Section 6 Fact 2. The double period had also escaped into many other paragraph headings throughout the paper (31 occurrences in paper_revision.tex, 32 in paper_publication.tex, 8 in paper_skeleton.tex). It is a presentation defect that signals the prose has not been carefully proofed.

**How to apply (strict — the user has flagged this twice; do not let it slip again):**

1. *Before writing any new `\paragraph{...}` heading:* compose the heading without a terminal period. Treat the period rule as part of the syntax of the command, not an optional polish item.

2. *After any session that adds new `\paragraph` headings (or any LaTeX edit at all):* run the project's brace-counting fixer script before reporting completion to the user. For Water and Crop: `python program/sandbox/fix_paragraph_periods.py`. The script handles nested-brace cases (math content like `$\mathcal{M}^{\text{base}}$`) that a naive regex cannot. If the project does not have such a fixer, run a brace-counting Python sweep before declaring done.

3. *When recompiling to verify a final draft:* visually scan the rendered PDF for any "..": this is the failure mode the rule prevents.

The rule applies to `\subparagraph` and any other run-in heading defined with the `[.]` after-code in the project's `paper.sty` or equivalent style file. Verify the project's style file once at session start: if `\titleformat{\paragraph}` ends with `[.]`, the rule is binding; if it ends with `[]` or has no after-code, the rule is moot.

Do *not* preemptively rewrite all paragraph headings in unfamiliar codebases — verify the project's style file first. Across the user's research projects (`0.AI/Research/Water and Crop/`, `0.AI/Research/ESG Green Premium/`, `0.AI/Research/Social Capital/`), the convention is the same.

**Failure mode that triggers re-flagging:** writing `\paragraph{Baseline institution $\mathcal{M}^{\text{base}}$.}` because the closing-brace nested-math pattern made the trailing period invisible during composition. The fixer script's brace-counting parser is the safety net; running it is the rule, not an optional check.
