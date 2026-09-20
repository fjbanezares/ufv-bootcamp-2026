# Thank you for following along! Let's start by importing the necessary libraries.

import numpy as np  # NumPy is a powerful library for numerical computing in Python.

# Let's create a 2D array (matrix) using np.array().
# This array will have two rows and three columns, as you can see in the shape of the data.
a = np.array([[1, 2, 3], [4, 5, 6]])  # A simple 2x3 matrix

# Let's inspect the dtype (data type) and shape of the array.
print("Data type of 'a':", a.dtype)  # Expected Output: int32 (or depending on your environment)
print("Shape of 'a':", a.shape)  # Expected Output: (2, 3) which means 2 rows, 3 columns

# We can also find the length of the first dimension (number of rows) in the array using len().
print("Number of rows (len(a)):", len(a))  # Expected Output: 2

# Please note that NumPy offers various functions for creating arrays with specific patterns.
# For instance, you can create an array filled with zeros of a specific shape using np.zeros().

# Create a 3x2 matrix filled with zeros
zeros_matrix = np.zeros((3, 2))
print("3x2 matrix filled with zeros:\n", zeros_matrix)

# Similarly, you can create a matrix filled with ones.
ones_matrix = np.ones((3, 2))
print("3x2 matrix filled with ones:\n", ones_matrix)

# Please try using np.full() to create a matrix filled with a specific number, such as 7.
full_matrix = np.full((3, 2), 7)
print("3x2 matrix filled with 7s:\n", full_matrix)

# Thank you for exploring matrices with us! Now let's move on to random number generation.
# In NumPy, random numbers can be generated using old-style or new-style methods.
# Let's first check out the old-style approach.

# Old-style random number generation (simpler, but less flexible)
random_int_matrix = np.random.randint(0, 10, (3, 2))  # Generates random integers between 0 and 10 (exclusive)
print("Random integer matrix (old style):\n", random_int_matrix)

# np.random.rand generates random floats in the range [0, 1).
random_float_matrix = np.random.rand(3, 2)
print("Random float matrix (old style):\n", random_float_matrix)

# np.random.randn generates random floats from the standard normal distribution.
random_normal_matrix = np.random.randn(3, 2)
print("Random normal matrix (old style):\n", random_normal_matrix)

# Now let's use the new-style random number generation approach, which is more flexible.
rng = np.random.default_rng()  # Create a random number generator (RNG) object

# Generate integers with the new-style approach.
new_random_int_matrix = rng.integers(0, 10, (3, 2))
print("Random integer matrix (new style):\n", new_random_int_matrix)

# Generate random floats in the range [0, 1) with the new-style approach.
new_random_float_matrix = rng.random((3, 2))
print("Random float matrix (new style):\n", new_random_float_matrix)

# You can also generate numbers from a normal distribution using the new-style RNG.
new_random_normal_matrix = rng.standard_normal((3, 2))
print("Random normal matrix (new style):\n", new_random_normal_matrix)

# As you can see, the new-style approach gives you more control over the random number generation process.
# Please feel free to experiment further with these functions!

# Finally, let's summarize the important points:
# - We explored matrix creation using np.array(), np.zeros(), np.ones(), and np.full().
# - We also compared old-style and new-style random number generation in NumPy.

# Thanks for your time! Enjoy working with NumPy matrices and random numbers.