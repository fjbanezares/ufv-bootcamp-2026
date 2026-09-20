# Import numpy to start working with arrays
import numpy as np

# --- Functions that create arrays filled with constants ---
# np.zeros: Create an array filled with zeros.
# np.ones: Create an array filled with ones.
# np.empty: Create an uninitialized array (values depend on memory state).
# np.full: Create an array filled with a specific value.

# Create a basic array for comparison
a = np.array([1, 2, 3])

# Creating an array of zeros with 3 elements
zeros_array = np.zeros(3)  # Output: array([0., 0., 0.])
print("Array of zeros:", zeros_array)

# Create a zero array with the same shape as 'a'
zeros_like_a = np.zeros_like(a)  # Matches shape and type of 'a'
print("Zeros like array 'a':", zeros_like_a)

# Creating an array of ones with 3 elements
ones_array = np.ones(3)  # Output: array([1., 1., 1.])
print("Array of ones:", ones_array)

# Create a ones array with the same shape as 'a'
ones_like_a = np.ones_like(a)  # Matches shape and type of 'a'
print("Ones like array 'a':", ones_like_a)

# Creating an uninitialized array with 3 elements
# WARNING: np.empty does not initialize the array, so it may contain garbage values.
empty_array = np.empty(3)
print("Uninitialized (empty) array:", empty_array)

# Create an empty array with the same shape as 'a'
empty_like_a = np.empty_like(a)
print("Empty like array 'a' (garbage values):", empty_like_a)

# Creating an array filled with a constant value (7.0) with 3 elements
full_array = np.full(3, 7.0)  # Output: array([7., 7., 7.])
print("Array filled with 7.0:", full_array)

# Create a full array with the same shape as 'a'
full_like_a = np.full_like(a, 7)  # All elements filled with the constant 7
print("Full like array 'a' with constant 7:", full_like_a)


# --- Indexing and Slicing Arrays (Fancy Indexing and Slicing) ---
# np.arange: Creates an array of evenly spaced values.
# Slicing: Extract parts of arrays.
# Fancy indexing: Extract multiple specific indices.

# Create an array with numbers from 1 to 5
arr = np.arange(1, 6)
print("\nOriginal array:", arr)

# Accessing a single element (index 1)
single_element = arr[1]  # Access the second element (index starts at 0)
print("Single element at index 1:", single_element)

# Slicing: Getting a subset of the array (elements from index 2 to 4)
slice_arr = arr[2:4]  # Output: array([3, 4]), note that the upper bound is exclusive
print("Slice from index 2 to 4 (exclusive):", slice_arr)

# Fancy indexing: Selecting multiple specific elements (at index 1, 3, and 4)
fancy_index = arr[[1, 3, 4]]  # Output: array([2, 4, 5])
print("Fancy indexing with indices [1, 3, 4]:", fancy_index)

# Negative indexing: Get the last two elements using negative indices
negative_slice = arr[-2:]  # Output: array([4, 5])
print("Negative slice (last two elements):", negative_slice)

# Using step in slicing: Extract every second element
step_slice = arr[::2]  # Output: array([1, 3, 5])
print("Step slicing (every second element):", step_slice)

# Modifying part of the array (slicing modifies the original array)
arr[2:4] = 0  # Set elements at index 2 and 3 to 0
print("Modified array after setting index 2:4 to 0:", arr)


# --- Creating sequences with np.arange and np.linspace ---
# np.arange: Returns evenly spaced values within a given range.
# np.linspace: Returns evenly spaced numbers over a specified range.

# Creating an array with np.arange (values from 0 to 5, exclusive)
arange_arr = np.arange(6)  # Output: array([0, 1, 2, 3, 4, 5])
print("\nArray created with np.arange (0 to 5):", arange_arr)

# Creating an array with np.arange (start at 2, stop at 6)
arange_arr_2 = np.arange(2, 6)  # Output: array([2, 3, 4, 5])
print("Array created with np.arange (2 to 6):", arange_arr_2)

# Creating an array with np.arange with a step (from 1 to 6, step 2)
arange_step = np.arange(1, 6, 2)  # Output: array([1, 3, 5])
print("Array created with np.arange (1 to 6, step 2):", arange_step)

# Creating evenly spaced values with np.linspace (from 0 to 0.5, 6 values)
linspace_arr = np.linspace(0, 0.5, 6)  # Output: array([0. , 0.1, 0.2, 0.3, 0.4, 0.5])
print("Array created with np.linspace (0 to 0.5, 6 values):", linspace_arr)

# --- Additional examples ---
# Remember that np.linspace is useful when you need a specific number of points between a range.
# np.arange is useful when you need a range of values with a defined step (integers or floats).
