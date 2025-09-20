import pandas as pd

# Mock data
data = {
    'merchant_id': ['m1', 'm2', 'm3', 'm4', 'm5'],
    'event': ['Cart.AddItem ', ' Cart.Checkout', 'charge', 'Subscription.Charge', 'Marketplace.Charge'],
    'segment': ['Saas', 'ecommerce', 'Platforms', 'SAAS', 'ECOMMERCE'],
    'description': ['User added item to cart', 'User completed checkout', 'Payment charge processed', 'Subscription renewed', 'Marketplace transaction']
}
df = pd.DataFrame(data)


df['event_extract'] = df['event'].str[0:4]
print(df[['event', 'event_extract']].head(3))


df['cart_cat'] = df.loc[df['event'].str.contains('Cart'), 'event'].str.strip().str[0:4]
print(df[['event','cart_cat']].head(3))

df['sub_cat'] = df.loc[df['event'].str.contains('Subscription'), 'event'].str[0:12]
print(df[['event', 'sub_cat']])

df['market_cat'] = df.loc[df['event'].str.contains('Marketplace'), 'event'].str[0:11]
print(df[['event', 'market_cat']])