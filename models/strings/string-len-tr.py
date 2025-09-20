import pandas as pd

# Mock data
data = {
    'merchant_id': ['m1', 'm2', 'm3', 'm4', 'm5'],
    'event': ['Cart.AddItem ', ' Cart.Checkout', 'charge', 'Subscription.Charge', 'Marketplace.Charge'],
    'segment': ['Saas', 'ecommerce', 'Platforms', 'SAAS', 'ECOMMERCE'],
    'description': ['User added item to cart', 'User completed checkout', 'Payment charge processed', 'Subscription renewed', 'Marketplace transaction']
}
df = pd.DataFrame(data)

# Purpose: Calculates the length of each string

df['merchant_len'] = df['merchant_id'].str.len()
print(df[['merchant_id', 'merchant_len']].head(3)) # merchant: m1 = len: 2

df['event_len'] = df['event'].str.len()
print(df[['event', 'event_len']].head(3))

df['segment_len'] = df['segment'].str.len()
print(df[['segment', 'segment_len']].head(3))

