import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import chi2

data = {
    'merchant_type': np.random.choice(['small', 'large'], 100, p=[0.5, 0.5]),
    'high_value': np.random.choice([0, 1], 100, p=[0.5, 0.5])  # Balanced
}
df = pd.DataFrame(data)

contingency = pd.crosstab(df['merchant_type'], df['high_value'])

chi2_stats, p_value, dof, expected = chi2_contingency(contingency.values)

critical_value = chi2.ppf(0.95, dof)

cramers_v = np.sqrt(chi2_stats / (contingency.astype(float).values.sum() * (min(contingency.shape) - 1)))

print(f'Chi2: {chi2_stats:.3f}')
print(f'Critical value: {critical_value:.3f}')
print(f'P-value: {p_value:.3f}')
print(f'Cramérs V: {cramers_v:.3f}')


# Null Hypothesis
# The variables in this analysis are independent, so there is no association between them.

# How much does the observed value deviate from the expected?
# chi2 = 0.362 (df=1), well below the critical value threshold of ~3.841
# showing no evidence of deviation from what we'd expect in an independent relationship between the variables.

# How likely is this result due to chance?
# p-value = 0.547, far above the 0.05 threshold, 
# confirming these results are likely due to random chance.

# How strong is the connection?
# Cramér's V = 0.060 falls under 0.10: Negligible (ignore unless huge sample).
# This reinforces that merchant type does not influence high values.

# What direction should we take based on these results?
# As the results show no association between these variables, proceed to the next test.
# Assume there's nothing to invest in this relationship—reallocate to association tests related to industry type, business model, or even target department size.
# This keeps our focus on segments that could lift qualified leads by 5-10% in our B2B campaigns.