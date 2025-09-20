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
count_adjusted = np.where(count_of_events_array > 400, 0, count_of_events_array)
print(count_adjusted)

usd_adjusted = np.where(usd_amount_array > 200, 200, usd_amount_array)
print(usd_adjusted)


# lists
count_adjusted_list = [0 if x > 400 else x for x in count_of_events_list]
print(count_adjusted_list)

usd_adjusted_list = [200 if x > 200 else x for x in usd_amount_list]
print(usd_adjusted_list)