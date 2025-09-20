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


# Purpose: Changes the data type (e.g., int64 to float64 or vice versa)

df['count_of_events_float'] = df['count_of_events'].astype(float)
print(df[['count_of_events', 'count_of_events_float']].head(3))

df['usd_amount_int'] = df['usd_amount'].astype(int)
print(df[['usd_amount', 'usd_amount_int']].head(3))