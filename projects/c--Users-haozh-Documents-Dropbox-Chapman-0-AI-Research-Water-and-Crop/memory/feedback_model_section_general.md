---
name: Keep model section general — empirical/calibration content goes to Empirical Strategy
description: In a model section, do not include calibration phrases ("calibrated to the historical X series"), specific empirical numbers, dataset references, sample-period descriptions, or phrases like "in the constructed panel". State each model object abstractly; concrete instantiations belong in Data, Stylized Facts, or Empirical Strategy. Applies across all research projects.
type: feedback
originSessionId: 78ced47c-e9ad-4b4d-84b1-a497ab260cb9
---
The model section presents the structural setup as if it could apply to any setting that fits the framework. Empirical realizations live elsewhere.

**Disallowed in model sections:**

- "calibrated to the historical SWP allocation series" → say only "follows a first-order Markov chain with transition matrix $\mathbf{P}_\omega$"; calibration goes to Empirical Strategy.
- Specific dollar numbers like "approximately \$50/AF" or "\$48--\$292/AF" → use abstract names ("flat wholesale rate", "cost-recovery rate $P_t^{\text{SWP,own}}$"); empirical magnitudes go to Data or Empirical Strategy.
- "In the constructed panel this affects 38 of 575 ag district-years" → empirical fact about the panel; goes to Empirical Strategy where the panel is built.
- "(Stylized Fact 2)" parenthetical references → the model setup should stand on its own; backward references to the data section dilute the abstraction.
- Specific institutional names ("Friant--Kern", "Miller--Haggin", "Bulletin 132", "USBR", "DWR") → in the model setup, use generic categories ("federal contract delivery", "priority cascade"); empirical instantiation in Data section.
- "Empirical implementation of $\mathcal{M}$ for the baseline regime" → the model object is the operator $\mathcal{M}$; how it is implemented in code is empirical-strategy detail.

**Allowed:**

- Functional forms and abstract parameters that the model needs (e.g., the spillover matrix $\beta_{kj}$, the cost-recovery rate $P_t^{\text{SWP,own}}$ as a model primitive).
- Forward references to where calibration appears: "see Section~\ref{sec:strategy_calib}".
- Generic descriptions of legal-rule categories ("federal contract delivery", "priority-rights allocation") if the model is built to accommodate this institutional structure.

**Why:** The user flagged this twice on 2026-05-08 — first on the aquifer Theis-kernel calibration drift into the model section, then on the drought-Markov-chain calibration phrase. Their rule: "model is general." Keep the model section a clean structural specification; empirical magnitudes, sample-period statements, and calibrated values go to the Empirical Strategy section. Applies across all research projects under `0.AI/Research/`.

**How to apply:** Before saving any edit to a Model section, search the diff for: "calibrated", "constructed panel", "in the data", "Stylized Fact", specific dollar/percent magnitudes, dataset acronyms (USBR, DWR, NASS, FRED, etc.), and named-entity institutional citations (Friant-Kern, Miller-Haggin, Bulletin 132, etc.). Move any matches to the appropriate downstream section.
