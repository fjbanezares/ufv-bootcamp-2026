# Importing the NumPy library. Please note that NumPy is the go-to library for numerical computations in Python.
import numpy as np

# First, let’s start with a simple 1D array (a vector), and explore reshaping it into 2D arrays.
data = np.array([1, 2, 3, 4, 5, 6])

# Example 1: Reshaping the data into a 2x3 matrix.
# Please understand that reshaping changes the view of the data, but the total number of elements must match.
reshaped_data_2x3 = data.reshape(2, 3)  # Reshaping into 2 rows and 3 columns.
print("Reshaped data (2x3):\n", reshaped_data_2x3)

# Example 2: Reshaping the data into a 3x2 matrix.
reshaped_data_3x2 = data.reshape(3, 2)  # Reshaping into 3 rows and 2 columns.
print("Reshaped data (3x2):\n", reshaped_data_3x2)

# Please remember that when reshaping, the product of the dimensions (rows * columns) must equal the total number of elements.

# Let's now explore more advanced reshaping techniques.

# Example 3: Using the wildcard (-1) in reshaping.
# The -1 tells NumPy to automatically infer the appropriate dimension based on the total number of elements.
reshaped_data_auto = data.reshape(-1, 1)  # NumPy automatically calculates the number of rows.
print("Reshaped data with wildcard (-1,1):\n", reshaped_data_auto)

# Similarly, you can use the wildcard to infer the number of columns:
reshaped_data_auto2 = data.reshape(1, -1)  # NumPy calculates the number of columns.
print("Reshaped data with wildcard (1,-1):\n", reshaped_data_auto2)

# Now, let’s take a closer look at `np.newaxis`, which is extremely useful when you want to add a new dimension to your array.
# This can be helpful for broadcasting, matrix operations, or changing the orientation of a vector (row vs column).

# Example 4: Using np.newaxis to convert a 1D array to a row vector (1xN).
row_vector = data[np.newaxis, :]  # Adds a new axis at the beginning (row vector).
print("Row vector using np.newaxis:\n", row_vector)

# Example 5: Using np.newaxis to convert a 1D array to a column vector (Nx1).
column_vector = data[:, np.newaxis]  # Adds a new axis at the end (column vector).
print("Column vector using np.newaxis:\n", column_vector)

# Thanks for your attention! Please note that `np.newaxis` is often used in the following cases:
# 1. When you need to align dimensions for broadcasting.
# 2. When you want to explicitly convert a 1D array into a 2D row or column vector.

# Let’s explore an example of broadcasting with `np.newaxis`:
# Example 6: Broadcasting a 1D array across the rows of a 2D matrix.
matrix = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
vector = np.array([1, 2, 3])

# Using np.newaxis, we can broadcast the vector across each row of the matrix.
broadcasted_result = matrix + vector[np.newaxis, :]  # Adds the vector to each row of the matrix.
print("Broadcasted result (adding vector to each row):\n", broadcasted_result)

# Thanks again! Please note that you can also broadcast across columns.
broadcasted_result_col = matrix + vector[:, np.newaxis]  # Broadcasts the vector across each column of the matrix.
print("Broadcasted result (adding vector to each column):\n", broadcasted_result_col)

# Please remember that using `np.newaxis` allows you to control the alignment of dimensions during broadcasting.
# It’s a simple and powerful way to expand arrays to higher dimensions without copying data.

# Finally, let’s talk about flattening and raveling arrays.
# Flattening transforms a multi-dimensional array into a 1D array.

# Example 7: Using flatten() to convert a matrix back into a 1D array.
flattened = matrix.flatten()  # Flattening always returns a copy.
print("Flattened matrix:\n", flattened)

# Example 8: Using ravel() to convert a matrix into a 1D array.
raveled = matrix.ravel()  # Ravel tries to return a view if possible, otherwise a copy.
print("Raveled matrix:\n", raveled)

print(matrix)


# When to use flatten() vs ravel():
# Please note that flatten() always returns a copy, while ravel() tries to return a view if possible.
# Use ravel() when you don’t need a new copy and want to avoid unnecessary memory usage.
# Use flatten() when you always need a separate copy of the data.

# Thank you so much for your patience! I hope this deep dive into reshaping, `np.newaxis`, and array flattening has been helpful.
# Making changes to the raveled array
raveled[0] = 100  # Modify the first element of the raveled view
print("Modified raveled array:\n", raveled)  # Expected to show the modification
print("Original matrix after modifying raveled array:\n", matrix)  # The original matrix will reflect the change
matrix[0,0]=1 # restore
# Making changes to the flattened array
flattened[0] = 999  # Modify the first element of the flattened copy
print("Modified flattened array:\n", flattened)  # Expected to show the modification
print("Original matrix after modifying flattened array:\n", matrix)  # The original matrix will NOT be affected
