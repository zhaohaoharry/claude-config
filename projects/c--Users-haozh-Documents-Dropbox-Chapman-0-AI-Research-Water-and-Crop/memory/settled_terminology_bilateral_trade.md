---
name: settled-terminology-bilateral-trade
description: "The Water and Crop manuscript no longer uses \"status quo\" — the bilateral-trade SW institution is named \"bilateral trade\" (the institution) or \"bilateral-trade\" (the adjective)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6de2f577-1ca3-423f-8df3-7772a79528ba
---

In the Water and Crop manuscript, the surface-water institution previously called "status quo" is now called **"bilateral trade"**. The rename was settled before today (e.g., `tab:cf_design` already had `\del{Status quo}\add{Bilateral trade}`) but holdovers in the abstract, intro, model section, results, and appendix were not swept until 2026-06-04.

**Naming convention:**
- The institution as a noun: **bilateral trade** (e.g., "autarky beats bilateral trade by \$0.20 billion")
- As an adjective: **bilateral-trade** (e.g., "the bilateral-trade market," "the bilateral-trade pumping schedule")
- The reference cell: **bilateral trade × open access**, or **bilateral × open access** in compact contexts (e.g., table column headers — Table 11 column reads "Bilateral")
- Old "fragmented status quo" framing should become "fragmented bilateral-trade baseline" or just "bilateral trade" — the fragmentation is implicit.

**Why:** "Status quo" was the old label when the institutional contrast was implicit (you = the world; counterfactual = the reform). Once the institutional grid became explicit ($3 \times 3$ with autarky / bilateral / centralized along the SW dimension), "status quo" stopped being a meaningful institutional label and became confusing. "Bilateral trade" is the proper institutional name — descriptive, parallel to "autarky" and "centralized" on the same axis.

**How to apply:**
- Never write "status quo" in new prose. Use "bilateral trade" / "bilateral-trade."
- When editing existing prose that still has "status quo," wrap with `\del{status quo}\add{bilateral trade}` (or the adjective form). Inside an existing `\add{}` block, replace directly without nested track-changes.
- Inside `\del{}` blocks: don't touch — those are already struck through and represent the old version.
- The reference cell label in table notes and figure captions: "bilateral-trade $\times$ open-access reference cell" (hyphenated when adjectival).
