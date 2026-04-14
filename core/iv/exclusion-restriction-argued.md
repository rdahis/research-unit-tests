---
id: iv-exclusion-restriction-argued
name: "IV: Exclusion restriction explicitly argued"
methodology:
  - iv
scope:
  - paper
  - proposal
severity: blocker
clarity: judgment
tags: [identification, exclusion-restriction, instrument-validity]
author: rdahis
version: 1
---

## What to Check

The exclusion restriction — that the instrument affects the outcome only through the endogenous variable, not through any other channel — cannot be tested. It must be argued. A paper that uses an IV without an explicit, credible argument for the exclusion restriction is unacceptable regardless of the statistical results.

## How to Check

1. Locate the argument for the exclusion restriction in the paper. It should appear in the identification or data section, typically after introducing the instrument.
2. Evaluate the argument on three dimensions:
   - **Specificity**: Does the paper name the specific channel through which the instrument could violate the exclusion restriction, and then argue why that channel is closed or negligible?
   - **Credibility**: Is the argument economic/institutional (how the world works), or merely a claim that "we cannot think of any other channel"? The former is strong; the latter is weak.
   - **Engagement with critics**: Does the paper anticipate and address the most obvious objections to the exclusion restriction?
3. Check whether the paper provides any partial tests of the exclusion restriction (overidentification tests where applicable, or reduced-form evidence on placebo outcomes that should not be affected).

## Pass Condition

The paper provides a specific, economically grounded argument for why the instrument satisfies the exclusion restriction, names the most plausible violations, and explains why they are unlikely or have been addressed.

## Failure Examples

1. **No argument given**: Paper introduces rainfall as an instrument for agricultural income. The only statement is "we use rainfall as an instrument, following Smith (2015)." No argument for why rainfall affects the outcome only through agricultural income. Fails — rainfall could affect health, migration, crime, and many other outcomes directly.
2. **Circular argument**: "We believe the instrument is valid because the first stage is strong." First-stage strength is instrument relevance, not the exclusion restriction. These are separate conditions. Fails.
3. **Generic disclaimer**: "Like all IV strategies, our results rely on the exclusion restriction, which by construction cannot be tested." This acknowledges the condition but makes no argument for why it holds. Fails.

## Notes

- In just-identified IV (one instrument), the exclusion restriction is not testable. In overidentified IV (more instruments than endogenous variables), Sargan-Hansen J-tests provide a partial check — but passing them is not sufficient evidence for validity.
- Some instruments have well-known threats to exclusion that the literature has extensively debated (e.g. proximity-to-college IV, rainfall instruments). Papers using these instruments must engage with the specific critique literature.

## References

- Bound, J., Jaeger, D. A., & Baker, R. M. (1995). Problems with instrumental variables estimation when the correlation between the instruments and the endogenous explanatory variable is weak. *Journal of the American Statistical Association*, 90(430), 443–450.
- Angrist, J. D., & Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton University Press. Chapter 4.
