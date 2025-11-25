import pandas as pd

data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'acquisition_source': ['social', 'search', 'email', 'paid_ad', 'social', 'search', 'email', 'paid_ad', 'social', 'search'],
    'hours_watched': [4.2, 6.8, 3.1, 5.5, 7.0, 2.9, 4.8, 6.2, 5.1, 3.7],
    'mrr_value': [45, 52, 38, 48, 55, 42, 50, 53, 46, 41]
}
df = pd.DataFrame(data)

df_01 = df.iloc[:3]
# print(df_01)

df_02 = df.iloc[:, :2]
# print(df_02)

df_03 = df.iloc[4,2]
# print(df_03)

df_04 = df.iloc[2:6, 1:4]
# print(df_04)

df_05 = df.iloc[::2]
# print(df_05)

df_06 = df.iloc[-4:, [0, 3]]
# print(df_06)

df_07 = df.iloc[::3]
# df_07 = df.iloc[[0, 3, 6, 9]] --> other way of doing it 
# print(df_07)

high_mrr = df['mrr_value'] > 50
df_08 = df.loc[high_mrr].iloc[:, 1:4]
# print(df_08)

df_09 = df.iloc[::-2]
# print(df_09)

df_10 = df.iloc[:5]
df_10.iloc[[1, 3], 2] = 0
df_10_2 = df_10.iloc[:, :3]
print(df_10_2)