import pandas as pd

data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'acquisition_source': ['social', 'search', 'email', 'paid_ad', 'social', 'search', 'email', 'paid_ad', 'social', 'search'],
    'hours_watched': [4.2, 6.8, 3.1, 5.5, 7.0, 2.9, 4.8, 6.2, 5.1, 3.7],
    'mrr_value': [45, 52, 38, 48, 55, 42, 50, 53, 46, 41]
}
df = pd.DataFrame(data)
# df.index = ['user_001', 'user_002', 'user_003', 'user_004', 'user_005', 'user_006', 'user_007', 'user_008', 'user_009', 'user_010']  # Label-based index for loc

df_01 = df.loc[(df['hours_watched'] > 4) & (df['mrr_value'] < 55), ['user_id', 'acquisition_source']]
# print(df_01)

df_02 = df.loc['2':'6']
df_02.loc[df['acquisition_source'] == 'email', 'mrr_value'] = 0
# print(df_02)

df_03 = df.loc[((df['mrr_value'] > 40) & (df['hours_watched'] < 5)) | (df['acquisition_source'] == 'search'), ['hours_watched', 'mrr_value']]
# print(df_03)

df['high_mrr_flag'] = False
df_04 = df.loc['1':'7']
df_04.loc[df['mrr_value'] > 50, 'high_mrr_flag'] = True
# print(df_04)

df_05 = df.loc['0':'5']
df_05_2 = df_05.loc[(df['acquisition_source'] != 'paid_ad') & (df['hours_watched'] > 3), 'acquisition_source':'mrr_value']
# print(df_05_2)

df_06 = df.loc['3':'8']
df_06_2 = df_06.loc[df_06['mrr_value'] > 45, ~df.columns.isin(['hours_watched'])]
# print(df_06_2)

df_07 = df.loc['0':'4']
df_07.loc[df_07['mrr_value'] < 50, 'acquisition_source'] = 'organic'
df_07_2 = df_07[df_07['acquisition_source'] == 'organic']
# print(df_07_2)

df_08 = df.loc[df['acquisition_source'].str.contains('so|se'), df.columns.str.contains('value')]
# print(df_08)

df_09 = df.loc['1':'6']
df_09.loc[df['acquisition_source'] == 'search', 'hours_watched'] = 10
df_09_2 = df_09.loc[df['hours_watched'] > 5, ['acquisition_source', 'hours_watched']]
# print(df_09_2)

df_10 = df.loc[df.index % 2 == 0]
df_10.loc[df_10['hours_watched'] > 4, 'mrr_value'] = df_10['mrr_value'] * 1.1
# print(df_10)