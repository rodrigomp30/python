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

df_date = df.copy()
df_date = df.set_index('date')
monthly_totals = df_date.resample('W').agg({'count_of_events': 'sum', 'usd_amount': 'mean'})
print('\n Monthly Totals:')
print(monthly_totals)