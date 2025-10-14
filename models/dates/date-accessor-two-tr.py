import pandas as pd

data = {
    'merchant_id': ['m1', 'm2', 'm3', 'm4'],
    'date_id': ['2013-01-04', '2013-01-05', '2014-01-08', '2014-01-09'],
    'count_of_events': [100, 200, 300, 400],
    'usd_amount': [50.0, 100.0, 150.0, 200.0]
}
df = pd.DataFrame(data)

df['date_id'] = pd.to_datetime(df['date_id'])

df['year'] = df['date_id'].dt.year
print(df)

df_jan = df[df['date_id'].dt.month == 1]
print(df_jan)

df_2013 = df[df['date_id'].dt.year == 2013]
print(df_2013)

min_date = df['date_id'].min()
df['days_since_started'] = (df['date_id']- min_date).dt.days
print(df)

df['shifted_date'] = df['date_id'] + pd.Timedelta(days=7)
print(df)

df['weeday'] = df['date_id'].dt.day_name()
print(df)