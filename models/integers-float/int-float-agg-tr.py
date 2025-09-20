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

# Purpose: Computes aggregate statistics (e.g., total events per merchant).

# aggregates and create (transform method) a column with the result
df['total_events'] = df.groupby('merchant_id')['count_of_events'].transform('sum') 
print(df[['merchant_id', 'count_of_events', 'total_events']])

df['avg_event'] = df.groupby('merchant_id')['event_duration'].transform('mean')
print(df[['merchant_id','event_duration', 'avg_event']])


# simple aggregations
total_events = df['count_of_events'].sum()
avg_event = df['event_duration'].mean()
median_event = df['event_duration'].median()
usd_amount_std = df['usd_amount'].std()

print(f'total events: {total_events} | average events: {avg_event} | median events: {median_event} | STD usd amount: {usd_amount_std}')


#aggregation with agg()
agg_df = df.groupby('merchant_id').agg({'count_of_events': 'sum', 'usd_amount': 'mean'}).reset_index().copy()
print(agg_df)