import pandas as pd

data = {
    'merchant_id': ['m1', 'm1', 'm2', 'm2', 'm3'],
    'date': ['2013-01-04', '2013-01-05', '2013-01-08', '2013-01-09', '2013-01-10'],
    'count_of_events': [100, 200, 300, 400, 500],
    'usd_amount': [50.0, 100.0, 150.0, 200.0, 250.0]
}
df = pd.DataFrame(data)


def cumulative_process(df, threshold=1000):
    cumulative_events = 0
    i = 0
    while cumulative_events < threshold and i < len(df):
        cumulative_events += df.iloc[i]['count_of_events']
        i += 1
    return df.iloc[:i]

process_df = cumulative_process(df, threshold=800)
print(df[['merchant_id', 'count_of_events']])
print(process_df)