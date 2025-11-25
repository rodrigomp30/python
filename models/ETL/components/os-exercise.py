import pandas as pd
import logging
import os

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

script_dir = os.path.dirname(os.path.abspath(__file__))

def manage_etl_paths(filename):
    """Key OS operations"""

    log_file_path = os.path.join(script_dir, 'logs', 'etl_run.log')
    print(f'1. Log path created: {log_file_path}')

    absolute_script_path = os.path.abspath(__file__)
    print(f'Absolute path of the script: {absolute_script_path}')

    config_file = os.path.join(script_dir, '..', 'config.ini')
    normalized_config_path = os.path.normpath(config_file)
    print(f'Normalized config path (parent dir): {normalized_config_path}')

    data_file_exists = os.path.exists(filename)
    if data_file_exists:
        print(f'File {data_file_exists} exists!')
    else:
        print(f'File {data_file_exists} NOT FOUND. Extraction will fail.')
    
    output_dir = os.path.join(script_dir, 'output', 'processed_data')
    os.makedirs(output_dir, exist_ok=True)
    print(f'Output directory ensured: {output_dir}')

    return data_file_exists

manage_etl_paths(df['File_Path'].iloc[0])