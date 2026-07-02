---
name: journal-fit
description: Adapt and critique a manuscript's writing to a target economics journal's house style (English top-5 and top Chinese journals). Detects the target journal, loads its style guide, then either gives a fit critique with concrete rewrites or applies the conventions while editing. Use when targeting or submitting to a specific journal, or when asked to make writing "fit" a journal.
---

# journal-fit — write to a target economics journal's style

Adapts a paper's framing, positioning, structure, abstract, and register to the
conventions of a specific top economics journal. Covers the English top-5 (AER, QJE,
JPE, Econometrica, REStud) and top Chinese journals (经济研究, 管理世界, 世界经济,
经济学（季刊）); more are added over time.

**Scope.** This skill governs JOURNAL FIT — framing, structure, abstract conventions,
citation and policy norms, register. It does NOT replace prose-quality rules: defer to
`C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Academic.md`
for grammar/style and to `~/.claude/rules/table-figure-format.md` for tables/figures.

## 1. Detect the target journal — in this priority order
1. **Explicit** — the user named one (`/journal-fit QJE`, "make this fit 经济研究",
   "target the AER"). Use it.
2. **Project file** — read the current project's `CLAUDE.md` for a line like
   `Target journal: <name>`. If present, use it.
3. **Ask** — if neither, ask which journal (AskUserQuestion). Never guess.

Resolve the name to a reference file via the alias table below.

## 2. Load the guide
- Load BOTH `references/_common-<english|chinese>-top.md` (cross-cutting norms) AND
  the specific `references/<lang>/<journal>.md`.
- The per-journal file specializes/overrides the common file. Read both before commenting.

## 3. Pick the mode
- **Critique / fit report (default).** Run the journal guide's §12 checklist against the
  draft (or the user's editor selection). Output: (a) what already fits; (b) the top 3–6
  fit gaps, each tied to a guide section and with a concrete, quotable rewrite; (c)
  specific feedback on the abstract, the introduction, and the contribution statement.
  Do not silently rewrite the whole paper.
- **Refine / rewrite.** When asked to "refine" or "rewrite to fit X", produce concrete
  edited passages (intro hook, contribution paragraph, abstract) in the journal's style,
  preserving the author's argument, results, and voice.
- **Ambient.** When editing a manuscript in a project whose CLAUDE.md names a target
  journal, apply that journal's conventions as part of normal editing, and flag any large
  structural mismatch (e.g., a standalone "Literature Review" section in a journal that
  weaves the literature in).

## 4. Guardrails
- **Conventions, not a cage.** Never flatten the author's prose into a template. Adapt
  framing and structure; preserve the argument, the evidence, and the author's voice.
- **Ground every suggestion in the guide.** Tie each point to a specific guide section;
  do not invent norms.
- **Respect house rules** from the global writing guide: no equations in abstracts; no
  boldface in running text; "et al." for 3+ authors; AER/RES table-figure format.
- **Language.** English target → respond and rewrite in English. Chinese target → coach
  in Chinese, using the real section terms (引言, 理论分析与研究假设, 边际贡献,
  机制检验, 稳健性检验, 政策启示).
- **Currency.** Each guide is date-stamped (§1). If it is stale (older than ~1 year),
  say so and offer to refresh it from recent issues.

## Alias table
| Aliases | File | Status |
|---|---|---|
| AER, American Economic Review | `english/AER.md` | built |
| QJE, Quarterly Journal of Economics | `english/QJE.md` | built |
| JPE, Journal of Political Economy | `english/JPE.md` | built |
| ECMA, Econometrica | `english/econometrica.md` | built |
| REStud, ReStud, Review of Economic Studies | `english/restud.md` | built |
| 经济研究, Jingji Yanjiu, Economic Research Journal, ERJ | `chinese/jingji-yanjiu.md` | built |
| 管理世界, Guanli Shijie, Management World | `chinese/guanli-shijie.md` | built |
| 世界经济, Shijie Jingji, Journal of World Economy | `chinese/shijie-jingji.md` | built |
| 经济学（季刊）, 经济学季刊, China Economic Quarterly, CEQ | `chinese/jingjixue-jikan.md` | built |

## Composition with other skills
For **English top-5** targets, this skill governs house-style *fit*; the underlying
craft is handled by the AEA-family workflow skills (`aer-topic-selection`,
`aer-identification`, `aer-robustness`, `aer-introduction`, `aer-tables-figures`,
`aer-submission`, `aer-rebuttal`, `aer-replication`, sequenced by `aer-workflow`) and
the general skills `review-paper`, `econometrics-playbook`, `bib-validate`,
`writing-deslop`. Each English top-5 guide carries a "Companion skills" pointer.
Those skills encode AER/AEA house defaults (100-word abstract, booktabs, AEA data
policy); for non-AER targets the per-journal guide overrides them.

## Adding or refreshing a journal
Guides are built by reading 8–12 recent exemplar papers (Zotero + project `literature\`
folders + online full texts) and filling the 12-section template in `references/_schema.md`.
To add or refresh a journal, gather recent exemplars, fill the schema, and date-stamp §1.
The Zotero inventory helper lives at
`Claude Master\journal_exemplars\_scan\zotero_scan.py`.
