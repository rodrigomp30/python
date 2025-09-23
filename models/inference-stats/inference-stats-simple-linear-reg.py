import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.formula.api import ols

np.random.seed(42)

# Mock data
data = {
    'merchant_id': np.random.choice(['m1', 'm2', 'm3'], 100),
    'segment': np.random.choice(['saas', 'ecommerce', 'platforms'], 100),
    'count_of_events': np.random.randint(50, 600, 100),
    'usd_amount': np.random.uniform(25.0, 300.0, 100),
    'success': np.random.choice([0, 1], 100, p=[0.3, 0.7])  # For binomial
}
df = pd.DataFrame(data)

model = sm.OLS.from_formula('usd_amount ~ count_of_events', data=df).fit()
print(model.params)
