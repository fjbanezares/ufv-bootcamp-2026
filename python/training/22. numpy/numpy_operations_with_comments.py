# Let's start by importing numpy
import numpy as np

# --- Basic operations with matrices ---
# Create a simple 1D array (or vector) with two elements
matrix = np.array([1, 2])

# Addition with a scalar
# We're adding 3 to each element of the array
result_add = matrix + 3  # This will give us [4, 5]
print("Addition with a scalar 3:", result_add)

# Subtraction with a scalar
# Subtracting 3 from each element
result_sub = matrix - 3  # This will give us [-2, -1]
print("Subtraction with a scalar 3:", result_sub)

# Multiplication with a scalar
# Multiplying each element by 3
result_mult = matrix * 3  # This will give us [3, 6]
print("Multiplication with a scalar 3:", result_mult)

# Division with a scalar
# Dividing each element by 3, note the results are float64 by default
result_div = matrix / 3  # This will give us [0.33, 0.67]
print("Division with a scalar 3:", result_div)

# Integer (floor) division with a scalar
# Dividing each element by 2 using integer division (//)
result_int_div = matrix // 2  # This will give us [0, 1]
print("Integer division with 2:", result_int_div)

# Exponentiation
# Each element raised to the power of 2
result_exp = np.array([3, 4]) ** 2  # This will give us [9, 16]
print("Exponentiation of [3, 4] to the power of 2:", result_exp)

# --- More intuitive manipulation with lists vs NumPy arrays ---
# Example with a Python list
a = [1, 2, 3]
# Doubling each element using list comprehension (similar to loops)
list_result = [q * 2 for q in a]  # This is the traditional Python way
print("Doubling each element in list:", list_result)

# The same operation with NumPy
a_np = np.array([1, 2, 3])
numpy_result = a_np * 2  # In NumPy, operations are element-wise by default
print("Doubling each element in NumPy array:", numpy_result)

# Adding two Python lists
b = [4, 5, 6]
list_add_result = [q + r for q, r in zip(a, b)]  # Element-wise addition for lists
print("Adding two Python lists element-wise:", list_add_result)

# Adding two NumPy arrays
b_np = np.array([4, 5, 6])
numpy_add_result = a_np + b_np  # Much simpler and faster with NumPy
print("Adding two NumPy arrays element-wise:", numpy_add_result)

# --- Performance comparison: Python list vs NumPy array ---
# Python lists allow heterogeneous data types and dynamic size but are slower
# NumPy arrays are homogenous (same data type) and faster due to lower memory overhead

# Example creating an array and a list of the same size
python_list = [1, 2, 3, 4, 5, 6]
numpy_array = np.array([1, 2, 3, 4, 5, 6])

# Appending is faster with Python lists, but operations like addition are much faster with NumPy
# Appending an element (O(1) for lists, O(n) for arrays)
python_list.append(7)  # Efficient append for lists
numpy_array = np.append(numpy_array, 7)  # More costly append for NumPy arrays
print("Appending in Python list:", python_list)
print("Appending in NumPy array:", numpy_array)

# --- Working with 1D arrays or vectors in NumPy ---
# Creating a 1D array (vector) using np.array
vector_a = np.array([1., 2., 3.])  # dtype is np.float64 by default
print("1D vector a:", vector_a)

# Create a 1D array of zeros with a specific dtype
vector_b = np.zeros(3, dtype=int)  # dtype is np.int32
print("1D vector of zeros with int dtype:", vector_b)

# Creating a zero array with the same shape as another array
vector_c = np.zeros_like(vector_a)  # Shape and dtype will match vector_a
print("1D vector of zeros matching the shape of vector_a:", vector_c)

# --- Example for working with larger matrices ---
# Creating a 2D matrix (matrix of shape 2x2)
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Adding two matrices element-wise
matrix_add = matrix_a + matrix_b  # Element-wise addition
print("Matrix addition (element-wise):\n", matrix_add)

# Multiplying two matrices element-wise
matrix_mult = matrix_a * matrix_b  # Element-wise multiplication
print("Matrix multiplication (element-wise):\n", matrix_mult)

# Matrix multiplication (dot product)
matrix_dot = np.dot(matrix_a, matrix_b)
print("Matrix dot product:\n", matrix_dot)

# --- Additional Tips ---
# NumPy arrays are efficient for numerical data and operations.
# Performance improves for large datasets or numerical calculations.

# --- End of Code ---
# Thanks for running this script! Please try experimenting with different arrays.
# Don't forget that NumPy is super powerful when working with big data sets!