---
name: notation-convention-model
description: manuscript_v1.tex model/estimation notation convention after the 2026-06-17 Option-2 refactor — district k is a subscript, choice led by a semicolon, bar only for probabilities, t only on realized-path objects
metadata:
  type: project
---

Convention adopted 2026-06-17 ("full clean" Option 2). Keep all NEW model/estimation notation in this
form. Plan: `quality_reports/plans/2026-06-17_notation_option2_full_clean.md`.

**Stationary within-period objects: district k = SUBSCRIPT, choice set off by `\,;\,`, bar only for
probabilities, NO time index.**
- u_k(c\,;\, s, \omega, h)   v_k(c\,;\, s, \omega, h)   V_k(s, \omega, h)
- p_k(c \mid s, \omega, h)   \widetilde{W}_k(s, \omega, h)
- price as a function: P^{\text{water}}_k(\omega, h) = \overline{AC}_k(\omega, h)
- estimation: v^{S1}_k(c \mid s, \widetilde{AC}), \hat p_k(c \mid s, \widetilde{AC}); appendix
  v^n_k, V^n_k, p^{\text{ccp}}_k(c \mid s, \omega).
- Evaluated along the path the subscript becomes the realized district:
  p_k(c\mid s_{p,t},\omega_t,h_{k,t}), \widetilde{W}_{k(p)}(s_{p,t},\omega_t,h_{k(p),t}),
  \hat p_{k(p)}(c_{p,t}\mid s_{p,t}, \widetilde{AC}_{k(p),t}).

**Revenue/cost: drop t in the recursive SETUP, keep t in the realized/Euler context.**
- setup (flow utility, \widetilde W): R(c,s), C(c).
- Euler/data: R(c_t,s_t,t), C(c_t,t), R_{c,t}, C_{c,t}, \Delta\pi_t keep t.
- A note after the flow utility (tracked \add) says revenue and price are the period's realized
  values, calendar index suppressed in the stationary problem, restored along the path.

**t lives ONLY on realized-path / sequence objects:** \overline{AC}_{k,t}, \widetilde{AC}_{k,t}, D_{k,t},
h_{k,t}, h_{k,t+1}, \omega_t, g_{k,t}, Q/T/p^\tau_{k,t}, bill_{k,t}, \underline P_{k,t}, \pi^{sale}_{k,t},
welfare sums \sum_{p,t}/\sum_{k,t}, eq:aquifer_lom. The doubly-indexed \overline{AC}_{k,t}(\omega,h) and
\overline{AC}^*_{k,t}(\omega,h) were collapsed to the realized scalars \overline{AC}_{k,t},
\overline{AC}^*_{k,t}.

**p/P/i disambiguation (2026-06-17).** The overloaded `p` was split by distinct letters, not styles:
- **lowercase $p$ = price** (unified): source $p^\tau_{k,t}$, trade $p_t^{\text{trade},\tau}$, SWP $p_t^{\text{SWP,trade/own}}$, water $p^{\text{water}}_k$, electricity $p^{\text{elec}}$.
- **cost floor = $\underline{p}_{k,t}$** (was $\underline{P}$).
- **capital $P$ = choice probability**: $P_k(c\mid\cdot)$, $\hat P_k$, $P^{\text{ccp}}_k$ (was lowercase $p$). The equilibrium-tuple policy is $P$.
- **plot/field index = $i$** (was $p$): $A_i$, $s_{i,t}$, $c_{i,t}$, $\sum_{i,t}$, $\sum_{i:\,k(i)=k}$, $k(i)$. The plot-count symbol was dropped (just "plots indexed by $i$").
- Appendix transport LP (eq:swp_lp_app) districts: **seller $j$, buyer $k$** (reuses the spillover's $k,j$; was $i,j$). So the seller reservation price is $r_j$, distinct from aquifer recharge $r_k$. Do NOT use $\ell$ for an LP/district index — $\ell$ is already a summation index in the SWP-share formula (line ~926).
- **Perennial field states = $Y(c)$ (young) / $M(c)$ (mature)** — renamed from $P_y/P_m$ so they don't clash with the choice probability $P_k$. Only in Table~\ref{tab:state_trans} and the "Field state" paragraph. Italic $M$ vs calligraphic $\mathcal{M}$ (institution) follows the paper's existing italic/calligraphic convention. Do NOT use $m$ for "mature" — $m$ is the appendix equilibrium-loop iteration index.
- The drought-state Markov matrix is bold $\hat{\mathbf{P}}_\omega$ (distinct from italic probability $P$); left as-is (bold = matrix, standard).
- Source price $p^\tau$, $\phi_P$ (perennial coef), $\mathcal{P}$ (perennial set) were left untouched. Swap script: `program/sandbox/swap_p_notation.py`; backup `latex/manuscript_v1.tex.bak_pnotation`. Plan: `quality_reports/plans/2026-06-17_p_notation_disambiguation.md`.

A NOTE on notation/equations: per [[project_v1_tracked_working_draft]], symbol/equation changes are
SILENT apparatus (no \del/\add). Only genuinely NEW prose sentences are tracked. Backup of the
pre-refactor file: `latex/manuscript_v1.tex.bak_notation`.
