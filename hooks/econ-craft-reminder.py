#!/usr/bin/env python3
"""
Econ-Craft Reminder Hook

UserPromptSubmit hook. Fires on prose-writing intent and injects two payloads:

  * MANNERED_PROSE -- Anthropic's anti-pattern definition, in EVERY project and
    on every model. Their guidance is to deliver this in a user message rather
    than the system prompt, which is exactly what this hook does.
  * REMINDER -- the econ craft layer (personal guide, craft guide, modern
    exemplar bank, academic guide) plus a one-screen cheat of the top craft
    moves. Gated to the 0.AI workspace, because it points at files that live
    there.

Design: biased toward firing. A missed fire means mechanical prose (the whole
problem we are fixing); a false fire is one short paragraph Claude can ignore.
Filtering is by (write-verb AND prose-target) OR intent-phrase, because
UserPromptSubmit has no matcher and runs on every prompt. Tune sensitivity by
editing the keyword lists below. Note there is no model field in the hook input
and no $CLAUDE_MODEL, so nothing here can branch on Fable vs Opus.

Contract (Claude Code, confirmed 2026-06): exit 0 and print JSON with
hookSpecificOutput.additionalContext to inject context discreetly. Fail-safe:
any error exits 0 silently so a prompt is never blocked.

Hook Event: UserPromptSubmit
"""

from __future__ import annotations

import json
import re
import sys

# ----------------------------------------------------------------------------
# TUNABLE KEYWORD LISTS  (edit these to adjust sensitivity)
# ----------------------------------------------------------------------------

# Writing-intent verbs. Matched as whole words (so "edit" won't fire on "credit").
WRITE_VERBS = [
    "write", "writing", "draft", "redraft", "rewrite", "rewriting",
    "revise", "revising", "revision", "edit", "editing", "refine", "refining",
    "polish", "polishing", "tighten", "tightening", "sharpen", "sharpening",
    "reword", "rephrase", "rephrasing", "improve", "improving", "clean up",
    "wordsmith", "deslop", "smooth",
]

# Prose targets. If a write-verb co-occurs with one of these, we treat the
# task as manuscript prose (NOT code). This is what keeps code prompts silent.
PROSE_NOUNS = [
    "paragraph", "sentence", "abstract", "introduction", "intro",
    "section", "subsection", "prose", "manuscript", "paper", "draft",
    "passage", "wording", "phrasing", "conclusion", "discussion",
    "literature review", "lit review", "writeup", "write-up", "write up",
    "text", "wording", "narrative", "exposition", "preamble", "motivation",
    ".tex", "skeleton", "the writing", "this writing", "my writing",
]

# Intent phrases that signal "make this read like real econ writing" even
# without an explicit write-verb + prose-noun pair.
INTENT_PHRASES = [
    "read better", "reads better", "make it flow", "make this flow",
    "sounds ai", "sounds like ai", "sounds robotic", "too mechanical",
    "less robotic", "less mechanical", "sounds machine", "machine-generated",
    "sound like a real economist", "sound more natural", "more natural",
    "less ai", "anti-ai", "ai tells", "ai-tell", "econ-craft", "econ craft",
    "make it read", "doesn't read like", "does not read like",
]

# Hard negatives: if present AND no prose-noun is present, stay silent. These
# catch code / data tasks that happen to use a write-verb ("write a script").
CODE_SIGNALS = [
    "script", "function", "compile", "debug", "do-file", "do file",
    "regression code", "dataframe", "merge the data", ".py", ".do", ".r ",
    ".jl", "stata code", "matlab", "the code", "this code", "a program",
]

# 0.AI workspace markers (case-insensitive substring on cwd).
WORKSPACE_MARKERS = ["0.ai", "dropbox_chapman", "claude master"]

# ----------------------------------------------------------------------------

PERSONAL_GUIDE = r"C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Personal.md"
CRAFT_GUIDE = r"C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_EconCraft.md"
EXEMPLARS = r"C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\econ_prose_exemplars.md"
MODERN_BANK = r"C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\econ_exemplars_modern\README.md"
ACADEMIC_GUIDE = r"C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_Academic.md"


def has_word(text: str, words: list[str]) -> bool:
    for w in words:
        if " " in w or "." in w:
            if w in text:
                return True
        else:
            if re.search(r"\b" + re.escape(w) + r"\b", text):
                return True
    return False


def has_phrase(text: str, phrases: list[str]) -> bool:
    return any(p in text for p in phrases)


def writing_intent(prompt: str) -> bool:
    """Prose-writing intent, independent of which project we are in.

    Deliberately not gated on the workspace: mannered prose is a defect in any
    project and on any model, so the anti-pattern block below travels everywhere.
    Only the econ-specific payload is workspace-gated.
    """
    p = prompt.lower()

    if has_phrase(p, INTENT_PHRASES):
        return True

    write_verb = has_word(p, WRITE_VERBS)
    prose_noun = has_phrase(p, PROSE_NOUNS)
    if write_verb and prose_noun:
        return True

    # write-verb alone, with a code signal and no prose target -> stay silent.
    if write_verb and not prose_noun and has_phrase(p, CODE_SIGNALS):
        return False

    return False


def in_econ_workspace(cwd: str) -> bool:
    return any(m in (cwd or "").lower() for m in WORKSPACE_MARKERS)


REMINDER = (
    "[econ-craft] This looks like manuscript-prose writing/polishing in the 0.AI workspace. "
    "Before composing, load the POSITIVE craft layer so the output reads like a specific economist, not an LLM:\n"
    f"  1. Read {PERSONAL_GUIDE} FIRST. It is authoritative -- these are rules you stated while\n"
    "     looking at your own drafts, and they override the other two guides where they disagree.\n"
    f"  2. Read {CRAFT_GUIDE} for the positive craft layer.\n"
    f"  3. Open {MODERN_BANK} and read the section you are about to write -- abstract, intro hook,\n"
    "     contribution, identification, results, mechanism, or conclusion. 34 passages from 21 top-5\n"
    "     applied papers, 2018-2025. Read them BEFORE composing, not after: every other writing tool\n"
    "     here filters finished text, and filtering machine prose only yields de-slopped machine prose.\n"
    "     Take the move order, never the phrasing.\n"
    f"  4. Skim {EXEMPLARS} for the relevant craft move.\n"
    f"  5. {ACADEMIC_GUIDE} governs surface rules, except where the personal guide overrides it.\n"
    "  6. Then apply the craft directly to the edit (run the econ-craft skill if a fuller pass is wanted).\n"
    "Top craft moves to apply right now:\n"
    "  - WRITE CUMULATIVE SENTENCES: one main clause plus a chain of subordinate clauses\n"
    "    (where/since/so that/which/while/thereby -ing). Never open a sentence by restating the\n"
    "    previous one; fold it in as a subordinate clause. Short declaratives that give each fact its\n"
    "    own sentence are the defect, not the goal. One short verdict after a long setup, once per paper.\n"
    "    On length: the author's accepted paragraphs measure about 40 words per sentence, while 50\n"
    "    top-5 applied papers measure 24.9 in paragraphs of 6.5 sentences. Build cumulatively, but do\n"
    "    not pad to hit a count. ABSTRACTS ARE EXEMPT -- they run near 22 words and as low as 12.\n"
    "  - Verb energy is the human/AI test: reap, export, lock, shelter -- not capture, bear, allow, give.\n"
    "  - Intuition first: give the mechanism / a concrete example before the estimate or notation.\n"
    "  - Agent + active verb: a flesh-and-blood subject does something; hunt zombie nouns (-tion/-ment/-ity).\n"
    "  - Given before new: open each sentence with old information, end on the new payload.\n"
    "  - Topic sentence carries the paragraph's meaning: 'To examine X, I do Y.' No warm-up.\n"
    "  - Transitions between topic shifts are REQUIRED ('I first look at', 'I next examine',\n"
    "    'Turning to'). Discourse markers (Crucially, Furthermore) stay -- do not strip them.\n"
    "  - Weld every magnitude to a benchmark (vs. OLS, vs. the mean, vs. a familiar quantity).\n"
    "  - One name per concept; repeat the keyword instead of cycling synonyms.\n"
    "  - Default to no em-dash, colon, or semicolon, but carry subordination with commas and\n"
    "    conjunctions. Fix by rewriting, never by substituting punctuation at the same break point.\n"
    "Clarity is the floor; sounding like a specific economist is the ceiling."
)


# Anthropic's own anti-pattern definition, reproduced verbatim -- the exact wording
# is what does the work, so do not paraphrase it. Their guidance is to deliver this
# in a user message rather than the system prompt, which is what a UserPromptSubmit
# hook does. Documented for Fable 5.1 (whose prose runs dense); the definition is
# model-agnostic and is harmless on Opus 5, which cannot be detected here anyway --
# UserPromptSubmit hooks receive no model field.
# Source: platform.claude.com .../prompting-claude-fable-5-1 (writing density),
#         platform.claude.com .../prompting-claude-opus-5 (deliverable length).
MANNERED_PROSE = (
    "[prose] Mannered prose substitutes metaphor and flourish for direct statement. "
    "Instead of \"a parameter worth varying,\" the mannered writer produces \"a dial worth "
    "turning.\" Instead of \"this point still matters,\" they write \"this point earns its "
    "keep.\" The phrases exist to display the writer, not to convey the idea, and readers can "
    "tell. That is why mannered prose irritates: it makes the reader work harder so the writer "
    "can perform. It is also imprecise. Metaphors drag in connotations the writer did not "
    "choose and cannot control. The fix is to say what you mean. When a literal phrase is "
    "available, use it.\n"
    "Match the length of written documents to what the task needs: cover the substance, but do "
    "not pad with filler sections, redundant summaries, or boilerplate."
)


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError):
        return 0

    prompt = data.get("prompt", "") or ""
    cwd = data.get("cwd", "") or ""

    if not writing_intent(prompt):
        return 0

    # The econ craft layer only makes sense inside the 0.AI workspace, since it
    # points at guides and an exemplar bank that live there. The mannered-prose
    # definition applies to any prose in any project, so it always ships.
    context = (REMINDER + "\n\n" + MANNERED_PROSE
               if in_econ_workspace(cwd) else MANNERED_PROSE)

    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        }
    }
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
