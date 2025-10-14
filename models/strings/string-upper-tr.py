import pandas as pd

data = {
    'merchant_id': ['m1', 'm2', 'm3', 'm4'],
    'segment': ['saas', 'ecommerce', 'SaAs', 'PLATFORMS'],
    'count_of_events': [100, 200, 300, 400],
    'usd_amount': [50.0, 100.0, 150.0, 200.0]
}
df = pd.DataFrame(data)

df['segment_upper'] = df['segment'].str.upper()
print(df[['segment', 'segment_upper']])