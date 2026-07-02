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

5. **Edit in place (default).** Rewrite the passage applying the moves above,
   preserving every claim, number, citation, and one appropriate hedge. Do not
   flatten the author's voice into a template, and do not over-edit strong prose
   into the very uniformity the rhythm rule removes. Before changing a word,
   read the previous, current, and next paragraph so edits don't break flow.

6. **Self-check before saving** (the craft guide's after-writing checklist):
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
