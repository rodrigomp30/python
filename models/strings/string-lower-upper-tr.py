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
# print(df)


df['segment_lower'] = df['segment'].str.lower()
print(df[['segment', 'segment_lower']].head(3))

df['event_upper'] = df['event'].str.upper()
print(df[['event', 'event_upper']].head(3))