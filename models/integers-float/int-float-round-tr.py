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

# Purpose: Rounds float values to a specified number of decimal places.

df['usd_amount_rounded'] = df['usd_amount'].round(2)
print(df[['usd_amount', 'usd_amount_rounded']].head(3))