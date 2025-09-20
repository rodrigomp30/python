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
count_of_events_flot = count_of_events_array.astype(float)
print(count_of_events_flot)

event_duration_int = event_duration_array.astype(float)
print(event_duration_int)


# lists (with list comprehenssion)
count_of_events_float_list = [float(x) for x in count_of_events_list]
print(count_of_events_list)

event_duration_int_list = [int(x) for x in event_duration_list]
print(event_duration_int_list)