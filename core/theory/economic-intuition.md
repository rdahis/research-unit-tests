---
id: theory-economic-intuition
name: "Theory: Economic intuition provided for main results"
methodology:
  - theory
scope:
  - paper
severity: warning
clarity: judgment
tags: [theory, intuition, exposition, communication]
author: rdahis
version: 1
---

## What to Check

A theory paper must explain why its results hold — not just prove that they hold. Formal proofs establish truth; economic intuition establishes understanding. A paper that proves results without explaining the economic mechanism contributes less than one that makes the mechanism clear. Referees and readers should be able to explain the main results in words after reading the paper.

## How to Check

1. For each main proposition or theorem, check whether the paper provides a verbal explanation of the mechanism: why does the result hold, what forces drive it?
2. Evaluate the quality of the intuition:
   - **Good**: The intuition names the economic forces and explains their direction and magnitude. Example: "The result holds because the substitution effect dominates the income effect when elasticity exceeds one."
   - **Weak**: The intuition restates the math in words without adding insight. Example: "The result holds because the derivative of the value function is positive."
   - **Absent**: The result is stated, proved, and the paper moves on.
3. Check whether the paper uses illustrative examples, figures, or special cases to build intuition before or after the general result.
4. For comparative statics, check whether the direction of each effect is explained economically, not just signed.

## Pass Condition

Each main result is accompanied by a verbal explanation of the economic mechanism that adds insight beyond the formal proof. At least one illustrative example or special case supports the intuition.

## Failure Examples

1. **Math restated as words**: After proving that equilibrium wages increase in ability, the paper writes "intuitively, the wage is higher when ability is higher." This is a restatement, not an explanation of mechanism. Fails.
2. **No intuition section**: Paper proves five propositions and proceeds immediately to welfare analysis. No prose between the proofs explains what drives the results. Fails.
3. **Intuition contradicts proof**: Paper provides an intuitive explanation that is actually inconsistent with the proof (a different mechanism than what the math shows). This is worse than no intuition — it misleads the reader. Fails.

## Notes

- Severity is `warning` rather than `blocker` because the formal content of the paper (assumptions + proofs) is valid without the intuition. But a theory paper without good intuition will face referee objections and should be flagged.
- For papers in technical sub-fields where the audience is specialists, the intuition may be brief and notation-heavy. The standard is whether a well-trained economist outside the sub-field can follow the argument.
