import pandas as pd

data = {
    'merchant_id': ['m1', 'm2', 'm3', 'm4'],
    'date_id': ['2013-01-04', '2013-01-05', '2013-01-08', '2013-01-09'],
    'count_of_events': [100, 200, 300, 400],
    'usd_amount': [50.0, 100.0, 150.0, 200.0]
}
df = pd.DataFrame(data)

df['event_id'] = df['merchant_id'] + '_' + df['date_id'].str.replace('-', '')
print(df)