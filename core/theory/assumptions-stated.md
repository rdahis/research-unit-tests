---
id: theory-assumptions-stated
name: "Theory: All model assumptions stated explicitly"
methodology:
  - theory
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [theory, assumptions, model, transparency]
author: rdahis
version: 1
---

## What to Check

Every theoretical model rests on assumptions. These must be stated explicitly, labeled (Assumption 1, 2, …), and placed before they are used. Assumptions hidden in prose, implied by notation, or introduced mid-proof create ambiguity about what the model actually assumes and make it impossible to assess which results depend on which assumptions.

## How to Check

1. Read through the model setup section. Are assumptions labeled and enumerated?
2. Check that each assumption is stated in a self-contained way — a reader should be able to understand the assumption without inferring it from context.
3. For each main result (proposition, theorem, lemma), check whether the required assumptions are stated in the theorem or referenced explicitly. A result that says "under mild regularity conditions" without naming those conditions fails.
4. Check whether the paper discusses which assumptions are critical (the result fails without them) versus which are made for tractability (results likely extend without them). The distinction matters for the paper's contribution.
5. Flag assumptions that are stated but implausible in the paper's context — e.g., assuming perfect information in a model of adverse selection.

## Pass Condition

All assumptions are labeled, stated precisely, and referenced in the relevant results. Critical assumptions are distinguished from tractability assumptions. The model section could be understood by a reader without reading the introduction.

## Failure Examples

1. **Assumption in prose only**: "We assume firms cannot observe worker ability." This restriction is stated in the text but not labeled as an assumption. Later proofs invoke it without reference. Fails — not findable or traceable.
2. **"Standard regularity conditions"**: Proposition 2 states "under standard regularity conditions, the equilibrium is unique." The regularity conditions are not stated anywhere in the paper. Fails — the result is not verifiable.
3. **Assumption introduced mid-proof**: A key monotonicity condition appears for the first time in the proof of Lemma 3, not in the model setup. Fails — assumptions must precede the results that depend on them.

## Notes

- This test does not assess whether assumptions are reasonable — only that they are stated. Reasonableness is evaluated by `theory-assumptions-discussed`.
- In applied theory papers where the model is a well-known workhorse (e.g., standard principal-agent, Hotelling), assumptions that are standard to that framework need not be re-stated in full, but departures from the standard version must be.
