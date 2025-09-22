import pandas as pd

data = {
    'merchant_id': ['m1', 'm1', 'm2', 'm2', 'm3'],
    'date': ['2013-01-04', '2013-01-05', '2013-01-08', '2013-01-09', '2013-01-10'],
    'count_of_events': [100, 200, 300, 400, 500],
    'usd_amount': [50.0, 100.0, 150.0, 200.0, 250.0]
}
df = pd.DataFrame(data)

def weighted_average(df):
    weights = [1, 2, 3, 4, 5]
    weighted_sum = 0
    total_weight = 0
    for i, row in df.iterrows():
        weighted_sum += row['usd_amount'] * weights[i]
        total_weight += weights[i]
    return weighted_sum / total_weight if total_weight > 0 else 0

weighted_avg = weighted_average(df)
print(weighted_avg)