---
name: research-ideation
description: Generate structured research questions, testable hypotheses, and empirical strategies from a topic, dataset, or observation. Use when brainstorming a new project or extension. For an interactive interview that formalizes a single vague idea into a spec, use interview-me.
argument-hint: "[topic, dataset, stylized fact, or 'extend [paper title]']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "WebSearch"]
---

# Research Ideation

Generate structured research questions and empirical strategies from a topic or observation.

**Input:** `$ARGUMENTS` — a topic, dataset, stylized fact, or "extend [paper]".

## Steps

1. **Understand the starting point** from `$ARGUMENTS`.
   - If a paper: read it and identify what's left unanswered.
   - If a topic: think about the key mechanisms, open empirical questions, and available data.
   - If a dataset: think about what variation it offers and what questions it can identify.

2. **Generate 3-5 research questions** at different levels:
   - Descriptive (what is happening?)
   - Causal (what causes what?)
   - Welfare / policy (what should be done?)

3. **For each question, develop:**
   - A testable hypothesis
   - A plausible identification strategy (ideal experiment, natural experiment, IV, DiD, RD, etc.)
   - Data requirements
   - Key threats to identification
   - Closest existing papers

4. **Flag the most promising question** with rationale:
   - Novelty relative to existing literature
   - Data feasibility
   - Identification credibility
   - Policy relevance

5. **Save ideas** to `quality_reports/ideation_[sanitized_topic]_YYYY-MM-DD.md`

## Output Format

```markdown
# Research Ideation: [Topic]
**Date:** YYYY-MM-DD

## Starting Point
[What we're building from]

## Research Questions

### RQ1: [Question]
- **Type:** Descriptive / Causal / Welfare
- **Hypothesis:** [Testable prediction]
- **Identification strategy:** [How to credibly answer this]
- **Data needed:** [What you'd need]
- **Key threats:** [What could go wrong]
- **Closest papers:** [Author (Year)]

[Repeat for 3-5 questions]

## Most Promising Direction
[Which question and why — novelty, feasibility, identification]

## Quick Literature Check
[5-10 most relevant papers with one-line summaries]
```
