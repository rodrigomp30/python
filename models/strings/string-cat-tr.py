import pandas as pd

# Mock data
data = {
    'merchant_id': ['m1', 'm2', 'm3', 'm4', 'm5'],
    'event': ['Cart.AddItem ', ' Cart.Checkout', 'charge', 'Subscription.Charge', 'Marketplace.Charge'],
    'segment': ['Saas', 'ecommerce', 'Platforms', 'SAAS', 'ECOMMERCE'],
    'description': ['User added item to cart', 'User completed checkout', 'Payment charge processed', 'Subscription renewed', 'Marketplace transaction']
}
df = pd.DataFrame(data)
print("Original DataFrame:")


# Purpose: Joins strings from multiple columns

df['segment_id'] = df['merchant_id'].str.cat(df['segment'], sep='-')
print(df[['merchant_id', 'segment', 'segment_id']].head(3))

df['description_id'] = df['event'].str.cat(df['description'], sep=' - ')
print(df[['event', 'description', 'description_id']].head(3))

