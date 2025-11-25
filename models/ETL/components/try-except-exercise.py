import pandas as pd
import logging
import os
from math import log

# --- Marketing Campaign Data ---
# This dictionary simulates data pulled from various channels (Meta, Google, etc.)
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

def calculate_cpl_and_check(df):
    """Calculates cost per lead (CPL) and handles multiples errors"""

    # total_spend = df.loc[:, 'Spend'].sum()
    # total_leads = df.loc[:, 'Leads'].sum()

    try:
        cpl =  df['Spend'] / df['total_leads']

    except KeyError as e:
        logging.error(f'KeyError caught: Missing column {e}. CPL calculation skipped.')

    try:
        leads = df['Leads'].sum()
        spend = df['Spend'].iloc[0]

        final_cpl = spend / int(leads)

    except (TypeError, ZeroDivisionError) as e:
        logging.error(f'Calculation failed due to data issue: {type(e).__name__}.')
        final_cpl = None

    except Exception as e:
        logging.error(f'An UNEXPECTED error occour: {e}')
        final_cpl = None

    return final_cpl

def safe_log(number):
    """Calculates safe logarithm, handling invalid input"""

    try:
        result = log(number)
    except ValueError as e:
        logging.error(f'ValueError: Cannot calculate log of number {number}. Must be positive.')
        result = None
    finally:
        logging.info(f'Log attempt finished for number: {number}')
    
    return result

calculate_cpl_and_check(df)
safe_log(-5)
