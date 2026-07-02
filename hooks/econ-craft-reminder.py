#!/usr/bin/env python3
"""
Econ-Craft Reminder Hook

UserPromptSubmit hook. When the user asks Claude to WRITE / DRAFT / REVISE /
POLISH manuscript PROSE inside the 0.AI workspace, this injects a compact
reminder to load the positive craft layer (AI_Writing_Guide_EconCraft.md +
econ_prose_exemplars.md) and apply it directly, plus a one-screen cheat of the
top craft moves. This closes the gap where the craft guidance exists but is
not loaded before Claude composes.

Design: biased toward firing. A missed fire means mechanical prose (the whole
problem we are fixing); a false fire is one short paragraph Claude can ignore.
Filtering is by (write-verb) AND (prose-target OR intent-phrase) AND
(0.AI context), because UserPromptSubmit has no matcher and runs on every
prompt. Tune sensitivity by editing the keyword lists below.

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

CRAFT_GUIDE = r"C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\AI_Writing_Guide_EconCraft.md"
EXEMPLARS = r"C:\Users\haozh\Documents\Dropbox_Chapman\0.AI\Claude Master\econ_prose_exemplars.md"
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


def should_fire(prompt: str, cwd: str) -> bool:
    p = prompt.lower()
    c = (cwd or "").lower()

    in_workspace = any(m in c for m in WORKSPACE_MARKERS)
    if not in_workspace:
        return False

    intent = has_phrase(p, INTENT_PHRASES)
    write_verb = has_word(p, WRITE_VERBS)
    prose_noun = has_phrase(p, PROSE_NOUNS)
    code_signal = has_phrase(p, CODE_SIGNALS)

    if intent:
        return True

    if write_verb and prose_noun:
        return True

    # write-verb alone, with a code signal and no prose target -> stay silent.
    if write_verb and not prose_noun and code_signal:
        return False

    return False


REMINDER = (
    "[econ-craft] This looks like manuscript-prose writing/polishing in the 0.AI workspace. "
    "Before composing, load the POSITIVE craft layer so the output reads like a specific economist, not an LLM:\n"
    f"  1. Read {CRAFT_GUIDE}\n"
    f"  2. Skim {EXEMPLARS} for the relevant move(s).\n"
    f"  3. {ACADEMIC_GUIDE} still governs surface rules (no em-dash/colon/semicolon, active voice, numbers not adjectives).\n"
    "  4. Then apply the craft directly to the edit (run the econ-craft skill if a fuller pass is wanted).\n"
    "Top craft moves to apply right now:\n"
    "  - Intuition first: give the mechanism / a concrete example before the estimate or notation.\n"
    "  - Agent + active verb: a flesh-and-blood subject does something; hunt and kill zombie nouns (-tion/-ment/-ity).\n"
    "  - Given before new: open each sentence with old information, end on the new payload.\n"
    "  - Vary rhythm by ear: 15-25 words is a center of mass, not a target; land a long setup with a short verdict sentence.\n"
    "  - Weld every magnitude to a benchmark (vs. OLS, vs. the mean, vs. a familiar quantity); the number carries the claim.\n"
    "  - One name per concept; repeat the keyword instead of cycling synonyms.\n"
    "  - All rhythm via periods and parentheses. No em-dash, colon, or semicolon in prose.\n"
    "Clarity is the floor; sounding like a specific economist is the ceiling."
)


def main() -> int:
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError):
        return 0

    prompt = data.get("prompt", "") or ""
    cwd = data.get("cwd", "") or ""

    if not should_fire(prompt, cwd):
        return 0

    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": REMINDER,
        }
    }
    json.dump(output, sys.stdout)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
