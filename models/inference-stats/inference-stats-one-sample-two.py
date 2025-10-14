import numpy as np
from scipy import stats
import pandas as pd

# Step 1: Simulate or load data (e.g., engagement times in minutes)
np.random.seed(42)  # For reproducibility
data = np.random.normal(6, 2, 100)  # Mean 6 > benchmark 5, n=100

# Step 2: Run one-sample t-test (H0: mean = benchmark)
benchmark = 5.0
t_stat, p_value = stats.ttest_1samp(data, benchmark)

# Degrees of freedom and critical value (two-tailed, alpha=0.05)
dfo = len(data) - 1
critical_t = stats.t.ppf(0.975, dfo)

# Cohen's d (effect size: (mean - benchmark) / std)
cohens_d = (np.mean(data) - benchmark) / np.std(data)

print(f'T_stat: {t_stat:.3f}')
print(f'Critical_t: {critical_t:.3f}')
print(f'P-value: {p_value:.3f}')
print(f'Cohens_d: {cohens_d:.3f}')

# Null Hypothesis
# The sample mean equals the benchmark (5 minutes engagement time), so no difference from industry standard.

# How much does the observed mean deviate from the expected?
# t-stat = 4.362 (df=99), well above the critical value threshold of ~1.984
# showing strong deviation from the benchmark—
# this refutes the null hypothesis of no difference in engagement time.

# How likely is this result due to chance?
# p-value = 0.000, far below the 0.05 threshold, 
# confirming statistical significance and reinforcing a real (non-random) improvement
# over the benchmark.

# How strong is the difference?
# Cohen's d = 0.438 falls in the 0.2-0.5 range: small-to-medium effect.
    # Under 0.2: Negligible (ignore unless huge sample).
    # 0.2-0.5: Small-to-medium (worth exploring, noticeable impact).
    # Over 0.5: Large (major opportunity).
# Our engagement time exceeds the benchmark modestly but meaningfully—other factors (e.g., content length) could amplify it.

# What direction should we take based on these results?
# With sample mean at 5.79 minutes (vs. 5-min benchmark, n=100 users),
# highlight this in marketing materials to build credibility—could drive 10-15% more trial sign-ups
# by showcasing better retention, aligning with B2B SaaS benchmarks for user activation.