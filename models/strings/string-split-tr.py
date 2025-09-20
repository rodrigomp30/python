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

# Purpose: Splits strings into lists or columns

df['event_splited'] = df['event'].str.split('.')
print(df[['event', 'event_splited']].head(3))

df_event_expanded = df['event'].str.split('.', expand=True)
print(df_event_expanded.head(3))