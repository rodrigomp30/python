import numpy as np

# Mock matrix array: rows = merchants, columns = days (e.g., 5 merchants, 5 days)
mock_matrix = np.array([
    [100, 200, 300, 400, 500],  # m1 count_of_events
    [50.0, 100.0, 150.0, 200.0, 250.0],  # m1 usd_amount
    [150, 250, 350, 450, 550],  # m2 count_of_events
    [75.0, 125.0, 175.0, 225.0, 275.0],  # m2 usd_amount
    [200, 300, 400, 500, 600]   # m3 count_of_events, etc.
])

# Slice first 2 rows (from 0 to 1, the 2 is discarted), all columns
sliced_matrix = mock_matrix[0:2, :]
print(sliced_matrix)

# Slice the first column, all rows
sliced_column = mock_matrix[:, 0]
print(sliced_column)

# Advanced slicing (getting specific position in the matrix (values))
advanced_slice = mock_matrix[[0, 2, 4], [1, 3, 0]] # Row 0 col 1, row 2 col 3, row 4 col 0
print(advanced_slice)


# Loop for custom slicing (sum each row)
rows_sum = []

for i in range(mock_matrix.shape[0]):
    rows_sum.append(mock_matrix[i, :].sum())
print(rows_sum)

# Alternative
rows_sum_array = np.sum(mock_matrix, axis=1) # sum across rows - axis=1 in arrays reffers to rows
print(rows_sum_array)