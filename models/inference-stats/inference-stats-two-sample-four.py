import numpy as np
import pandas as pd
from scipy import stats

# Step 1: Create DataFrame (simulated MasterClass A/B on pricing conversion rates; replace with real data)
np.random.seed(202)  # For this exercise
group_a = np.random.beta(0.15, 1.2, 100) * 100  # Variant A: Emotional copy, ~12% mean (beta for 0-100% rates)
group_b = np.random.beta(0.09, 1.1, 100) * 100  # Variant B: Feature copy, ~8% mean

df = pd.DataFrame({
    'user_id': range(1, 201),
    'variant': ['A'] * 100 + ['B'] * 100,
    'conversion_rate': np.concatenate([group_a, group_b])
})

# Step 2: Run two-sample t-test (H0: means equal)
group_a_data = df[df['variant'] == 'A']['conversion_rate']
group_b_data = df[df['variant'] == 'B']['conversion_rate']

t_stat, p_value = stats.ttest_ind(group_a_data, group_b_data, equal_var=True)

# Degrees of freedom and critical value (two-tailed, alpha=0.05)
dof = df_freedom = len(group_a_data) + len(group_b_data) - 2
critical_t = stats.t.ppf(0.975, dof)

# Cohen's d (pooled std)
pooled_std = np.sqrt(((len(group_a_data)-1)*np.var(group_a_data) + (len(group_b_data)-1)*np.var(group_b_data)) / dof)
cohens_d = (group_a_data.mean() - group_b_data.mean()) / pooled_std

# Step 3: Print results
print(f'mean A: {group_a_data.mean():3f}')
print(f'mean B: {group_b_data.mean():.3f}')
print(f't_stats: {t_stat:.3f}')
print(f'critical_t: {critical_t:.3f}')
print(f'p_value: {p_value:.3f}')
print(f'cohens_d: {cohens_d:.3f}')

# Null Hypothesis
# The means of the two groups are equal (no difference in conversion rates between emotional and feature-focused pricing copy), so variants perform the same.

# How much do the observed means deviate from each other?
# t-stat = 1.603 (df=198), below the critical value threshold of ~1.972
# showing no strong deviation between groups—
# this supports the null hypothesis of no clear difference in funnel performance at MasterClass.

# How likely is this result due to chance?
# p-value = 0.110, above the 0.05 threshold, 
# confirming these results are likely due to random chance—no standout variant yet.

# How strong is the difference?
# Cohen's d = 0.228 falls in the under 0.2 range: negligible effect.
    # Under 0.2: Negligible (ignore unless huge sample).
    # 0.2-0.5: Small-to-medium (worth exploring, noticeable impact).
    # Over 0.5: Large (clear opportunity to scale).
# Differences are negligible between variants—other factors (e.g., traffic source) likely play a bigger role.

# What direction should we take based on these results?
# With Variant A at 13.31% vs. B at 8.25% (n=100 per group),
# no significant difference—pivot to test mobile vs. desktop views or add more data for a potential 5% lift,
# aligning with B2C SaaS benchmarks for funnel optimization.

# Refining Your Recommendation: Increasing Sample Size for Precision and Power

# You're on the right track with suggesting a larger sample size—it's a smart, 
# practical next step when you have a non-significant result 
# like your p=0.110 and small Cohen's d=0.228. But let's clarify one nuance to make it even stronger: 
# Boosting the number of users (n) doesn't aim to "shrink" the effect size 
# (d stays around the true value, like your ~0.23 hint of a 5% conversion edge). 
# Instead, it sharpens the estimate—making d more precise (tighter confidence interval) 
# and boosting your "power" (chance of spotting a real difference if it exists). 
# In a B2C SaaS like MasterClass, this avoids false negatives: 
# Your current n=100/group might miss a modest win that could still add $5K MRR from better pricing copy, 
# but with n=300, you'd confirm or rule it out reliably.