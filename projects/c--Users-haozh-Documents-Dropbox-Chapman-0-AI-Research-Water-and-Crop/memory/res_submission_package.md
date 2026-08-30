---
name: res_submission_package
description: RES (Review of Economic Studies) submission rules as read 2026-08-30 and where the RES package lives; paper is over the 45/30 page caps at 12pt
metadata: 
  node_type: memory
  type: project
  originSessionId: 317e2324-b164-41c6-a9c1-b53f11154e36
  modified: 2026-08-30T11:38:04.719Z
---

RES submission package built 2026-08-30 in `Submissions/RES/` (target after the AER desk reject
of 2026-08-24). Generators: `program/sandbox/flatten_manuscript_res_20260830.py`
(manuscript_v4.tex -> latex/manuscript_res.tex, derived only, asserts on v4 text) and
`program/sandbox/split_manuscript_res_20260830.py` (main / online appendix PDFs with links).
Cover letter `Submissions/RES/cover_letter_RES.tex` reads headline numbers from
`tables/cf_headline_macros.tex`.

RES rules (restud.com/submissions, verbatim copy saved in
`quality_reports/submissions/RES_submissions_page_2026-08-30_verbatim.txt`):
- Editorial Express (editorialexpress.com/restud); single PDF; fee USD 250 from 1 June 2026,
  USD 150 if EVERY author is a student / within 6 yrs of PhD / resides in a low- or
  middle-income economy (World Bank; China = upper-middle-income FY2027), evidence links required.
- Main paper UNDER 45 pages incl. title page, tables, figures, references, appendices; 12-pt font
  throughout, 1.5 spacing (references and footnotes may be single-spaced), margins >= 1 in,
  numbered pages. Online appendix labelled "Online Appendix", <= 30 pp, same font/spacing.
  Exceptions only by prior request to Elias Papaioannou.
- Abstract <= 150 words + keywords; title page with department, institution, city+postcode,
  country, corresponding author's telephone/fax/email (one corresponding author).
- Acknowledgements before references, not in footnotes; separate Funding and Conflict-of-interest
  sections (suggested guidance). Tables: no vertical lines, coloured text, shading.
- Cover letter required (DCAP exemption requests go there). Submitting = accepting DCAP
  (DCAS v1.0). Sole submission; rejected papers cannot be resubmitted uninvited.

**Why:** at 12pt the v4 draft runs 55 pp main + 32 pp appendix in Source Serif with parskip;
the RES build uses Times (tgtermes via derived paper_res.sty), indent-only paragraphs, and 8pt
exhibits in the APPENDIX ONLY (published RES tables are 8pt vs 10pt body; the 12pt rule covers text
only). A blanket 8pt hook on every tabular also shrank the title-page author block and the main-text
tables; the user rejected that ("too small"), so main-text tables stay at the generators' 10pt. v4 moved
Figure 1 (district map) and Table 1 (crop categories) into Appendix A with tracked "Appendix" pointers.
Result 50 + 30: appendix at cap, main 6 over. Margins (1in), spacing (18pt = 1.5 x 12pt), and the
appendix text font ("12pt applies to the entire manuscript, including appendices") are fixed by rule,
so the rest is content; the decision (cut 6 pp of main text vs. exception request) is the author's.
Measured: moving the crop-share fit table saves 1 main page but costs 2 appendix pages by reflow.

**How to apply:** rerun flatten -> compile (pdflatex x3 + bibtex in latex/) -> split before any
RES upload; never edit the PDFs; recheck the README checklist in `Submissions/RES/`.
Related: [[project_manuscript_versions_v4_working_draft]], [[feedback_focused_scope_not_cascade]].
