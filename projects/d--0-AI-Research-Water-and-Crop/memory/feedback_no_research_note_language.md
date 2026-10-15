---
name: No research-note language in manuscript prose
description: In paper prose, describe the substance directly. Avoid sentences that reflect the author's reasoning, methodological decisions, name an argument's standard label, or comment on what the writing is doing. Applies across all research projects.
type: feedback
originSessionId: 6de2f577-1ca3-423f-8df3-7772a79528ba
---
The manuscript should read as a published paper, not as research notes. Sentences that reflect researcher decisions, justify methodology choices, label an argument's standard name, or telegraph the structure of the writing are out of register. State the content directly and let the substance speak for itself.

**Disallowed patterns:**

- "I devote the remainder of this discussion to X" / "I therefore..." / "this is supported by the fact that..." / "warrants the closer look below" — meta-commentary on the writing.
- "This is the standard X argument under which Y" — labeling the argument by name (Y is what matters; X is researcher framing).
- "any error in $\hat\theta$ scales the welfare proportionally" — reflecting on estimator imprecision in casual aside.
- "the choice of which $r$ to use is a matter of convenience" — reflection on author's decision-making.
- "I view this as a robustness extension" / "left to a future revision" / "is deferred" — author-decision meta-language.
- Long parentheticals justifying choices ("for tractability we assume...", "we use X because Y is impractical").

**Allowed and preferred:**

- Direct claims about the model, data, or result. Example: "Each plot accounts for a vanishing share of district pumping" — substantive, no labeling needed.
- Forward references that locate content ("Appendix~X reports the robustness check", "Section~Y derives the estimator") — these are pointers, not justifications.
- Stating an assumption matter-of-factly: "Atomistic farmers take the current head as parametric" — declarative, no "the standard X argument" framing.

**How to apply:**

Before saving any manuscript prose, ask: does the sentence describe substance, or does it describe what the writer is thinking/doing? The latter is a research note and should be cut or rewritten.

Concrete examples of what to remove from the Water and Crop manuscript:
- "I devote the remainder of this discussion to its identifying variation and the underlying exclusion restriction." → just delete; let the next paragraph speak.
- "This is the standard atomistic price-taker argument under which farmers take the current head as parametric and individual extraction has only a second-order effect on the average cost." → rewrite as "the head facing the plot enters the choice problem as a parameter that the plot's own crop choice cannot meaningfully move" (substance only, no labeling).

This rule applies across all research projects under `0.AI/Research/`.
