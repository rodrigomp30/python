import pandas as pd

# Mock data with six different date column types
mock_data = {
    'string_date': ['2023-01-15', '2023-02-20', '2023-03-10'],  # String in 'YYYY-MM-DD' format
    'unix_timestamp': [1673750400, 1676851200, 1678416000],     # Unix timestamp (seconds since 1970-01-01)
    'datetime_string': ['15-Jan-2023 14:30:00', '20-Feb-2023 09:15:00', '10-Mar-2023 16:45:00'],  # Datetime string with time
    'excel_serial': [44927, 44963, 44981],                      # Excel serial date (days since 1900-01-01)
    'iso_week_date': ['2023-W03-1', '2023-W08-3', '2023-W11-5'], # ISO week date (YYYY-Www-d)
    'custom_format': ['01/15/23', '02/20/23', '03/10/23']       # Custom string format (MM/DD/YY)
}

df = pd.DataFrame(mock_data)
print("Original Mock Data:")
print(df)

df['date'] = pd.to_datetime(df['date'].dt.strftime('%m-%d-%Y'))
print('\n. After foramating date')
print(df['date'])
print(df)