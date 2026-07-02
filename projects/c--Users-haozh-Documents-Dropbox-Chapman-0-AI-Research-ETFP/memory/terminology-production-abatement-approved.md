---
name: terminology-production-abatement-approved
description: "Coauthors approved renaming clean/dirty technology to production/abatement technology (2026-07-02); Hongsong's handwritten note proposes a share-form \"preferred specification\""
metadata: 
  node_type: memory
  type: project
  originSessionId: c3dae0d6-96ef-491d-953c-724c0ebc0469
---

On 2026-07-02 the user reported all coauthors agree with the terminology change: the two technologies are now **production technology (ω)** and **abatement technology (ω_Z)**, replacing clean/dirty. "Biased technology" names the phenomenon (the ratio ω_Z/ω moving), never ω_Z itself. "Abatement technology" is defined broadly at first use (cleaner inputs, process change, end-of-pipe).

Hongsong's handwritten note (`latex/Emission_CleanTech_Spec.HEIC`, dated 6/23/2026, converted PNG in session scratchpad) proposes a "preferred specification" (ν=1): the share form Q^ρ = e^{ρω}X^ρ + e^{ω̂_Z}Z^ρ with composite ω̂_Z ≡ ρω + ω_Z(his) = ρ·wZ (i.e., ρ times the log dirty-augmenting technology; ρ=0.6377, σ=2.76). Under this scaling the figure's ×8.5 dirty-line growth becomes ×3.9. His points: (1) higher ω̂_Z = lower Z/Q at given inputs = cleaner; (2) identification intuition: Q–Z comovement (slope) separates ω̂_Z and τ, labor FOC/proxy (Levinsohn–Petrin, M as proxy) identifies ω; (3) ω̂_Z contains ω, so do not compare the sizes/growth of ω̂_Z and ω.

On 2026-07-02 the rename was applied **paper-wide** to `latex/manuscript.tex` (backup `manuscript_backup_20260702_pre_rename.tex`). Notation policy: **ω** = production technology (was clean/ω̃_C), **ω_Z** = abatement technology (was dirty/ω̃_Z, the augmenting ×8.5 object). The estimation keeps **ω_H** (Hicks-neutral) and renames the old non-tilde ω_Z gap to **b ≡ ω_Z − ω** ("the technology bias"), so ω_Z means abatement everywhere and b is the estimation gap. Section 2 adopts the symmetric CES and drops the 1/α effort exponent (α absent from the reduced form, so no estimated number changes). A pre-existing Taylor-coefficient error was corrected (missing ½ on the π² term; correct α=1 coeff −β(1−β)/(2σ) — see `latex/answers/answer_taylor_coefficient_correction.pdf`). Compiles 82pp, 0 undefined refs.

**Open follow-ups (NOT done):** regenerate figure PDFs whose legends bake in clean/dirty or ω̃_C/ω̃_Z (`Figure/time_trends.pdf`, `group_comparison.pdf`, `density_w*.pdf`); update the Stata/R script that generates `Table/omega_shock.tex` to emit ω/ω_Z headers (build artifact, don't hand-edit).

Related: [[etfp-motivation-aggregate-numbers]]. Section 2 standalone review copy: `latex/section2_revised_for_review.tex`.
