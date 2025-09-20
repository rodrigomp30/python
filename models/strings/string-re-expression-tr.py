import pandas as pd
import re

# Mock data
data = {
    'merchant_id': ['m1', 'm2', 'm3', 'm4', 'm5'],
    'event': ['Cart.AddItem ', ' Cart.Checkout', 'charge', 'Subscription.Charge', 'Marketplace.Charge'],
    'segment': ['Saas', 'ecommerce', 'Platforms', 'SAAS', 'ECOMMERCE'],
    'description': ['User added item to cart', 'User completed checkout', 'Payment charge processed', 'Subscription renewed', 'Marketplace transaction']
}
df = pd.DataFrame(data)


# Purpose: Replaces patterns using regex (e.g., remove non-alphabetic characters from segment)

df['segment_clean'] = df['segment'].str.replace(r'[^a-zA-Z]','', regex=True)
print(df[['segment', 'segment_clean']].head(3))

df['event_clean'] = df['event'].str.replace(r'[^a-zA-Z]','',regex=True)
print(df[['event', 'event_clean']])

df['description_clean'] = df['description'].str.replace(r'[\sA-Z]', '', regex=True)
print(df[['description', 'description_clean']])