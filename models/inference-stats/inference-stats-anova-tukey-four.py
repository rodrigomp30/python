import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Step 1: Create DataFrame (simulated MasterClass A/B/C on test email open rates; replace with real data)
np.random.seed(404)  # For this exercise
group_a = np.random.normal(22, 5, 100)  # Variant A: Morning, ~22% mean
group_b = np.random.normal(20, 5, 100)  # Variant B: Afternoon, ~20% mean
group_c = np.random.normal(28, 6, 100)  # Variant C: Evening, ~28% mean

df = pd.DataFrame({
    'user_id': range(1, 301),
    'variant': ['A'] * 100 + ['B'] * 100 + ['C'] * 100,
    'open_rate': np.concatenate([group_a, group_b, group_c])
})

group_a_data = df[df['variant'] == 'A']['open_rate']
group_b_data = df[df['variant'] == 'B']['open_rate']
group_c_data = df[df['variant'] == 'C']['open_rate']

f_stat, p_value = stats.f_oneway(group_a_data, group_b_data, group_c_data)
tukey = pairwise_tukeyhsd(df['open_rate'], df['variant'], alpha=0.05)

# Step 4: Eta-squared (overall effect size)
overall_mean = df['open_rate'].mean()
ss_between = 100 * ((group_a_data.mean() - overall_mean)**2 + (group_b_data.mean() - overall_mean)**2 + (group_c_data.mean() - overall_mean)**2)
ss_total = df['open_rate'].var() * len(df)
eta_squared = ss_between / ss_total

# Step 5: Critical F for ANOVA
df_between = len(np.unique(df['variant'])) - 1  # 2
df_within = len(df) - len(np.unique(df['variant']))  # 297
critical_f = stats.f.ppf(0.95, df_between, df_within)

print(f'Mean A: {group_a_data.mean():.2f}')
print(f'Mean B: {group_b_data.mean():.2f}')
print(f'Mean C: {group_c_data.mean():.2f}')

print(f'F_stat: {f_stat:.3f}')
print(f'Critical_f: {critical_f:.3f}')
print(f'P_value: {p_value:.3f}')

print(f'\n{tukey}')
print(f'Eta_square: {eta_squared:.3f}')



# Applying It to Your Table (With Your Means)
# Using your means (A=22.56%, B=20.33%, C=28.77%), here's the correct read for each pair:

# A vs. B: meandiff = -2.23% (B - A = 20.33% - 22.56% = -2.23%). 
# Negative means A has the higher average than B by 2.23%. CI all negative (-3.98% to -0.48%) 
# confirms A is reliably higher (no zero cross). p-adj=0.008 <0.05 = real difference.

# A vs. C: meandiff = +6.22% (C - A = 28.77% - 22.56% = +6.22%). 
# Positive means C has the higher average than A by 6.22%. CI all positive (+4.46% to +7.97%) 
# confirms C is reliably higher. p-adj=0.000 <0.05 = real difference.

# B vs. C: meandiff = +8.45% (C - B = 28.77% - 20.33% = +8.45%). 
# Positive means C has the higher average than B by 8.45%. CI all positive (+6.69% to +10.20%) 
# confirms C is reliably higher. p-adj=0.000 <0.05 = real difference.

# Overall Picture: C has the highest average (28.77%), 
# A is second (22.56%), and B is lowest (20.33%). 
# All pairs are significant, with C pulling ahead of both A and B (CIs confirm no ties). 
# Your eta-squared=0.316 is a large effect, 
# meaning the thumbnails explain a good portion (~32%) of the click differences—strong reason to focus on C.


# Null Hypothesis
# The means of the three groups are equal (no difference in click-through rates across celebrity, scene, and text thumbnail styles), so variants perform the same.

# How much do the observed means deviate overall?
# ANOVA F-stat = 69.058 (df=2, 297), above the critical threshold of ~3.026
# showing a strong overall deviation among groups—
# this refutes the null hypothesis of no clear difference in preview performance at MasterClass.

# How likely is this result due to chance?
# ANOVA p-value = 0.000, far below the 0.05 threshold, 
# confirming statistical significance and reinforcing real (non-random) differences
# across thumbnail styles.

# How do pairs compare (Tukey follow-up, with 95% confidence intervals for gap reliability)?
# Significant pairwise differences (p-adj <0.05, confidence intervals showing reliable edges):
#   A vs. B: -2.23% gap, p-adj=0.008, CI -3.98% to -0.48% (negative range—reliable A edge over B).
#   A vs. C: +6.22% gap, p-adj=0.000, CI +4.46% to +7.97% (positive range—reliable C edge over A).
#   B vs. C: +8.45% gap, p-adj=0.000, CI +6.69% to +10.20% (positive range—reliable C edge over B).
# Variant C (text thumbnails) stands out as the better option, with tight confidence intervals confirming the gaps are not due to chance.

# How strong is the overall difference?
# Eta-squared = 0.316 falls in the over 0.06 range: large effect.
    # Under 0.01: Negligible (ignore unless huge sample).
    # 0.01-0.06: Small (worth exploring, subtle impact).
    # Over 0.06: Medium (scale the standout for real gains).
# Thumbnail styles differ in a large way overall—focus on C's edge for bigger retention plays.

# What direction should we take based on these results?
# With means A=22.56%, B=20.33%, C=28.77% (n=100 per group),
# roll out text thumbnails site-wide to lift video starts—reliable confidence intervals show +6-10% gains,
# potentially driving 10% more subscriptions and $15K MRR, aligning with B2C SaaS benchmarks for visual tweaks.