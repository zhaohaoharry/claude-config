---
name: No author-decision meta-sentences in manuscripts
description: Never include sentences that reveal the author's decision/iteration history (alternative-comparison justifications, "left to a future revision", "is deferred", "earlier specifications of this model required", "subsumes any rank-restricted parametric form used in prior work", "I view ... as a robustness extension"). The published draft presents methodology as a finished product, not a record of choices made. Applies across all research projects.
type: feedback
originSessionId: 78ced47c-e9ad-4b4d-84b1-a497ab260cb9
---
A manuscript draft is for the reader. It presents the methodology and results as a finished product. It does not narrate the author's process, alternative specifications considered, future plans, deferred extensions, or comparisons to "what an earlier version of this model required."

**Disallowed phrasings:**

- *Alternative-specification justifications:* "subsumes any rank-restricted parametric form $F(s, c)$ used in prior work, because the additive form is a strict linear combination..."; "An alternative renewal action $r$ would also satisfy ... but would require..."
- *Future-revision references:* "is left to a future revision"; "an external IV would resolve this; it is left to a future revision"; "is deferred"; "is the standard remedy and is deferred"
- *Iteration-history references to one's own model:* "earlier specifications of this model required"; "earlier specifications squeezed into a parametric transition-cost form"
- *Author-meta opinions:* "I view ... as a conservative upper bound"; "is partly tautological"; "sensitivity to a Walrasian variant is a robustness extension"; "this raises a substantive question about what the dynamic-discrete-choice machinery adds beyond..."
- *Process-of-analysis exposure:* "this is an out-of-sample extrapolation that I treat with explicit caveats in Section X below" (the caveat itself is fine; the meta-comment is not)
- *Choice-to-ideal comparisons:* "neither is the textbook idealized instrument"; "this is not a textbook Pigouvian/cap-and-trade ideal"; "rather than the textbook X benchmark"; "two specific, rigid implementations rather than the ideal" — comparing the modeled choice against an unmodeled ideal exposes the author's decision boundary
- *Scope-disclaimer references:* "more flexible designs lie outside the set considered here"; "X is not considered in this paper"; "alternative implementations are beyond the scope" — these telegraph what is NOT done rather than describing what IS
- *Operational-definition exposure:* "the same-crop conditioning is my operational definition of a planting decision"; "my treatment of X as Y" — never name the construct as the author's chosen operational handle. State what the construct IS, not that the author defined it.
- *Sample-construction decision verbs:* "I drop three districts"; "I exclude observations with X"; "I retain only Y"; "I restrict the panel to Z"; "the structural sample therefore excludes no district with..." — rewrite as factual statements about what the sample contains, not as author-decisions. "Three districts contribute no plot-level decisions" not "I drop three districts." Avoid defensive trailing sentences that justify the exclusion ("therefore excludes no district with non-trivial activity").
- *Modeling-choice decision verbs:* "I treat A as B"; "I view C as D"; "I parameterize X as Y rather than Z"; "I assume" — rewrite as declarative "A is B" / "X = Y" / "C and D are taken to be." If a contrast with an alternative form must be stated, state it impersonally ("a reduced-form summary rather than a derivation from confined-aquifer hydraulics") without "I treat... as."
- *Reporting-choice decision verbs:* "I report X as Y rather than Z" — rewrite passive ("X is reported as Y") or drop the contrast if the alternative has already been ruled out earlier.
- *Referee-response markers:* "which several referees flagged as candidate exclusions"; "in response to referee comments"; "following a referee's suggestion" — never name the referee process inside the manuscript. The finished draft does not narrate the review history.

**What is allowed:**

- *Caveats stated as facts:* "The cap implementation is a hard annual ceiling. SGMA permits multi-year averaging; this overstates forced fallowing in wet/dry sequences."
- *Identification statements:* "$\beta_W$ is identified from cross-district, cross-year variation in $\overline{AC}_{k,t}$..."
- *Contribution framing in introduction:* "To my knowledge no prior structural work in this literature constructs the water-cost regressor in this way" (literature contextualization is academic-standard).
- *Functional-form descriptions:* "The flow utility includes a state-by-crop intercept $\alpha_{s,c}$ that captures..."

**Rule of thumb:** if a sentence answers "why did you pick this and not the alternative?" or "what comes next in the project?", it is author-decision meta and should be cut. The manuscript should read as if the author always made these choices, not as if they are still being negotiated.

**Why:** The user flagged the sentence "The flow utility (1) contains no separate transition cost: a flexible $\alpha_{s,c}$ subsumes any rank-restricted parametric form $F(s, c) = \mathbf{1}\{s\not\to c\}[F_{\text{rem}}(s) + F_{\text{est}}(c)]$ used in prior work, because the additive form is a strict linear combination of $\alpha_{s,c}$ rows" on 2026-05-08 as exactly this kind of author-decision exposure. They asked it never appear again. Apply globally.

**How to apply:** Before any save in a draft, search the diff for: "left to a future", "is deferred", "rather than ... used in prior work", "subsume any ... form", "earlier specifications", "is a robustness extension", "I view ... as", "would resolve", "would also satisfy ... but would require", "I treat with explicit caveats". Cut or rewrite as factual prose.
