# Mock dictionary: merchant_id as keys, nested dicts with dates and metrics
mock_dict = {
    'm1': {
        '2013-01-04': {'count_of_events': 100, 'usd_amount': 50.0},
        '2013-01-05': {'count_of_events': 200, 'usd_amount': 100.0}
    },
    'm2': {
        '2013-01-08': {'count_of_events': 300, 'usd_amount': 150.0},
        '2013-01-09': {'count_of_events': 400, 'usd_amount': 200.0}
    },
    'm3': {
        '2013-01-10': {'count_of_events': 500, 'usd_amount': 250.0}
    }
}

# Purpose: Creates or transforms dictionaries efficiently (e.g., mapping merchant IDs to totals).

# Create a dictionary of total events per merchant
    
total_events_dict = {
    merchant: sum(data[date]['count_of_events'] for date in data) 
    for merchant, data in mock_dict.items()
    }
print(total_events_dict)


total_usd_dict = {
    merchant: sum(inner_dict[date]['usd_amount'] for date in inner_dict)
    for merchant, inner_dict in mock_dict.items()
}
print(total_usd_dict)