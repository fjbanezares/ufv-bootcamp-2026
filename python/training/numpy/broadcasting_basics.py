import numpy as np

# Example 1: Adding a 1D array to a 2D array
# Initialize 2D array A with shape (3, 4)
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Initialize 1D array B with shape (4,)
B = np.array([1, 0, 1, 0])

# Use broadcasting to add B to each row of A
# B gets virtually stretched to shape (3, 4) to match A
C = A + B
print("Example 1: C = A + B")
print(C)

# Example 2: Broadcasting with a Scalar
# Add a scalar to a 2D array
# The scalar gets broadcasted to all elements in the array
D = A + 1
print("\nExample 2: D = A + 1")
print(D)

# Example 3: More Complex Broadcasting
# Initialize a 3D array X with shape (3, 4, 2)
X = np.random.rand(3, 4, 2)

# Initialize a 2D array Y with shape (4, 2)
Y = np.random.rand(4, 2)

# Use broadcasting to add Y to each "layer" of X
# Y gets virtually stretched to shape (3, 4, 2) to match X
Z = X + Y
print("\nExample 3: Z = X + Y")
print(Z)


# Example 4: Fixed numbers for better understanding
# Initialize a 3D array X with shape (2, 2, 2) with fixed numbers
X_fixed = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Initialize a 2D array Y with shape (2, 2) with fixed numbers
Y_fixed = np.array([[1, 1], [1, 1]])

# Using broadcasting to add Y_fixed to each "layer" of X_fixed
# Y_fixed is virtually "stretched" to shape (2, 2, 2) to match X_fixed
Z_fixed = X_fixed + Y_fixed

print("\nExample 4: Z_fixed = X_fixed + Y_fixed")
print(Z_fixed)

# Example 5: Broadcasting with row vector
# Initialize a 1D array V with shape (4,)
V = np.array([1, 0, -1, 0])

# Use broadcasting to add V as a row to each row of A
# V gets virtually "stretched" to shape (3, 4) to match A
E = A + V
print("\nExample 5: E = A + V")
print(E)

# Example 6: Broadcasting with column vector
# Initialize a 1D array W with shape (3,)
W = np.array([1, 0, -1])

# Reshape W to be a column vector of shape (3, 1)
W = W[:, np.newaxis]

# Use broadcasting to add W as a column to each column of A
# W gets virtually "stretched" to shape (3, 4) to match A
F = A + W
print("\nExample 6: F = A + W")
print(F)
