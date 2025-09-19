import pandas as pd

# Mock data
data = {
    'merchant_id': ['m1', 'm1', 'm2', 'm2', 'm3'],
    'date': ['2013-01-04', '2013-01-05', '2013-01-08', '2013-01-09', '2013-01-10'],
    'count_of_events': [100, 200, 300, 400, 500],
    'usd_amount': [50.0, 100.0, 150.0, 200.0, 250.0]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

df['previous_count_of_events'] = df['count_of_events'].shift(1).fillna(0)
df['diff_count_of_events'] = df['count_of_events'] - df['previous_count_of_events']
print(df)

df['previous_usd_amount'] = df['usd_amount'].shift(1).fillna(0)
df['diff_usd_amount'] = df['usd_amount'] - df['previous_usd_amount']
print(df[['merchant_id', 'date', 'usd_amount', 'previous_usd_amount', 'diff_usd_amount']])