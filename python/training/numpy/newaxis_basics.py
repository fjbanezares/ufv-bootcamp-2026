# import the NumPy library
import numpy as np

# Example 1: Converting a 1D array to 2D
a = np.array([1, 2, 3])  # Original 1D array
a_newaxis_0 = a[np.newaxis, :]  # Adding a new axis along the 0th axis
# Here, a_newaxis_0 becomes a 2D array with shape (1, 3)

# Example 2: Converting a 2D array to 3D
b = np.array([[1, 2], [3, 4]])  # Original 2D array
b_newaxis_2 = b[:, :, np.newaxis]  # Adding a new axis along the 2nd axis
# Now, b_newaxis_2 is a 3D array with shape (2, 2, 1)

# Example 3: Broadcasting
c = np.array([[1, 2], [3, 4]])  # 2D array
d = np.array([1, 2])  # 1D array

# Broadcasting by adding a new axis
result = c + d[:, np.newaxis]
# The new axis helps to align the arrays for broadcasting.
# result becomes a 2D array with the values [[2, 3], [5, 6]]

# Broadcasting can be extremely useful when you need to perform element-wise operations between arrays of different shapes.

# Adding dimensions can sometimes be crucial for aligning arrays in operations that require the same number of dimensions.

# Confirming np.newaxis is an alias for None
print("Is newaxis None?", np.newaxis is None)  # Output: True

# Example 1: 1D to 2D array
a = np.array([1, 2, 3])
a_newaxis = a[:, np.newaxis]
a_none = a[:, None]
print("Shape with newaxis:", a_newaxis.shape)  # Output: (3, 1)
print("Shape with None:", a_none.shape)  # Output: (3, 1)

# Example 2: Adding more dimensions
b = a[:, np.newaxis, np.newaxis]
b_none = a[:, None, None]
print("Shape with multiple newaxis:", b.shape)  # Output: (3, 1, 1)
print("Shape with multiple None:", b_none.shape)  # Output: (3, 1, 1)

# Example 3: Broadcasting using np.newaxis
x = np.arange(3)
print("x:", x)
y = np.arange(3, 6)
print("y:", y)
print("x[:, np.newaxis]:", x[:, np.newaxis])
result = x[:, np.newaxis] * y
print(
    "Broadcasting Result:", result
)  # Output: [[ 0,  0,  0], [ 3,  4,  5], [ 6,  8, 10]]

# Example 4: Verifying np.newaxis, None and newaxis slice are the same
print(
    "Is shape of x[newaxis, :] same as x[newaxis]?",
    (x[np.newaxis, :]).shape == (x[np.newaxis]).shape,
)  # Output: True
print(
    "Is shape of x[newaxis, :] same as x[None, :]?",
    (x[np.newaxis, :]).shape == (x[None, :]).shape,
)  # Output: True
