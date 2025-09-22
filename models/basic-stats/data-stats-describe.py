import pandas as pd
import numpy as np

# Mock data
data = {
    'merchant_id': ['m1', 'm1', 'm2', 'm2', 'm3', 'm3', 'm4', 'm4'],
    'date': ['2013-01-04', '2013-01-05', '2013-01-08', '2013-01-09', '2013-01-10', '2013-01-11', '2013-01-12', '2013-01-13'],
    'count_of_events': [100, 200, 300, 400, 500, 600, 700, 800],
    'usd_amount': [50.0, 100.0, 150.0, 200.0, 250.0, 300.0, 350.0, 400.0]
}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

stats_summary = df[['count_of_events', 'usd_amount']].describe()
print(stats_summary)

summary_all = df.describe(include='all')
print(summary_all)