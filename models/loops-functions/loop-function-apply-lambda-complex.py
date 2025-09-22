import pandas as pd

data = {
    'merchant_id': ['m1', 'm1', 'm2', 'm2', 'm3'],
    'date': ['2013-01-04', '2013-01-05', '2013-01-08', '2013-01-09', '2013-01-10'],
    'count_of_events': [100, 200, 300, 400, 500],
    'usd_amount': [50.0, 100.0, 150.0, 200.0, 250.0]
}
df = pd.DataFrame(data)

def categoriza_performance(row):
    if row['count_of_events'] > 300 and row['usd_amount'] > 200:
        return 'High'
    elif row['count_of_events'] > 200:
        return 'Medium'
    else:
        return 'Low'
    
df['performance'] = df.apply(lambda row: categoriza_performance(row), axis=1)