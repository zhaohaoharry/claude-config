---
name: feedback-relational-claims-go-stale
description: "Prose that asserts a RELATION between macro values (\"more than triples\", \"far smaller than\") goes stale silently on a re-run; print the figures instead"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 77cdb1a4-fa85-47f0-bd23-b7e966521efe
  modified: 2026-08-10T03:02:08.065Z
---

Never write a claim that asserts a relation between generator-written macros without printing the numbers the relation rests on. Write "at 16.00\% under autarky, 17.32\% under bilateral trade, and 16.00\% under centralization", not "far smaller under autarky than under the trade regimes".

**Why:** a relational claim carries no number of its own, so a macro rebuild cannot contradict it, the provenance audit cannot see it, and a two-pass compile reports zero errors while the sentence has become false. This has broken twice in Water and Crop, both caught by the author reading the page rather than by any tool. "More than triples" survived the 2026-08-09 price fix that moved the autarky tax from \$65 to \$150 against a centralized \$234 (1.56x, not 3x). "The autarky cap far smaller than the trade-regime caps" was stale from the pre-fix 10.3\% vintage and was flatly false against 16.00 / 17.32 / 16.00 for eleven months of drafts.

**How to apply:** when a re-run moves any headline quantity, grep the manuscript for comparative language near the affected macros (triples, doubles, far smaller, larger than, half again, well below, outweighs). Each one is a hand-typed assertion that no generator maintains. If a relation genuinely must be stated, print both figures in the same sentence so a future shift shows on the page.

See [[feedback-every-number-has-provenance]] and [[feedback-verify-by-reexecution-not-rederivation]]. Live instance to re-check: "more than half again the autarky rate" in sec:cf.
