---
name: econ-craft
description: Apply the positive craft layer to economics manuscript prose so it reads like a specific economist, not an LLM. Use when asked to write, draft, rewrite, revise, refine, polish, tighten, sharpen, or improve the prose of a paper, section, abstract, introduction, or paragraph. Installs flow, rhythm, voice, intuition-first exposition, and number-anchored argument — then applies them in place. Default mode EDITS the file; pass --audit for a report-only pass. Complements writing-deslop (removes AI tells), journal-fit (house style), and proofread (correctness).
argument-hint: "[filename or section, e.g. 'main.tex', 'introduction', or '--audit introduction']"
allowed-tools: ["Read", "Grep", "Glob", "Edit", "Write"]
---

# econ-craft — build native economics-writing register, then apply it

Most of the user's writing setup is *negative* (the stop-sign list in
`AI_Writing_Guide_Academic.md` removes AI tells). This skill supplies the
*positive* layer and applies it: what good economics prose actively *does* —
flow, rhythm, voice, intuition-first exposition, and argument carried by
numbers. The aim is the ceiling, not just the floor: clarity is the floor;
sounding like a specific economist is the ceiling.

**Default behavior: apply the craft in place** (edit the `.tex`/section).
Pass `--audit` to produce a report without editing.

This skill stays in the *craft* lane. It does not duplicate:
- `writing-deslop` — flags/scores AI tells (report only).
- `journal-fit` — framing and target-journal house style.
- `proofread` — grammar, typos, notation, LaTeX correctness.
Run those for their jobs; cross-reference, don't re-do them here.

## Steps

1. **Identify what to work on.**
   - `$ARGUMENTS` is a filename → read that file.
   - `$ARGUMENTS` is a section name (e.g. "introduction") → find and read that
     section in `main.tex` or `paper_skeleton.tex`.
   - Editor selection present and no argument → use the selection.
   - Nothing specified → ask which file or section.
   - If `--audit` appears in the arguments, run in report-only mode (see below).

2. **Load the craft layer (always, before composing).**
   - `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Personal.md`
     — **read this first and treat it as authoritative.** These are the rules the author
     stated while looking at his own drafts, compiled from the project memories, and they
     override both other guides where they disagree. Three that reverse the default advice:
     body-paragraph sentences run **about 40 words** as cumulative constructions, not 15–25;
     discourse markers ("Crucially,", "Furthermore,") and flow markers ("I first look at")
     stay; and em-dash removal is a rewrite, never a substitution.
   - `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_EconCraft.md`
     — the 18 craft principles, idiom bank, and per-paper-type cheat sheet.
   - `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\econ_prose_exemplars.md`
     — verified real passages; pull the one or two that match the move you need.
   - `C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Academic.md`
     — still authoritative on every surface rule (no em-dash/colon/semicolon,
     active voice, numbers not adjectives, no math/forward-refs in the intro).
     On any conflict, the academic guide wins; the craft guide never overrides it.

3. **Tag the subfield and the section type.** Each craft principle is tagged
   `[applied-micro] [structural/macro] [theory] [finance]`. Read the project
   `CLAUDE.md` (or infer from the content) to pick the register, and use the
   per-paper-type cheat sheet in the craft guide to weight the moves (an intro
   leans on the picturable puzzle and the magnitude; a model section leans on
   intuition-before-notation and the worked example).

4. **Apply the top craft moves** (the full set is in the guide):
   - **Intuition first.** Mechanism or a concrete example before the estimate,
     the notation, or the formal result. The "Intuitively, ..." gloss earns its
     place once per idea.
   - **Agent + active verb.** Put a flesh-and-blood subject in front of an
     active, signed verb. Hunt nominalizations by suffix (-tion, -ment, -ity,
     -ance) and turn the buried verb back on. Keep genuine technical terms.
   - **Given before new.** Open each sentence with information the reader
     already has; end on the new payload. This is the main flow engine.
   - **Coherence by repetition.** One name per concept. Repeat the keyword;
     do not cycle synonyms (households/agents/individuals) to sound varied.
   - **Rhythm by ear.** 15–25 words is a *center of mass*, not a target. Vary
     length deliberately; land a long setup with a short verdict sentence.
     Read it aloud. All rhythm comes from periods and parentheses — never an
     em-dash, colon, or semicolon.
   - **Argue with numbers.** Weld every magnitude to a benchmark (vs. OLS, vs.
     the sample mean, vs. a familiar quantity). Economic magnitude over
     statistical significance. The number, not the adjective, carries the claim.
   - **Argue, don't enumerate.** Reason through the point in prose instead of
     announcing "three reasons" and listing them.

5. **Triage before polishing: revise, or redraft?** Judge the incoming passage
   first, because polishing a weak draft launders its content forward. In a
   controlled decomposition of two-stage pipelines (COLM 2026), weak draft
   *content* actively hurt the second pass, while the draft's *structure* still
   helped — so the scaffold is worth keeping even when the sentences are not.
   - **Strong draft** (the author wrote it by hand, the argument is already
     there): revise in place. A critique pass on strong prose adds real value.
   - **Weak draft** (a machine first pass, a placeholder, an argument that does
     not yet land): keep the paragraph's *role* in the section and redraft the
     prose from the `econ-introduction` contract and the results. Do not sand
     down the existing sentences — that carries the weak content forward under
     better rhythm, which is harder to spot later, not easier.
   Say which path you took in one line before the rewrite, so the author can
   disagree. When genuinely unsure, revise: it is the reversible choice.

6. **Edit in place (default).** Rewrite the passage applying the moves above,
   preserving every claim, number, citation, and one appropriate hedge. Do not
   flatten the author's voice into a template, and do not over-edit strong prose
   into the very uniformity the rhythm rule removes. Before changing a word,
   read the previous, current, and next paragraph so edits don't break flow.

   Never judge the result by asking whether it "sounds like the author." That
   assessment correlates at |r| < 0.07 with independent stylometric measures, so
   it returns confident noise. Judge against the craft moves and the exemplars,
   which are checkable.

7. **Self-check before saving** (the craft guide's after-writing checklist):
   intuition precedes formalism; subjects act; sentence length varies and at
   least one short verdict lands after a long setup; every magnitude has a
   benchmark; one name per concept; zero em-dashes/colons/semicolons in prose;
   the academic-guide stop-sign list still passes.

## `--audit` mode (report only)

Do not edit. For the target text, produce:
- A short read on the three weakest craft dimensions (flow, rhythm, voice,
  intuition-first, number-argument) with the specific passages that show them.
- 3–6 before/after rewrites, each tied to the craft principle it applies.
- A pointer to run `writing-deslop` (tells), `journal-fit` (house style), and
  `proofread` (correctness) for their separate lanes.
Save to `quality_reports/[name]_econcraft_YYYY-MM-DD.md` if a project
`quality_reports/` exists; otherwise present inline.

## Guardrails

1. **Apply by default; report only with `--audit`.**
2. **The academic guide wins every surface conflict.** The craft guide adds the
   positive layer; it never relaxes a stop-sign rule.
3. **Preserve substance.** Every rewrite keeps the claim, the numbers, the
   citations, and one appropriate hedge. Craft is not a license to change results.
4. **Voice, not template.** Adapt to the author's register and subfield; never
   homogenize. The goal is a specific economist's voice, not a house monotone.
5. **Stay in lane.** Tells → `writing-deslop`; house style → `journal-fit`;
   grammar/notation → `proofread`. Cross-reference, don't duplicate.
6. **Locate by section + opening words**, never by line number, when pointing
   at a passage.
