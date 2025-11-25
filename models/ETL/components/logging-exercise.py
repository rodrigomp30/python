import pandas as pd
import logging
import os

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

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_metrics(df):
    """Calculates total spent and return calculated metrics"""

    logging.info('Starting metric calculation')

    total_spend = df.loc[:,'Spend'].sum() #ex1

    logging.debug(f'Intermediate calculation: Total leads are {df.loc[:, 'Leads'].sum()}') #ex2

    if total_spend < 50000:
        logging.warning(f'Total spend is low ${total_spend:,.0f}. May affect analysis coverage')

    if df.loc[:, 'Spend'].empty:
        logging.critical('Input Dataframe is empty. Calculation aborted')
        return None, None

    try:
        avg_cost_per_lead = total_spend / df.loc[:, 'Leads'].sum()
    except Exception:
        loggin.execepetion('A mathematical error occurred during final metric calculation.')
        return None, None

    logging.info('Metric calculation completed successfully')
    return total_spend, avg_cost_per_lead

calculate_metrics(df)