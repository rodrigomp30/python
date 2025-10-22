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
# print(df)

df_01 = df.loc['user_001':'user_007']
# print(df_01)

df_02 = df.loc[['user_001', 'user_005', 'user_009'], 'hours_watched']
# print(df_02)

df_03 = df.loc[df['mrr_value'] > 48]
# print(df_03)

df_04 = df.loc[df['acquisition_source'] == 'social', ['user_id', 'mrr_value']]
# print(df_04)

df_05 = df.loc['user_002':'user_006']
df_05_2 = df_05.loc[df_05['hours_watched'] < 5]
# print(df_05_2)

df_06 = df.loc[(df['mrr_value'] > 45) & (df['acquisition_source'] != 'paid_ad')]
# print(df_06)

# df_07
df['engagement_level'] = 'low'
df.loc[df['hours_watched'] > 5, 'engagement_level'] = 'high'
# print(df)

df_08 = df.loc['user_001':'user_005']
df_08_2 = df_08.loc[df['mrr_value'] < 50, ['acquisition_source', 'hours_watched']]
# print(df_08_2)

df_09 = df.loc[df['acquisition_source'].isin(['social', 'search']), (df.columns.str.startswith('user')) | (df.columns.str.startswith('mrr'))]
# print(df_09)

df_10 = df.loc['user_001':'user_006']
df_10.loc[df_10['hours_watched'] < 4,'mrr_value'] = 0
print(df_10)