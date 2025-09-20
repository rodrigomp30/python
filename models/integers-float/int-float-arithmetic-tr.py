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


# Purpose: Performs element-wise arithmetic (e.g., add a bonus to usd_amount).

df['usd_amount_bonus'] = df['usd_amount'].add(10.0)
print(df[['usd_amount', 'usd_amount_bonus']].head(3))

df['event_duration_cut'] = df['event_duration'].sub(5)
print(df[['event_duration', 'event_duration_cut']].head(3))

df['count_of_events_doubled'] = df['count_of_events'].mul(2)
print(df[['count_of_events', 'count_of_events_doubled']].head(3))

df['count_of_events_div'] = df['count_of_events'].div(2)
print(df[['count_of_events', 'count_of_events_div']].head(3))