import numpy as np

# Mock matrix array: rows = merchants, columns = days (e.g., 5 merchants, 5 days)
mock_matrix = np.array([
    [100, 200, 300, 400, 500],  # m1 count_of_events
    [50.0, 100.0, 150.0, 200.0, 250.0],  # m1 usd_amount
    [150, 250, 350, 450, 550],  # m2 count_of_events
    [75.0, 125.0, 175.0, 225.0, 275.0],  # m2 usd_amount
    [200, 300, 400, 500, 600]   # m3 count_of_events, etc.
])

