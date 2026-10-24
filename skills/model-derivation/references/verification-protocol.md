# Verification protocol for model-derivation

## Check A — units and homogeneity

Assign each symbol its unit from `model_setup.tex` (goods, dollars, dollars per unit, acre-feet,
shares, rates per period). Verify units(LHS) = units(RHS) after the step. Where units are
abstract, check the homogeneity degree instead: if the problem is homogeneous of degree one in
prices, a demand function must be homogeneous of degree zero in prices and income. Record
`PASS: [unit] = [unit]` or the mismatch.

## Check B — limiting cases

For each flagged step pick at least two limits that economic logic pins down, for example:

| Situation | Limit | What must happen |
|---|---|---|
| Borrowing or collateral constraint | multiplier to 0 (slack) | first-best condition returns |
| Friction, tax, trade cost | to 0 | frictionless allocation returns |
| CES elasticity σ | to 1 | Cobb-Douglas form |
| CES elasticity σ | to ∞ | perfect substitutes, corner or linear form |
| Discount factor β | to 0 | static choice |
| Heterogeneity | one type | representative-agent result |
| Share parameter α | to 0 or 1 | the corresponding input drops out |

Use SymPy `limit` where the expression is closed form. Record each limit, the result, and whether
it matches.

## Check C — SymPy and numeric spot-check

Write every check into `checks.py` so it can be re-run:

```python
import sympy as sp
k, theta, w, r = sp.symbols("k theta w r", positive=True)
lhs = ...   # expression before the step
rhs = ...   # expression after the step
assert sp.simplify(lhs - rhs) == 0, "Step 4 does not hold"
```

For FOCs and equilibrium conditions, solve for the endogenous variables at a parameter vector first,
then evaluate both sides there. Use at least two parameter vectors, one interior and one near a
boundary, and a tolerance of 1e-8 relative for closed forms.

Default parameter vectors (replace with the project's calibration when it exists):

| Parameter | Interior | Near boundary |
|---|---|---|
| β (annual) | 0.96 | 0.99 |
| α (capital share) | 0.33 | 0.05 |
| σ (CES elasticity) | 2.0 | 1.05 |
| δ (depreciation) | 0.08 | 0.01 |
| θ (pledgeability) | 0.5 | 0.95 |
| risk aversion | 2.0 | 0.5 |
| interest rate | 0.04 | 0.001 |

For a sign claim, evaluate the derivative on a grid of at least 50 random parameter vectors inside
the stated domain and report the share with the claimed sign. Anything below 100% means the sign is
conditional: find and state the condition.

## Blind re-derivation prompt (fresh subagent)

```
You are independently verifying derivations in an economic model. You have not seen the author's
derivation. Derive each claim yourself from the model setup below, one operation per line,
without skipping steps. You may use Python with SymPy to check algebra.

MODEL SETUP:
[contents of model_setup.tex]

CLAIMS:
Claim 1: Starting from [equations/assumptions], applying [operation], the result is: [equation]
...

For each claim return:
CLAIM N; DERIVATION (numbered steps); VERDICT: AGREE | DISAGREE | AMBIGUOUS;
if DISAGREE: the step where your path diverges, the author's expression, yours, and why;
if AGREE: any assumption you needed that the setup does not state;
for sign claims: the sign and every condition it requires.
```

At most five claims per call. Do not attach or paste `derivation.tex`.

## Halt protocol

1. Stop at the first failure.
2. Show the step, the check that failed, and both versions side by side.
3. Re-run SymPy on the disputed step to settle which version is right.
4. Back up `derivation.tex`, correct it, and re-run checks A-C on the corrected step and on every
   later step that cites it.
5. Record the halt and its resolution in `verification_log.tex`.
