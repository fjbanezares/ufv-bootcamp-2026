import numpy as np

# ------- Intro to Reshaping in NumPy -------

# Create a simple 1D array
one_d_array = np.array([1, 2, 3, 4, 5, 6, 7])
print("Original 1D array:", one_d_array)

# Reshape the 1D array into a 2D array with shape (3, 2)
two_d_array = one_d_array.reshape((3, 2))
print("Reshaped into 2D (3x2):")
print(two_d_array)

# Use -1 to let NumPy infer the size of one dimension
# In this case, -1 will be inferred as 3 (6 elements / 2 columns = 3 rows)
two_d_array_inferred = one_d_array.reshape((-1, 2))
print("Reshaped with inferred dimension (-1, 2):")
print(two_d_array_inferred)

# ------- Reshaping with newaxis -------

# Add a new axis to transform a 1D array into a column vector
print(one_d_array.shape)

column_vector = one_d_array[np.newaxis, np.newaxis, :]
print(column_vector.shape)
print("Column vector using newaxis:")
print(column_vector)

# ------- Row-Major ('C') vs Column-Major ('F') -------

# Create a 2D array (2x3)
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])

# Reshaping in Row-Major (C-order)
reshaped_row_major = two_d_array.reshape((3, 2), order="C")
print("Reshaped in Row-Major ('C'):")
print(reshaped_row_major)

# Reshaping in Column-Major (F-order)
reshaped_col_major = two_d_array.reshape((3, 2), order="F")
print("Reshaped in Column-Major ('F'):")
print(reshaped_col_major)

# Flattening in Row-Major (C-order)
flattened_row_major = two_d_array.ravel(order="C")
print("Flattened in Row-Major ('C'):", flattened_row_major)

# Flattening in Column-Major (F-order)
flattened_col_major = two_d_array.ravel(order="F")
print("Flattened in Column-Major ('F'):", flattened_col_major)

# C-contiguous (row-major) array
c_array = np.array([[1, 2, 3], [4, 5, 6]], order="C")
# Output: True
print(c_array.flags["C_CONTIGUOUS"])

# F-contiguous (column-major) array
f_array = np.array([[1, 2, 3], [4, 5, 6]], order="F")
# Output: True
print(f_array.flags["F_CONTIGUOUS"])
