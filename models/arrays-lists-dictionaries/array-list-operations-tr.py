import numpy as np

# Mock data as NumPy arrays and lists
merchant_ids = np.array(['m1', 'm1', 'm2', 'm2', 'm3'])
count_of_events_array = np.array([100, 250, 350, 450, 600])
usd_amount_array = np.array([50.1234, 150.6789, 200.2345, 300.7890, 400.5678])
event_duration_array = np.array([15, 30, 45, 60, 75])

count_of_events_list = [100, 250, 350, 450, 600]
usd_amount_list = [50.1234, 150.6789, 200.2345, 300.7890, 400.5678]
event_duration_list = [15, 30, 45, 60, 75]


# arrays
total_events = np.sum(count_of_events_array)
print(total_events)

doubled_events = count_of_events_array * 2
print(doubled_events)

total_events_doubled = np.sum(count_of_events_array) * 2
print(total_events_doubled)

avg_usd = np.mean(usd_amount_array)
print(avg_usd)

# lists
total_events_list = sum(count_of_events_list)
print(total_events_list)

total_events_list_doubled = sum(count_of_events_list) * 2
print(total_events_list_doubled)

avg_usd_list = sum(usd_amount_list) / len(usd_amount_list)
print(avg_usd_list)