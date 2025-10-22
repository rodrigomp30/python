import numpy as np
import pandas as pd
from scipy import stats

# Step 1: Create DataFrame (simulated MasterClass A/B on email open rates; replace with real data)
np.random.seed(101)  # For this "another" test
group_a = np.random.normal(35, 8, 120)  # Variant A: Engaging subjects, higher mean
group_b = np.random.normal(28, 8, 120)  # Variant B: Standard subjects

group_a = np.clip(group_a, 0,100)
group_b = np.clip(group_b, 0,100)

df = pd.DataFrame({
    'user_id': range(1, 241),
    'variant': ['A'] * 120 + ['B'] * 120,
    'open_rate': np.concatenate([group_a, group_b])
})

# Step 2: Run two-sample t-test (H0: means equal)
group_a_data = df[df['variant'] == 'A']['open_rate']
group_b_data = df[df['variant'] == 'B']['open_rate']

t_stat, p_value = stats.ttest_ind(group_a_data, group_b_data, equal_var=True)

# Degrees of freedom and critical value (two-tailed, alpha=0.05)
dof = len(group_a_data) + len(group_b_data) - 2
critical_t = stats.t.ppf(0.975, dof)

# Cohen's d (pooled std)
pooled_std = np.sqrt(((len(group_a_data)-1)*np.var(group_a_data) + (len(group_b_data)-1)*np.var(group_b_data)) / dof)
cohens_d = (np.mean(group_a_data) - np.mean(group_b_data)) / pooled_std

mean_a = group_a_data.mean()
mean_b = group_b_data.mean()

print(f'Mean A: {mean_a:.3f}')
print(f'Mean B: {mean_b:.3f}')

print(f't_stat: {t_stat:.3f}')
print(f'critical_t: {critical_t:.3f}')
print(f'p_value: {p_value:.3f}')
print(f'cohens_d: {cohens_d:.3f}')
