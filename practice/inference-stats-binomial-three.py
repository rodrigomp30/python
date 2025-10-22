import numpy as np
import pandas as pd
from scipy import stats

# Step 1: Simulate data (or load from PostgreSQL: df = pd.read_sql(...); successes = df['clicked'].sum(); n = len(df))
np.random.seed(707)  # For reproducibility
n = 1000  # Total impressions
benchmark_p = 0.025  # 2.5% expected
observed_p_param = 0.032  # Parameter for sim
successes = np.random.binomial(n, observed_p_param)  # 32 successes

# Actual observed rate
actual_observed_p = successes / n

binom_result = stats.binomtest(successes, n, benchmark_p, alternative='greater')

# Z-score (deviation measure)
standard_error = np.sqrt(benchmark_p * (1 - benchmark_p) / n)
z_score = (actual_observed_p - benchmark_p) / standard_error

# Step 3: 95% CI (built-in for exactness)
ci_lower, ci_upper = binom_result.proportion_ci(confidence_level=0.95)

# Step 4: Proportion difference (effect size)
proff_diff = actual_observed_p - benchmark_p


print(f'Benchmark: {benchmark_p:.3f}')
print(f'Actual: {actual_observed_p:.3f}')

print(f'\nZ-score: {z_score:.3f}')
print(f'P-value: {binom_result.pvalue:.3f}')

print(f'\nCI: {ci_lower:.3f} - {ci_upper:.3f}')
print(f'Effect Size: {proff_diff:.3f}')

# Null Hypothesis
# The observed proportion equals the benchmark (2.5% ad click rate), so the new creative makes no difference.

# How much does the observed proportion deviate from the benchmark?
# Z-score = 1.620, below the typical threshold (~1.96 for 95% confidence)
# showing a modest deviation from the expected 2.5%—
# this supports the null hypothesis of no clear improvement in clicks at MasterClass.

# How likely is this result due to chance?
# p-value = 0.069, above the 0.05 threshold, 
# confirming these results are likely due to random chance—no reliable increase yet.

# What is the range of the true proportion (95% confidence interval)?
# Observed rate = 3.3% (33/1,000 successes), CI = 0.024 (2.4%) to 1.000 (100%)
# The range crosses the 2.5% benchmark, so the true rate could be lower, equal, or higher—too uncertain.

# How strong is the difference?
# Proportion difference = +0.8% (3.3% - 2.5%) falls in the small range.
    # Under 0.5%: Negligible (ignore unless huge sample).
    # 0.5-1.5%: Small (worth exploring, noticeable impact).
    # Over 1.5%: Medium (scale for real gains).
# The creative increases clicks in a very small way—other factors (e.g., platform) likely matter more.

# What direction should we take based on these results?
# With 3.3% observed rate (vs. 2.5% benchmark, n=1,000 impressions),
# no reliable difference—retest with 2,000 impressions to narrow the CI, potentially uncovering a 0.5-1% gain
# for 3-5% more sign-ups and $5K MRR, aligning with B2C SaaS benchmarks for ad tweaks.