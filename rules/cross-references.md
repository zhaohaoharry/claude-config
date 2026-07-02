# Cross-References in Academic Manuscript Prose

Universal rule for all research projects under `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Research\`.

## The Rule

In manuscript prose:

1. **Natural-sentence cross-references are fine and often necessary.** Writing "Appendix X documents the conventions" or "the calibration is described in Appendix Y" or "Section Z reports the estimates" is normal academic prose. Keep these. The reader needs to know where supporting material lives, and the manuscript must point to its own appendices.

2. **Bare parenthetical cross-references are not fine.** Do not write `(Appendix X)`, `(Section 7.3)`, or `(see Appendix~\ref{app:Y})` as a standalone parenthetical inserted into a sentence. These read as abrupt navigational tags and add nothing to the reader's understanding at that point in the prose.

3. **If a parenthetical pointer is truly needed, write it out explicitly.** Use `(see Appendix X for details)` or `(see Section 7.4)` instead of the bare `(Appendix X)`. The "see ... for details" framing makes the navigational intent explicit; the bare tag does not.

## Examples

**GOOD** (natural-sentence references):
- *"Appendix~\ref{app:plot_reconstruction} documents the pixel-history conventions, the per-pixel acreage assignment, and the plot reconstruction procedure."*
- *"The vintage list and the construction of the annual panel between vintages are described in Appendix~\ref{app:data}."*
- *"The cap fraction $x$ is calibrated row by row in Section~\ref{sec:counterfactual_design} to deliver the SGMA target."*

**GOOD** (explicit parenthetical pointer):
- *"The ranking reverses below a \$940/AF crossover (see Section~\ref{sec:sensitivity} for the full grid)."*
- *"Mean realized $\overline{AC}$ ranges from \$60 to \$110/AF (see Appendix~\ref{app:swp_calibration} for anchor data)."*

**BAD** (bare parenthetical):
- *"The ranking reverses below a \$940/AF crossover (Section~\ref{sec:sensitivity})."*
- *"... anchored to literature-defensible California sources (Appendix~\ref{app:sigma_decomposition}):"*
- *"(\$260--\$960/AF across years; Appendix~\ref{app:swp_calibration})"*

## Object References

`\ref{tab:X}`, `\ref{fig:Y}`, `\ref{eq:Z}` are subject to the same rule (clarified 2026-06-16). A bare parenthetical tag like `"(Figure~\ref{fig:X})"` or `"(Table~\ref{tab:Y})"` is **not** acceptable — the user finds it extremely unclear. Write the reference into the sentence: `"Figure~\ref{fig:X} shows..."`, and at the **first** reference to a figure or table prefer `"as Figure~\ref{fig:X} demonstrates/illustrates/shows"`. If a parenthetical pointer is genuinely needed, write `"(see Figure~\ref{fig:X})"`, never the bare `"(Figure~\ref{fig:X})"`. (Earlier versions of this rule exempted object refs; that exemption is withdrawn.)

## External Bibliographic References

External documents like *"DWR Bulletin 132 Appendix B tables"* or *"reported in Hanak et al. (2019), Table 3"* are bibliographic, not internal navigation. They are fine in any form (parenthetical, inline, etc.) since they cite a specific external artifact rather than telling the reader to flip elsewhere in the same document.

## Rationale

Bare parenthetical cross-references read as abrupt navigational tags lifted from a thesis chapter or a research note. Top-5 journals expect prose where every parenthetical contributes a piece of information the reader needs at that moment. A bare `(Appendix X)` doesn't — it tells the reader "go elsewhere," which the reader doesn't need an interruption to know how to do (the TOC handles that). The explicit `(see X for details)` form, when used, signals to the reader that the parenthetical is a deliberate pointer rather than a content fragment.
