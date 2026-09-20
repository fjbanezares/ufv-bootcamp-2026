# Importing the NumPy library. NumPy provides powerful operations for numerical and array-based computations.
import numpy as np

# Let's start with a simple 3x3 matrix 'a' for demonstration.
# We'll explore how broadcasting works and how to perform operations with different shapes.
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Broadcasting in NumPy allows arrays of different shapes to be combined element-wise.
# Broadcasting aligns the shapes in such a way that element-wise operations are performed.

# Example 1: Element-wise division using broadcasting
# Dividing each element of 'a' by a 3x3 matrix of 9s.
# Please note that the matrix of 9s can be a single scalar as well (i.e., a constant broadcasted across the array).
b = np.array([[9, 9, 9], [9, 9, 9], [9, 9, 9]])
normalized_a = a / b  # Element-wise division (broadcasting example).
print("Element-wise division result (normalization):\n", normalized_a)

# Example 2: Element-wise multiplication with broadcasting
# We can multiply specific columns of 'a' by different values.
# The right-hand matrix has the same number of columns as 'a', but only one row, so it's broadcasted to match.
multiplying_columns = a * np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])  # Element-wise column multiplication.
print("Multiplying columns using broadcasting:\n", multiplying_columns)

# Example 3: Row-wise normalization using broadcasting
# Dividing each row of 'a' by a corresponding row vector. This is also an example of broadcasting.
# Here, the matrix on the right has the same number of rows as 'a', but only one column.
row_wise_normalized = a / np.array([[3], [6], [9]])
print("Row-wise normalization using broadcasting:\n", row_wise_normalized)

# Please note that broadcasting simplifies operations and reduces the need for explicit loops.

# Outer product example:
# The outer product is the result of multiplying each element of one vector with each element of another.
# NumPy allows us to easily compute the outer product using broadcasting.
v1 = np.array([1, 2, 3])  # A column vector
v2 = np.array([1, 2, 3])  # A row vector

# The outer product of two vectors creates a matrix.
outer_product = np.outer(v1, v2)  # The outer product between two vectors.
print("Outer product of vectors v1 and v2:\n", outer_product)

# Dot (or inner) product example:
# The dot product is the sum of element-wise products of two vectors.
dot_product = np.dot(v1, v2)  # Dot product results in a scalar.
print("Dot (inner) product of vectors v1 and v2:", dot_product)

# Now, let's discuss transposing matrices.
# Transposing means swapping rows with columns. NumPy provides a handy function 'T' to transpose arrays.

# Transposing a 2D matrix
transposed_a = a.T  # Transposing the matrix 'a'.
print("Transposed matrix 'a':\n", transposed_a)

# Transposing a row vector
b = np.array([[1, 2, 3]])  # This is a row vector (1x3).
transposed_b = b.T  # Transposing the row vector will result in a column vector.
print("Transposed row vector 'b' to column vector:\n", transposed_b)

# Transposing doesn't work as expected for 1D arrays (no true rows or columns exist in 1D arrays).
c = np.array([1, 2, 3])  # 1D array
transposed_c = c.T  # Transposing a 1D array doesn't change anything.
print("Transposed 1D array 'c':", transposed_c)

# Please feel free to explore different broadcasting rules and operations in NumPy to understand how shapes align during operations.
# Remember, NumPy's broadcasting feature is powerful, but it's always good to ensure you're working with compatible shapes.

# In summary:
# - Broadcasting allows arrays of different shapes to interact during element-wise operations.
# - We explored the outer product, dot product, and transposition of arrays.
# Thanks for learning with us! I hope this gave you a deeper understanding of NumPy operations.
