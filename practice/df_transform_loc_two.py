import pandas as pd

# Sample DataFrame: 10 users from MasterClass marketing data
data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'acquisition_source': ['social', 'search', 'email', 'paid_ad', 'social', 'search', 'email', 'paid_ad', 'social', 'search'],
    'hours_watched': [4.2, 6.8, 3.1, 5.5, 7.0, 2.9, 4.8, 6.2, 5.1, 3.7],
    'mrr_value': [45, 52, 38, 48, 55, 42, 50, 53, 46, 41]
}
df = pd.DataFrame(data)
df.index = ['user_001', 'user_002', 'user_003', 'user_004', 'user_005', 'user_006', 'user_007', 'user_008', 'user_009', 'user_010']  # Label-based index for loc

df_01 = df.loc['user_002':'user_008']
df_01_2 = df_01.loc[(df['hours_watched'] > 4) & (df['mrr_value']< 55)]
# print(df_01_2)

df_02 = df.loc[df['acquisition_source'].isin(['social', 'email']), 'user_id':'hours_watched']
# print(df_02)

df['high_engagement'] = False
df_03 = df.loc['user_001': 'user_005']
df_03.loc[df_03['hours_watched'] > 6, 'high_engagement'] = True
# print(df_03)

df_04 = df.loc['user_003':'user_009']
df_04_2 = df_04.loc[df_04['mrr_value'] > 40, ['acquisition_source', 'mrr_value']]
# print(df_04_2)

df_05 = df.loc[((df['mrr_value'] > 45) | (df['hours_watched'] > 6)) & (df['acquisition_source'] != 'email'), ~df.columns.str.contains('user_id')]
# print(df_05)

df['priority'] = 'low'
df_06 = df.loc['user_001':'user_006']
df_06.loc[df_06['mrr_value'] > 50, 'priority'] = 'high'
# print(df_06)

df_07 = df.loc[(df.index.str.contains('user_00')) & (df['mrr_value'].between(40,55))]
# print(df_07)

df_08 = df.loc[(df['acquisition_source'] == 'search') | (df['mrr_value'] > 50), 'acquisition_source':'mrr_value']
# print(df_08)

df_09 = df.loc['user_006':'user_010']
df_09.loc[df_09['mrr_value'] < 45, 'hours_watched'] = 0
df_09_2 = df_09.loc[df_09['hours_watched'] > 3]
# print(df_09)
# print(df_09_2)

df_10 = df.loc[(df.index.str.endswith('05')) | (df.index.str.endswith('08'))]
df_10.loc[df['acquisition_source'] == 'paid_ad', 'mrr_value'] = 0
df_10['adjusted_mrr'] = df_10['mrr_value'] * 1.1
# print(df_10)