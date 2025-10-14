import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import chi2

np.random.seed(123)
data = {
    'content_type': np.random.choice(['video', 'blog'], 100, p=[0.6, 0.4]),
    'engaged': np.random.choice([0, 1], 100, p=[0.3, 0.7])  # Initial engaged
}
df = pd.DataFrame(data)

# Fix: Calculate number of video rows and generate matching values
num_video = len(df[df['content_type'] == 'video'])
df.loc[df['content_type'] == 'video', 'engaged'] = np.random.choice([0, 1], num_video, p=[0.2, 0.8])

# Number of blog rows
num_blog = len(df[df['content_type'] == 'blog'])
df.loc[df['content_type'] == 'blog', 'engaged'] = np.random.choice([0, 1], num_blog, p=[0.5, 0.5])

# Create the contingency table (counts only—key step!)
contingency = pd.crosstab(df['content_type'], df['engaged'])  # Rows: content_type, Columns: engaged (0,1)

# Run chi-square on the table's values (numeric array)
chi2_stats, p_value, df_freedom, expected = chi2_contingency(contingency.values)

# For alpha=0.05 (95% confidence)
critical_value = chi2.ppf(0.95, df_freedom)

# One-liner for Cramér's V (now using contingency, which has no strings)
cramers_v = np.sqrt(chi2_stats / (contingency.astype(float).values.sum() * (min(contingency.shape) - 1)))

print(f"Chi2: {chi2_stats:.3f}")
print(f'Critical value: {critical_value:.3f}')
print(f"P-value: {p_value:.4f}")
print(f"Cramér's V: {cramers_v:.3f}")

# Null hypothesis: 
# The variables in this analysis are independent, so there is no association between them.

# How much does the observed data deviate from the expected?
# chi2 = 8.189 (df=1), well above the critical value of ~3.84, 
# showing strong deviation from an independent relationship—
# this refutes the null hypothesis of no link between content type and engagement.

# How likely is this result due to chance?
# p-value = 0.004, far below the 0.05 threshold, confirming statistical significance
# and reinforcing a real (non-random) connection between the variables.

# How strong is the connection?
# Cramér's V = 0.286 falls in the 0.10-0.30 range: small/weak association.
    # Under 0.10: Negligible (ignore unless huge sample).
    # 0.10-0.30: Small/weak (worth exploring, but modest impact).
    # Over 0.30: Getting meaningful.
# Content type influences engagement modestly—worth exploring, but other factors (e.g., user segment) matter too.

# What direction should we take based on these results?
# With overall 66% engagement and videos at 77% vs. blogs at 47% (n=100 users),
# prioritize videos for user activation—could boost trials by 5-7% in our next A/B test,
# aligning with SaaS benchmarks for video-driven retention.