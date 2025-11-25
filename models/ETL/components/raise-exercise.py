import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MARKETING_DATA = {
    'Campaign_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Channel': ['Meta', 'Google', 'Meta', 'TikTok', 'Google', 'Meta', 'TikTok', 'Google', 'Meta', 'TikTok'],
    'Spend': [5000, 7500, 2000, 1000, 9000, 6000, 1500, 8000, 4500, 2500],
    'Leads': [250, 400, 100, 50, 450, 300, 80, 420, 220, 120],
    'Conversion_Rate': [0.12, 0.15, 0.10, 0.08, 0.18, 0.11, 0.07, 0.16, 0.13, 0.09],
    'File_Path': ['data/meta.csv', 'data/google.csv', 'data/meta.csv', 'data/tiktok.csv', 'data/google.csv', 
                  'data/meta.csv', 'data/tiktok.csv', 'data/google.csv', 'data/meta.csv', 'data/tiktok.csv']
}
df = pd.DataFrame(MARKETING_DATA)

class InvalidChannelError(Exception):
    """Custom exception for unexpected marketing channel data."""
    pass

def validate_and_process(df, min_rows=5):
    """Enforces data quality rules and raises exceptions on failure."""

    # type enforcement
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Input must be a pandas DataFrame.')

    if df.shape[0] < min_rows:
        raise Exception(f'Data quality check failed: Dataframe has only {df.shape[0]} rows, requires {min_rows}.')

    valid_channels = ['Meta', 'Google', 'TikTok']
    if not df['Channel'].isin(valid_channels).all():
        invalid = df[~df['Channel'].isin(valid_channels)]['Channel'].unique()
        raise InvalidChannelError(f'Unexpected channels found: {invalid}. ETL must stop.')

    return True

def main(df):
    try:
        validate_and_process(df)
        logging.info('Validation passed!')
    except Exception as e:
        logging.error(f'Validation failed at MAIN level: {type(e).__name__} caught.')
        raise

main(df)