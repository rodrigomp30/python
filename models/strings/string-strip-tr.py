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


df['event_striped'] = df['event'].str.strip()
print(df[['event', 'event_striped']].head(3))