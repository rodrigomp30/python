import pandas as pd
import numpy as np

# Mock data
data = {
    'merchant_id': ['m1', 'm2', 'm3', 'm4', 'm5'],
    'count_of_events': [100, 250, 350, 450, 600],
    'usd_amount': [50.1234, 150.6789, 200.2345, 300.7890, 400.5678],
    'event_duration': [15, 30, 45, 60, 75]
}
df = pd.DataFrame(data)

# Purpose: Limits values

# limit values between 100 and 300
# You can cap outliers out of a distribution with this
df['usd_amount_clipped'] = df['usd_amount'].clip(100,300)
print(df[['usd_amount', 'usd_amount_clipped']].head(4))

# get values within a certain codition
# It’s used for conditional transformations, such as setting values below a threshold to zero or flagging anomalies
# if the condition is TRUE, WILL NOT RECEIVE the flag values
df['usd_adjusted'] = df['usd_amount'].where(df['usd_amount'] > 150,0)
print(df[['usd_amount', 'usd_adjusted']])

df['high_usd_flag'] = df['usd_amount'].where((df['usd_amount'] < 220.0) | (df['usd_amount'] > 301.0),'High')
print(df[['usd_amount', 'high_usd_flag']])


#numpy method usade for several conditions and several outputs
# If the condition is TRUE, WILL RECEIVE the flag values
df['low_usd_flag'] = np.select([df['usd_amount'] < 220.0, df['usd_amount'] > 300.0], ['low', 'high'])
print(df[['usd_amount', 'low_usd_flag']])