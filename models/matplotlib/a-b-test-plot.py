import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.patches import FancyBboxPatch  # For a simple bracket

# Your data (matching results)
np.random.seed(789)
group_a = np.random.normal(28.87, 6, 100)  # Variant A
group_b = np.random.normal(23.35, 6, 100)  # Variant B

df = pd.DataFrame({
    'user_id': range(1, 201),
    'variant': ['A'] * 100 + ['B'] * 100,
    'session_duration': np.concatenate([group_a, group_b])
})

# Quick t-test recap
group_a_data = df[df['variant'] == 'A']['session_duration']
group_b_data = df[df['variant'] == 'B']['session_duration']
t_stat, p_value = stats.ttest_ind(group_a_data, group_b_data)
mean_a = np.mean(group_a_data)
mean_b = np.mean(group_b_data)
gap = mean_a - mean_b

# Overlaid histogram with enhancements
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(group_a_data, bins=20, alpha=0.6, label='Variant A (Short Intro)', color='lightgreen', density=True)
ax.hist(group_b_data, bins=20, alpha=0.6, label='Variant B (Long Intro)', color='lightcoral', density=True)

# Vertical lines for group centers (means)
ax.axvline(mean_a, color='darkgreen', linestyle='--', linewidth=2, label=f'A Mean: {mean_a:.1f} min')
ax.axvline(mean_b, color='darkred', linestyle='--', linewidth=2, label=f'B Mean: {mean_b:.1f} min')

# Bracket/arrow for the gap (horizontal span between means)
ax.annotate('', xy=(mean_a, 0.3), xytext=(mean_b, 0.3),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
ax.text((mean_a + mean_b)/2, 0.35, f'Gap: {gap:.1f} min', ha='center', fontsize=10, fontweight='bold')

# Text box for t-stat (top-right corner)
t_box = FancyBboxPatch((0.65, 0.7), 0.25, 0.15, boxstyle="round,pad=0.1", facecolor='lightblue', alpha=0.8)
ax.add_patch(t_box)
ax.text(0.7, 0.8, f't-stat: {t_stat:.1f}\n(Big stretch = Low overlap)', 
        transform=ax.transAxes, fontsize=11, va='center', ha='left')

ax.set_xlabel('Session Duration (minutes)')
ax.set_ylabel('Density (Proportion)')
ax.set_title('Overlaid Histograms: T-Stat Stretch Visualized')
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()  # Or plt.savefig('enhanced_ab_plot.png') for Tableau/Power BI import