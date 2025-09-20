import numpy as np

# Mock data as NumPy arrays and lists
merchant_ids = np.array(['m1', 'm1', 'm2', 'm2', 'm3'])
count_of_events_array = np.array([100, 250, 350, 450, 600])
usd_amount_array = np.array([50.1234, 150.6789, 200.2345, 300.7890, 400.5678])
event_duration_array = np.array([15, 30, 45, 60, 75])

count_of_events_list = [100, 250, 350, 450, 600]
usd_amount_list = [50.1234, 150.6789, 200.2345, 300.7890, 400.5678]
event_duration_list = [15, 30, 45, 60, 75]

# array
usd_amount_rounded = np.round(usd_amount_array, 2)
print(usd_amount_rounded)


# list
usd_amount_rounded_list = [round(x,2) for x in usd_amount_list]
print(usd_amount_rounded_list)