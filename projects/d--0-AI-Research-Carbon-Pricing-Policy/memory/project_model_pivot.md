---
name: Carbon Pricing Policy — model architecture pivot to single-country
description: As of 2026-05-06, the theoretical framework is single-country small-OE built on Sun (2026) note + (z, eps) extension; multi-country AFT model is legacy
type: project
originSessionId: 989f0ece-2b64-4612-953b-46deb8ca9663
---
**Fact.** As of 2026-05-06, the Carbon Pricing Policy paper's theoretical framework is a *single small-open-economy heterogeneous-firm* model, calibrated to China only. The earlier multi-country AFT-style model (`latex/drafts/model_v0.tex`) is preserved as legacy but no longer the canonical reference.

**Why:** (i) The Chinese spoke (ASIF × CIEPD × Customs) is the binding identification engine and is naturally a single-country object. (ii) The asymmetric intensive-margin response observed in F3 (per-pair imports ↓ much more than per-pair exports) admits a closed-form derivation in the single-country setup that the multi-country model does not. (iii) Selection mechanisms generalize cleanly without the multi-country complementarity machinery. The pivot was decided in a coauthor meeting prior to 2026-05-06.

**How to apply:**

- The canonical model document is `latex/drafts/model_haoning_v2.tex` (11-page PDF as of 2026-05-07). It contains: setup, joint (z, ε) heterogeneity, cutoffs, destination-based tax mechanism (rebate share r), per-firm propositions, country-margin corollary, GE algorithm, abatement extension. Coauthor circulation file.
- The model spine is Haoning Sun's April 2026 note (`latex/Carbon_Pricing_Policy_and_International_Trade(1).pdf`), which adapts Kwon-Zhao-Zhao 2023.
- The four changes from Sun's note: (1) baseline drops the CBAM-style foreign demand penalty τ\*(δ̄) → CBAM is a separate counterfactual; (2) joint (z, ε) heterogeneity collapsing to effective productivity z̃ = z·ε^(-αβ); (3) per-firm propositions added (Sun's note skipped them); (4) destination-based carbon tax with rebate share r added (2026-05-07) for country-margin asymmetry.
- The model has **two single-parameter testable predictions**:
  - **Per-pair asymmetry**: per-firm export invariant; per-firm import falls iff η > 1 + (1-α)(σ-1). For (α=0.7, σ=4, η=3) ξ=0.45 < 1, asymmetry holds.
  - **Country-margin asymmetry**: $\Delta\log V^X/\Delta\log V^M_{\text{ext}} = 1-r$ where r∈[0,1] is the trade-weighted share of firms/sectors with destination-based treatment (free allocation / output-based benchmark). r=0 → symmetric extensive response; r=1 → exports invariant. Empirically r∈[0.7, 0.95] for EU ETS Phase 1–3 trade-exposed sectors.
- **CRITICAL math note**: a fixed proportional rebate where every firm pays $(1-r)\tau$ does NOT deliver the asymmetry — the elasticity of cost in $\log\tau$ is unchanged. The correct interpretation is r = share of firms with FULL rebate; the remaining 1-r face full origin-based tax. This was a math error in the initial 2026-05-07 plan draft and corrected before implementation.
- The skeleton (`latex/paper_skeleton.tex`) §6 has been rewritten to this single-country summary (May 2026). Decisions D14-D19 and questions Q13-Q17 record the pivot and the rebate addition.
- §9 (Calibration) and §10 (Counterfactuals) of the skeleton **still contain stale multi-country notation** flagged with TODO markers.
- Plan file: `C:\Users\haozh\.claude\plans\luminous-pondering-gadget.md` (approved 2026-05-06; updated 2026-05-07 with Step 6).
- Next gating items: Q8 (matched ASIF×CIEPD×Customs availability) for calibration; coauthor sign-off on the updated `model_haoning_v2.pdf` before proceeding to GE numerical implementation (Step 4 of the plan).
