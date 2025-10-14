import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols

np.random.seed(42)

# Mock data for 200 leads
n = 200
data = {
    'lead_id': range(1, n+1),
    'content_type': np.random.choice(['video', 'blog', 'email'], n),
    'views': np.random.randint(10, 500, n),
    'activation_time': np.random.exponential(scale=5, size=n).round(1),
    'engaged': np.random.choice([0, 1], n, p=[0.4, 0.6])  # 60% engagement rate
}
df = pd.DataFrame(data)

"""Correlation"""

# -0.042 correlation (means almost no relationship (close to 0))
# and 0.5 p-value ((greater the 0.05) suggests it's random, not a real link)
corr, p = stats.pearsonr(df['views'], df['activation_time'])
print(f'Correlation: {corr:.3f}, p-value: {p:.3f}')


#                     views  activation_time   engaged
# views            1.000000        -0.041805  0.030313
# activation_time -0.041805         1.000000 -0.058985
# engaged          0.030313        -0.058985  1.000000

# no correalation between variables, all of them close to 0
corr_matrix = df[['views', 'activation_time', 'engaged']].corr()
print(corr_matrix)


"""Lienar Regression"""

# Intercept 5.3 means average activation time of 5.3 days with 0 views; 
# slope -0.001 means each additional view reduces time by 0.001 days (negligible).
model = sm.OLS.from_formula('activation_time ~ views', data=df).fit()
print(model.params)

# Interpretation of the intercept:
# It means that for users with 0 views (dind't view anything), the expected activation day is 5

# Interpretation of the slope:
# It means that for every new view, the expected activation days decreases by 0.001 days.


# We can also do this specific predictions using the .predict() method
# To predict the activation time of a 300 views user, 
# we need to first create a new dataset with views equal to 300 as shown below:
new_pred = {'views': [300]}
prediction_300 = model.predict(new_pred)
print(prediction_300) # 4.88 days (but this isnt a strong model according to the tes above)


"""A/B testing with Two-Sample T Test"""

video_time = df[df['content_type'] == 'video']['activation_time']
blog_time = df[df['content_type'] == 'blog']['activation_time']

# t-stat 0.084 means little difference; 
# p-value 0.93 > 0.05 suggests video and blog activate similarly (their avarages are not really different)
t_stat, p = stats.ttest_ind(video_time, blog_time)
print(f'T_stat: {t_stat:.3f}, p-value: {p:.3f}')

"""ANOVA + Tukey"""

video_time_n = df[df['content_type'] == 'video']['activation_time']
blog_time_n = df[df['content_type'] == 'blog']['activation_time']
email_time = df[df['content_type'] == 'email']['activation_time']

# F-stat 0.20 means no major group differences; 
# p-value 0.81 > 0.05 suggests content types activate users similarly (No difference in their activation average)
f_stat, p = stats.f_oneway(video_time_n, blog_time_n, email_time)
print(f'F-stat: {f_stat:.3f}, p-value: {p:.3f}')

