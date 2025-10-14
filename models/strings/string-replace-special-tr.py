import pandas as pd

data = {
    'merchant_id': ['m1@abc', 'm2#def$', 'm3_ghi', 'm4-jkl'],
    'count_of_events': [100, 200, 300, 400],
    'usd_amount': [50.0, 100.0, 150.0, 200.0]
}
df = pd.DataFrame(data)

df['clean_merchant_id'] = df['merchant_id'].str.replace(r'[^a-zA-Z0-9]', '', regex=True)
print(df[['merchant_id', 'clean_merchant_id']])