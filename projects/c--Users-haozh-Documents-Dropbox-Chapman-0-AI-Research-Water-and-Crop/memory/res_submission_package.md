---
name: res_submission_package
description: RES (Review of Economic Studies) submission rules as read 2026-08-30 and where the RES package lives; paper is over the 45/30 page caps at 12pt
metadata: 
  node_type: memory
  type: project
  originSessionId: 317e2324-b164-41c6-a9c1-b53f11154e36
  modified: 2026-08-31T03:30:23.174Z
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
Table 11 (welfare) was moved after the paragraph that introduces it (barrier kept, mechanism figure
still first) so p.37 fills: 49 + 30 within the rules. The author then CHOSE sub-1in margins although
RES asks for >=1in on all sides (flagged in the README; --margin1in restores): 0.8in gave 46 + 29 but
was judged "too obvious", 0.9in gave 47 + 30, then settled at 1in L/R on 08-31 (0.9 and 0.95 were interim steps; L/R now compliant),
0.85in top, 0.8in bottom;
accepted headings ending a page with one line under them (--keep-heading-rule restores), \flushbottom,
\predisplaypenalty=300 (a display may open a page), and all figures at 85% width (--figscale): 46 + 29;
then heading spacing tightened (titlespacing 2ex/1.8ex/1.2ex; --keep-heading-space) and main-text
tables UNIFIED at 10pt (\footnotesize; user first capped at 11pt, then chose uniform 10pt on 08-31;
generators had a 10/11/12pt mix): 45 + 27. PITFALL: any BeforeBeginEnvironment{tabular}
size hook also catches the \maketitle author block (titling sets \and authors in a tabular); the
flatten wraps \maketitle in a group that neutralises the hook. Title page is in RES layout (name,
then department / institution / city+postcode / country under each name; corresponding author's
email under Yinan Liu; --tel/--fax flags for the numbers RES asks for, not yet supplied).
Wide displays (eqs 8, 11, A6) stay on ONE line via \scalebox{0.88}{$\displaystyle ...$} rather than
being broken (user's preference; --eqscale). Use \scalebox, not \small before a mid-paragraph display
(that shrinks the line spacing of the text above it).
The AI-use acknowledgement was removed from manuscript and cover letter on the author's instruction
(RES page silent; some OUP journals require a generative-AI declaration with grammar tools exempt;
--ai-statement restores). Spacing (18pt = 1.5 x 12pt) and the appendix text font are fixed by rule.
On 08-31 the appendix exhibits were raised 8pt -> 10pt to match the main tables and the appendix set
raggedbottom (the wide inter-exhibit gaps were flushbottom glue on float-only [H] pages): package now
45 + 29 (74 pp), then the length route: L/R margins back to 1in and the crop-share fit table (old
Table 9) moved to Appendix A as Table A7 with the moments table (now Table 9) promoted into the 7.1
text (approved paragraph; footnote keeps the Buena Vista check): FINAL 45 + 30 (75 pp), main at the
author-accepted 45 vs the literal under-45, appendix exactly at cap. The gkt-validation figure was the one non-[H] float in v4 Appendix A and printed A8
before A7; pinned [H] in v4. Float-distance lesson: v4 preamble float fractions (0.92/0.85/0.05/0.90,
counters 3/3/5) override the flatten block, [!htbp] ignores fractions, and a float only takes space
not yet filled at its env - to pull an exhibit onto the page of its reference, move its env BEFORE the
referencing paragraph (done for Table 2 / Figure 2, envs now before the Fact-2/Fact-3 headings).
The last main-text page (45 vs "under 45") is the author's call; moving Table 9 (crop-share fit) to
the appendix is the natural single move now that the appendix has room.
Measured: moving the crop-share fit table saves 1 main page but costs 2 appendix pages by reflow.

**How to apply:** rerun flatten -> compile (pdflatex x3 + bibtex in latex/) -> split before any
RES upload; never edit the PDFs; recheck the README checklist in `Submissions/RES/`.
Related: [[project_manuscript_versions_v4_working_draft]], [[feedback_focused_scope_not_cascade]].
