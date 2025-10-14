import pandas as pd

# Mock data
data = {
    'merchant_id': ['m1abc', 'm2def', 'm3ghi', 'm4jkl'],
    'count_of_events': [100, 200, 300, 400],
    'usd_amount': [50.0, 100.0, 150.0, 200.0]
}
df = pd.DataFrame(data)

df['merchant_prefix'] = df['merchant_id'].str[:3]
print(df['merchant_prefix'])

