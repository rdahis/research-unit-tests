---
id: theory-results-proven
name: "Theory: Main results formally proven, not just stated"
methodology:
  - theory
scope:
  - paper
severity: blocker
clarity: deterministic
tags: [theory, proofs, propositions, formal]
author: rdahis
version: 1
---

## What to Check

Propositions, theorems, and lemmas in a theory paper must be formally proven. A result stated without proof, or with a proof that is incomplete or circular, does not constitute an established result. Proofs may appear in the main text or in an appendix, but they must exist and be complete.

## How to Check

1. List all labeled results: propositions, theorems, lemmas, corollaries.
2. For each result, verify that a proof is provided — either immediately following the result or in a clearly referenced appendix.
3. Evaluate proof completeness at a high level:
   - Does the proof address all cases the result claims to cover?
   - Are all steps that require justification actually justified, or do steps appear as "it follows that…" without explanation?
   - Does the proof use only assumptions stated in the model and previously established results?
4. Check for results labeled "intuition" or "sketch" — these are not proofs. If the formal proof is deferred ("proof in supplementary appendix"), verify the supplementary appendix is actually provided.

## Pass Condition

Every labeled result (proposition, theorem, lemma) has a complete proof in the main text or appendix. No result is established only by intuition, example, or simulation (unless the paper explicitly says the result is a conjecture).

## Failure Examples

1. **No proof provided**: Paper states "Proposition 2: The equilibrium wage is increasing in worker ability." No proof follows and no appendix reference. Fails.
2. **Proof by example**: Paper demonstrates a result holds for a specific parameterization and calls it proven. An example demonstrates possibility, not generality. Fails.
3. **Circular proof**: Proof of Proposition 1 invokes "the result of Proposition 2," which is stated later. If Proposition 2's proof also depends on Proposition 1, the argument is circular. Fails.
4. **"Sketch" only**: Paper provides a "proof sketch" with key steps but defers the full proof to "a technical appendix available from the authors." The appendix is not attached to the submitted paper. Fails.

## Notes

- Computational or quantitative theory papers that characterize equilibria numerically should clearly state which results are analytical (proven) and which are established by simulation. Simulation-based results are not proofs — they are quantitative illustrations.
- Corollaries that follow directly from propositions by substitution or inspection can have shortened proofs, but must state what they follow from.
