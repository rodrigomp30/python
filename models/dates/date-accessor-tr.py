import pandas as pd
import numpy as np

# Function to generate dates with time for a given year and months
def generate_dates_with_time(years, months):
    dates = []
    for year in years:
        for month in months:
            days = pd.date_range(start=f'{year}-{month:02d}-01', end=f'{year}-{month:02d}-{pd.Period(f"{year}-{month}").days_in_month}', freq='D')
            for day in days:
                # Random time between 00:00:00 and 23:59:59
                hour = np.random.randint(0, 24)
                minute = np.random.randint(0, 60)
                second = np.random.randint(0, 60)
                time_str = f'{hour:02d}:{minute:02d}:{second:02d}'
                dates.append(day.strftime('%Y-%m-%d ') + time_str)
    return dates

# Generate mock data
years = [2013, 2014, 2015]
months = [1, 2, 3]  # January, February, March
dates = generate_dates_with_time(years, months)

# Create DataFrame with random values
np.random.seed(42)  # For reproducibility
data = {
    'merchant_id': np.random.choice(['m1', 'm2', 'm3', 'm4'], size=len(dates)),
    'date': dates,
    'count_of_events': np.random.randint(50, 600, size=len(dates)),
    'usd_amount': np.random.uniform(25.0, 300.0, size=len(dates)).round(2)
}
df = pd.DataFrame(data)


df['date'] = pd.to_datetime(df['date'])

df['year'] = df['date'].dt.year
print(df[['date','year']].head(3))

df['month'] = df['date'].dt.month
print(df[['date','month']].head(3))

df['day'] = df['date'].dt.day
print(df[['date','day']].head(3))

df['hour'] = df['date'].dt.hour
print(df[['date', 'hour']].head(3))

df['minute'] = df['date'].dt.minute
print(df[['date', 'minute']].head(3))

df['second'] = df['date'].dt.second
print(df[['date', 'second']].head(3))