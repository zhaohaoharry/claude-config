---
name: interview-me
description: Interactive interview to formalize a vague research idea into a structured specification with a clear research question, identification strategy, and next steps.
argument-hint: "[topic or 'I have an idea about X']"
allowed-tools: ["Read", "Write"]
---

# Interview Me

Conduct an interactive interview to formalize a research idea into a structured specification.

**Input:** `$ARGUMENTS` — a vague description of the idea.

## Protocol

1. **Start by listening.** Ask the user to describe the idea in their own words. Do not interrupt or offer suggestions yet.

2. **Ask clarifying questions** one at a time (not a list — conversation style):
   - What is the key phenomenon or puzzle you're trying to explain?
   - What is the ideal experiment that would answer this?
   - What real-world variation could serve as a natural experiment?
   - Who is affected and what is the outcome you care about?
   - What is the closest existing paper and how does yours differ?

3. **Synthesize** after each answer. Reflect back what you heard before asking the next question.

4. **Identify what's still missing:**
   - Identification strategy
   - Data source
   - Key threat to identification
   - Contribution relative to literature

5. **Draft the structured specification** at the end:
   ```markdown
   ## Research Idea: [Working Title]
   **Date:** YYYY-MM-DD

   ### The Question
   [One sentence: what causal effect or phenomenon]

   ### The Motivation
   [Why this matters — policy, theory, empirical puzzle]

   ### Identification Strategy
   [How to credibly answer the question]

   ### Data
   [What data is needed]

   ### Key Threats
   [What could go wrong with the identification]

   ### Contribution
   [How this differs from closest existing papers]

   ### Next Steps
   1. [First concrete action]
   2. [Second concrete action]
   ```

6. **Ask user to approve** the specification before saving.

7. **Save** to `quality_reports/specs/YYYY-MM-DD_[working-title].md`
