---
id: universal-effect-size-magnitude
name: "Effect sizes reported with economic significance assessment"
methodology:
  - universal
scope:
  - paper
severity: blocker
clarity: heuristic
tags: [effect-size, economic-significance, magnitude, interpretation]
author: rdahis
version: 1
---

## What to Check

Statistical significance establishes that an effect is distinguishable from zero; it says nothing about whether the effect is large or small in an economically meaningful sense. Papers must report effect sizes in interpretable units and assess whether the magnitudes are economically significant — large enough to matter for the phenomena under study.

## How to Check

1. Check that effect sizes are reported in interpretable units:
   - For continuous outcomes: report the raw coefficient (e.g., "wages increase by $120/month") AND a standardized or percent effect relative to the control mean or baseline.
   - For binary outcomes: report marginal effects, not just log-odds or probit index coefficients.
   - For log-log specifications: coefficients are elasticities — state this explicitly.
2. Check that the control mean (or baseline mean) is reported in or near the main regression table. Without it, raw coefficients cannot be interpreted as percent changes.
3. Assess economic significance: is the estimated effect large enough to matter?
   - Compare the effect to the existing cross-sectional variation in the outcome.
   - Compare to the cost of treatment (cost-effectiveness).
   - Compare to effects found in prior literature for related interventions.
   - Compare to policy-relevant thresholds (e.g., "the effect is larger than the gender wage gap in this context").
4. Flag papers that report only t-statistics or stars without discussing whether magnitudes are plausible or meaningful.

## Pass Condition

Effect sizes reported in raw and relative (percent or SD) units. Control mean present. At least one sentence assessing whether the magnitude is economically significant with a concrete comparator.

## Failure Examples

1. **Coefficient without baseline**: Table shows a coefficient of 0.023 on a continuous outcome. No control mean anywhere in the paper. Is 0.023 large or small? Impossible to say. Fails.
2. **Stars only**: Table has three columns of asterisks and a footnote "*p<0.10, **p<0.05, ***p<0.01." No discussion of magnitudes in the text. Fails.
3. **Statistical significant but economically trivial, not discussed**: A large-N study finds that a policy reduces crime by 0.003 events per 100,000 population (p < 0.001). The paper does not note that this is approximately zero relative to crime rates in the study area. Fails.
4. **Significant and large but not benchmarked**: A training program increases earnings by 40%. The paper reports this without comparing to the cost of the program, prior evaluations, or the baseline earnings level. Plausible range not established. Fails.

## References

- Ioannidis, J. P., Stanley, T. D., & Doucouliagos, H. (2017). The power of bias in economics research. *Economic Journal*, 127(605), F236–F265.
- Ziliak, S. T., & McCloskey, D. N. (2008). *The Cult of Statistical Significance*. University of Michigan Press.
