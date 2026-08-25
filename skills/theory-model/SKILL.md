---
name: theory-model
description: Build the smallest theoretical model that generates an empirical result you already have — for the "what is the model?" referee demand, for turning a reduced-form estimate into a signed comparative static, or for deciding whether a paper needs a model at all. Works backward from findings to a minimal framework. Use after results exist, not to generate a new research idea (that is research-ideation) and not to choose an estimator (that is econometrics-playbook).
argument-hint: "[the empirical result, e.g. 'water price rise cut perennial acreage 8%' or a results-section path]"
allowed-tools: ["Read", "Grep", "Glob", "Write"]
---

# theory-model — the smallest model that explains what you found

An AER or JEEM referee asks "what is the model?" for one of two reasons, and they need different answers. Either the empirical result is uninterpretable without a framework that signs the effect, or the paper claims a mechanism it has not disciplined. This skill builds the minimum needed to answer, working **backward from the estimate you already have**.

It does not invent theory for its own sake. A model that does not change how a reader interprets the empirical work is a liability: it adds notation, invites a theory referee, and earns nothing.

## First, decide whether the paper needs a model at all

Answer these before writing a single equation. If the honest answer to all four is no, say so and stop — recommending no model is a legitimate and often correct output of this skill.

1. **Does the sign of the effect depend on a parameter the reader cannot guess?** If a rational reader cannot predict the sign without a framework, a model earns its place.
2. **Is there a mechanism claim the data alone cannot separate?** Two channels predicting the same reduced-form sign need a model to be distinguished, or the mechanism claim must be dropped.
3. **Does the paper need to extrapolate?** Out-of-sample policy counterfactuals require structure. Within-sample descriptive claims do not.
4. **Is the referee's real objection about magnitude plausibility?** Sometimes "what is the model?" means "is this number too big to believe?" A back-of-envelope calibration answers that better than a formal model, and faster.

If the objection is really about identification, route to `aer-identification`. If it is about whether the effect is robust, route to `aer-robustness`. Neither is fixed by adding theory.

## Then build the smallest thing that works

**Start from the comparative static you need, and reverse-engineer toward it.** Write the target first, as a sentence: "an increase in *p* lowers *A*, and more so when σ is small." Everything in the model exists to deliver that sentence. Anything that does not is cut.

The build order:

1. **Name the agent and the choice.** One decision-maker, one margin. "A grower chooses acreage to allocate between perennial and annual crops." Resist adding a second agent until the first cannot carry the result.
2. **Write the objective and the constraint.** Both in words before either is in notation. If the intuition does not survive being said in a sentence, the model is wrong, not the sentence.
3. **Take the first-order condition and sign it.** This is the whole payoff. The comparative static must be the empirical object you actually estimated — not a cousin of it. A model that signs ∂A/∂p when the paper estimates a response to a quantity restriction has not answered the referee.
4. **Identify what the model says that the reduced form does not.** If nothing, the model is decorative. Cut it or make it earn its place with a testable auxiliary prediction.
5. **State the assumptions you are buying with.** Every simplification purchases tractability at a price. Name the price. Referees forgive strong assumptions that are acknowledged and punish strong assumptions that are hidden.

**Match the model's ambition to the empirical design.** A two-period model is enough to sign a dynamic response. A continuum of heterogeneous agents is not needed to generate heterogeneous effects if the paper only estimates an average. Adding generality that the data cannot test is the most common failure here, not the least.

## Anti-novelty guard — read this before proposing anything

The dominant failure mode of model-building with an LLM is a plausible-sounding, technically coherent, unpublishable model. It looks like theory, uses the right notation, and would not survive a seminar. Guard against it explicitly:

- **Prefer the canonical model.** If a standard framework in the field already generates your comparative static (Hotelling for extraction, Roy for selection, a two-sector allocation model, a simple principal-agent setup), use it and cite it. "This is the standard X model with Y added" is a strength, not a weakness. Novelty in the *model* is not the contribution of an empirical paper.
- **Do not invent a new mechanism.** If the mechanism is not already in the literature or in the institutional record, the model is speculating, not disciplining.
- **Every proof sketch needs the author's own check.** Treat the steps in this skill as prompts for judgment, never as verification. Do not assert that a result "follows" without the author confirming the algebra. Sign errors in comparative statics are easy to produce and expensive to publish.
- **If the model requires an assumption the setting contradicts, stop.** Report the conflict rather than assuming it away. An institutional fact that breaks the model is a finding about the model.

## Output

```text
NEEDS A MODEL: <yes — reason | no — what to do instead>
TARGET COMPARATIVE STATIC: <the signed statement, in words>
MATCHES THE ESTIMATE: <which empirical result this corresponds to, exactly>
CANONICAL BASE: <named model + citation, or "none — new setup, justify">
AGENT AND MARGIN: <who chooses what>
KEY ASSUMPTIONS AND THEIR PRICE: <list, each with what it buys and what it costs>
THE RESULT: <FOC, sign, and the intuition in one sentence>
WHAT THE MODEL ADDS: <what a reader learns that the reduced form alone does not>
AUXILIARY TESTABLE PREDICTION: <one, or "none — model is interpretive only">
UNVERIFIED STEPS: <every step the author must check by hand>
HANDOFF: aer-robustness (test the auxiliary prediction) | econ-introduction (fold the mechanism into the contract) | econ-craft (write the intuition before the notation)
```

## Important

1. **Work backward from results, never forward from a modeling impulse.** This skill runs after estimates exist.
2. **Intuition before notation, always.** The mechanism must be statable in one sentence a non-specialist follows. `AI_Writing_Guide_EconCraft.md` P9 and P11 govern how the model gets written up.
3. **Recommending no model is a valid answer**, and often the right one for a clean reduced-form paper.
4. **Never claim a comparative static you have not derived.** Mark every step the author must verify. A confidently wrong sign is worse than no model.
5. **Do not compete with `aer-identification`.** Theory disciplines interpretation; it does not rescue a design. If the identification is weak, the model cannot fix it and should not be used to distract from it.
6. **One margin until it fails.** Add complexity only when the simple version provably cannot generate the result.
