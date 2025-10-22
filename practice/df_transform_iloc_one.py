import pandas as pd

data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'acquisition_source': ['social', 'search', 'email', 'paid_ad', 'social', 'search', 'email', 'paid_ad', 'social', 'search'],
    'hours_watched': [4.2, 6.8, 3.1, 5.5, 7.0, 2.9, 4.8, 6.2, 5.1, 3.7],
    'mrr_value': [45, 52, 38, 48, 55, 42, 50, 53, 46, 41]
}
df = pd.DataFrame(data)

