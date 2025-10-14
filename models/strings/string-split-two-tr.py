import pandas as pd

data = {
    'merchant_id': ['m1-abc', 'm2-def', 'm3-ghi', 'm4-jkl'],
    'count_of_events': [100, 200, 300, 400],
    'usd_amount': [50.0, 100.0, 150.0, 200.0]
}
df = pd.DataFrame(data)

df[['prefix', 'suffix']] = df['merchant_id'].str.split('-', expand=True)
print(df)