---
name: econ-introduction
description: Design, diagnose, draft, or rewrite the intellectual architecture of an economics-paper introduction across empirical, structural, theory, and macro work. Use for any substantive economics-paper writing task that affects the research question, opening motivation, framing, contribution, main-results narrative, mechanism, or general-interest claim. Establish the introduction contract before applying econ-craft or journal-fit; use aer-introduction additionally for AER-family format requirements.
---

# Economics Introduction

Build the introduction around one consequential question and an evidence-bounded answer. Treat the introduction as the paper's contract with the reader. Later sections should deepen that contract rather than accumulate outcomes and checks.

## Scope and precedence

This skill governs the argument's architecture and the reader's beliefs. It does not replace:

- `econ-craft`, which controls sentence-level flow, rhythm, voice, intuition, and magnitudes;
- `journal-fit`, which adapts the argument to a target journal;
- `aer-introduction`, which supplies AER-family formatting and abstract constraints;
- `aer-identification` or `econometrics-playbook`, which assesses or implements identification.

For substantive manuscript writing outside the introduction, first check whether the new passage changes the paper's question, main claim, mechanism, interpretation, or contribution. If it does, update the introduction contract before polishing the local prose. Purely local exposition can proceed directly to `econ-craft`.

## Workflow

### 1. Inspect the live paper

Read enough of the current manuscript, design, results, and project state to distinguish what the paper proves from what the author hopes it means. Preserve existing claims, citations, numbers, and revision-mark rules unless the user authorizes substantive changes. Do not add a citation or bibliography entry merely to decorate the opening.

Identify the paper type and load the corresponding architecture from `references/architectures.md`.

### 2. Write the paper contract

Before drafting paragraphs, write one private working sentence with three parts:

`This paper asks [consequential question], answers [result or mechanism] using [credible source of discipline], and thereby changes what we know about [broader economic problem].`

The contract is not boilerplate for the manuscript. It is a test. Each substantive introduction paragraph must earn one part of it.

A strong research question asks for an economically meaningful object whose answer is not already settled. Prefer magnitude, mechanism, incidence, equilibrium consequence, boundary condition, or policy tradeoff over a binary question with a predictable answer. A binary question remains valid when the sign itself is genuinely unresolved.

### 3. Test the general-interest ceiling

Run the six tests in `references/diagnostics.md`. In particular, remove the empirical setting mentally. The motivating question should still matter. Then restore the setting and explain why it supplies unusually sharp leverage on that question.

Distinguish three levels of contribution:

1. a new fact in one setting;
2. an explanation or mechanism that may travel across settings;
3. evidence that changes a canonical calculation, resolves a recognized contradiction, or reorganizes an established literature.

Claim the highest level the evidence can support, not the highest level the prose can imply. State the boldest responsible interpretation and identify the additional test that would make a stronger interpretation credible.

### 4. Model the reader's first reaction

Before adding detail, ask what a skeptical economist will decide in the first page:

- Why should I care?
- Is this answer already obvious?
- Does the design identify the claim being made?
- Is the setting doing intellectual work or merely supplying data?
- Is the author inflating a local fact into a universal mechanism?

Classify likely objections as fatal, claim-limiting, or local. Fix fatal objections in the design or central claim. Narrow overbroad claims. Handle only the most salient local objection in the introduction when the answer is short and decisive. Do not add a defensive paragraph for every imaginable criticism. More text usually increases suspicion when it delays the design, result, or economic meaning.

### 5. Build the paragraph sequence

Use the paper-type sequence in `references/architectures.md`, then adjust it to the actual argument. For a reduced-form empirical paper, the default sequence is:

1. Big-picture problem, precise knowledge gap, and research question. Usually one-third to one-half page. Use only the canonical citations needed to locate the problem.
2. What the paper does and why the variation or instrument can answer the question. Give the identification intuition, not the full data and estimator description.
3. Main findings. Report economic magnitudes and explain what they imply for the research question. Do not march through "we find A, we also find B."
4. Mechanism, heterogeneity, and extensions. Include only analyses that discriminate among explanations, establish scope, or change the interpretation. Usually no more than four paragraphs in total.
5. Literature and value added. Use one or two paragraphs to explain what becomes known because of the paper. A topical contrast such as "prior work studies X, while we study Y" is not a contribution.
6. A short roadmap when the journal or paper length warrants one.

Do not force a paragraph count when the paper type requires a different order. The sequence is a belief-changing progression, not a template to fill.

### 6. Draft for cumulative meaning

Every paragraph should change one reader belief. Every sentence should add one necessary layer, such as a premise, contrast, causal link, implication, piece of evidence, or transition from the general question to the empirical leverage.

Use medium-length, cumulative economics prose. Avoid both clause-stacked sentences and strings of short aphorisms. Do not write slogan-like fragments such as "Information travels upward. Influence does too." A short verdict is useful only when it completes a developed argument.

Keep the level of abstraction stable. Name the principal, agent, institution, margin, or distortion when those objects carry the economics. Connect abstract stakes to a concrete decision quickly. Use one name per concept, and let given information lead to new information.

Use citations as intellectual anchors, not as a carpet. The opening normally needs only the canonical sources that establish the broad problem or competing view. Verify any paper before characterizing it.

### 7. Revise by subtraction

Cut material that does not advance the contract:

- broad claims that never reach the research question;
- mini literature reviews in the opening;
- repeated statements of why the setting is useful;
- robustness inventories without interpretive value;
- caveat stacks that do not alter the claim;
- contribution lists that name topics instead of new knowledge;
- roadmap language embedded in substantive paragraphs.

When a criticism is valid, prefer changing the claim, design, or order of exposition over adding qualifications around the same sentence.

### 8. Apply the prose and project rules

After the architecture is sound, apply `econ-craft` and the project's academic-writing guide. Apply `journal-fit` when a target journal is named. Preserve visible track changes when the project requires them, compile after substantive LaTeX edits, and inspect the rendered PDF before declaring the revision complete.

## Output modes

Match the user's requested action:

- **Diagnose or evaluate:** report the current contract, the highest-ceiling defensible claim, the two or three structural weaknesses, and a proposed paragraph map. Do not edit.
- **Draft or rewrite:** supply or apply replacement prose. Preserve facts and flag any missing evidence that constrains the framing.
- **Reframe:** revise the contract first, then propagate it through the opening, results interpretation, mechanisms, and contribution paragraphs so the introduction tells one argument.
- **Local section edit:** state whether the edit changes the contract. If it does, align the introduction and affected section; if it does not, keep the intervention local.

## Final self-check

Before saving or presenting prose, verify that:

- a nonspecialist economist can repeat the central claim in one sentence;
- the question matters without the empirical setting, and the setting provides distinctive leverage;
- the paper answers a nontrivial quantity, mechanism, incidence, or tradeoff;
- the design supports the breadth of the claim;
- the main result includes magnitude and meaning;
- mechanisms and extensions escalate the same argument;
- the literature discussion states what is newly learned;
- the introduction anticipates the dominant objection without sounding defensive;
- no paragraph exists only because an outline said it should;
- no sentence is merely a slogan, a list transition, or a hedge around missing substance.
