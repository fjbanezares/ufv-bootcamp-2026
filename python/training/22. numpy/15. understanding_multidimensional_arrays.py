import numpy as np

# Please note, we are starting simple with 2D arrays to lay a solid foundation.
# Thanks for your attention!

# 1. 2D Array Example (Rows and Columns)
# Let's create a 2D array, which is essentially a matrix.
# A 2D array can be thought of as a grid, with rows and columns.

print("Creating a 2D array:")

# A simple 2x3 array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# The .shape attribute shows us the dimensions of the array.
# In this case, it has 2 rows and 3 columns.
print("2D Array:\n", array_2d)
print("Shape of 2D array:", array_2d.shape)  # (2, 3)

# If you want to access the element in the first row and second column:
element = array_2d[0, 1]
print("Element at first row, second column:", element)  # Output should be 2

# Now let's move on to a 3D array! Please pay attention :)

# 2. 3D Array Example (A cube or a stack of matrices)
# A 3D array can be thought of as a stack of 2D arrays.

print("\nCreating a 3D array:")

# This creates a 3D array of shape (2, 3, 4).
# Imagine it as 2 blocks of 2D arrays, each with 3 rows and 4 columns.
array_3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                     [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])

print("3D Array:\n", array_3d)
print("Shape of 3D array:", array_3d.shape)  # (2, 3, 4)

# If you want to access the element in the second 2D block, first row, and third column:
element_3d = array_3d[1, 0, 2]
print("Element at [1, 0, 2]:", element_3d)  # Output should be 15

# A handy trick: Reshape the 3D array into 2D, using .reshape()
array_reshaped = array_3d.reshape(6, 4)
print("\nReshaped 3D array into 2D (6x4):\n", array_reshaped)

# Now things get more fun with 4D arrays. Thanks for keeping up so far!

# 3. 4D Array Example (Imagine it like a 3D stack of 2D arrays)
# A 4D array can be thought of as a stack of 3D arrays.
# Let's create a 4D array of shape (2, 2, 3, 4), which means:
# - 2 blocks of 3D arrays
# - Each 3D array has 2 blocks of 2D arrays
# - Each 2D array has 3 rows and 4 columns.

print("\nCreating a 4D array:")

array_4d = np.array([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                      [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]],
                     [[[25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36]],
                      [[37, 38, 39, 40], [41, 42, 43, 44], [45, 46, 47, 48]]]])

print("4D Array:\n", array_4d)
print("Shape of 4D array:", array_4d.shape)  # (2, 2, 3, 4)

# Let's access the element in the first 3D block, second 2D array, third row, and fourth column:
element_4d = array_4d[0, 1, 2, 3]
print("Element at [0, 1, 2, 3]:", element_4d)  # Output should be 24

# As a trick, let's reshape this 4D array into a 2D array.
# We can "flatten" the first two dimensions to create a 2D array of shape (4, 12)
array_reshaped_4d = array_4d.reshape(4, 12)
print("\nReshaped 4D array into 2D (4x12):\n", array_reshaped_4d)

# Just to remind you: .reshape() can be very useful for adjusting the dimensions of arrays!

# For extra fun, try reshaping the 4D array into different shapes and see how the elements align.

# 4D arrays and higher can become tricky to visualize, but these tricks will help students understand!

# Please note: We used .shape and .reshape() a lot here to show how dimensions change.
# This is a fundamental skill when working with higher-dimensional arrays in any library, including TensorFlow!

# Finally, let's summarize:
# 1D: A simple array or vector.
# 2D: A matrix (rows and columns).
# 3D: A stack of matrices.
# 4D: A stack of 3D arrays!

# Thanks for following along! Practice is key to mastering multidimensional arrays. Keep going!
