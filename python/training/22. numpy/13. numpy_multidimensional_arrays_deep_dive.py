import numpy as np  # NumPy is the foundation library for multidimensional arrays

# Step 1: Create a 1D array (vector)
# This is a simple one-dimensional array. Think of it as a row of data.
one_d_array = np.array([1, 2, 3, 4, 5])

print("1D array (vector):\n", one_d_array)
print("Shape of 1D array:", one_d_array.shape)  # Shape will be (5,), which means it's 1-dimensional with 5 elements
print("===================================")

# Step 2: Create a 2D array (matrix)
# A 2D array can be thought of as a table with rows and columns (like a spreadsheet).
two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("2D array (matrix):\n", two_d_array)
print("Shape of 2D array:", two_d_array.shape)  # Shape will be (3, 3), meaning 3 rows and 3 columns
print("===================================")

# Step 3: Create a 3D array (tensor)
# A 3D array can be visualized as a cube of data, like stacking multiple 2D arrays on top of each other.
three_d_array = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # First 2D matrix
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],  # Second 2D matrix
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]  # Third 2D matrix
])

print("3D array (tensor):\n", three_d_array)
print("Shape of 3D array:", three_d_array.shape)  # Shape will be (3, 3, 3), which means 3 layers of 3x3 matrices
print("===================================")

# Step 4: Reshaping arrays
# You can reshape arrays into different dimensions while keeping the same number of elements.
reshaped_array = one_d_array.reshape(5, 1)  # Change from shape (5,) to shape (5, 1) (a column vector)

print("Reshaped 1D array into 2D array:\n", reshaped_array)
print("Shape of reshaped array:", reshaped_array.shape)  # Shape is now (5, 1)
print("===================================")

# Step 5: Broadcasting
# Broadcasting allows NumPy to perform operations on arrays of different shapes in a smart way.
# Here's an example where we add a scalar to a 1D array, and NumPy broadcasts the scalar across the array.
broadcasted_array = one_d_array + 5  # Add 5 to every element in the array

print("Broadcasting example (adding 5 to each element):\n", broadcasted_array)
print("Shape remains:", broadcasted_array.shape)  # Shape stays the same as (5,)
print("===================================")

# Step 6: High-dimensional reshaping
# Let's take a 3D array and reshape it into a different 3D shape.
reshaped_three_d_array = three_d_array.reshape(9, 3, 1)  # Flatten the first two axes into 9, keeping the rest

print("Reshaped 3D array:\n", reshaped_three_d_array)
print("Shape of reshaped 3D array:", reshaped_three_d_array.shape)  # Shape will be (9, 3, 1)
print("===================================")

# Step 7: Using .ravel() to flatten an array
# You can use `.ravel()` to flatten any multidimensional array into a 1D array.
flattened_array = three_d_array.ravel()

print("Flattened 3D array into 1D array using ravel():\n", flattened_array)
print("Shape of flattened array:", flattened_array.shape)  # Shape will be (27,)
print("===================================")

# Step 8: Working with TensorFlow
# TensorFlow is built on top of NumPy, and it handles tensors, which are essentially multidimensional arrays.
# Let's create a tensor using TensorFlow.
import tensorflow as tf

tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float32)  # 2D tensor (matrix)

print("TensorFlow Tensor:\n", tensor)
print("Shape of TensorFlow tensor:", tensor.shape)  # Shape will be (3, 2)
print("===================================")

# TensorFlow allows you to reshape tensors in the same way as NumPy.
reshaped_tensor = tf.reshape(tensor, [2, 3])  # Reshaping from (3, 2) to (2, 3)

print("Reshaped TensorFlow tensor:\n", reshaped_tensor)
print("Shape of reshaped tensor:", reshaped_tensor.shape)  # Shape is now (2, 3)
print("===================================")

# Step 9: Practical use case: Image Data in PyCharm/TensorFlow
# Often in deep learning, you'll work with image data, which is typically represented as 4D arrays (batch, height, width, channels).
# Here's an example of how a 4D image tensor might look.

# Create a random 4D tensor representing a batch of 2 images (height 64, width 64, 3 color channels)
image_data = np.random.rand(2, 64, 64, 3)

print("Image data tensor (4D):\n", image_data)
print("Shape of image data tensor:", image_data.shape)  # Shape will be (2, 64, 64, 3)
print("===================================")

# Let's reshape it for some operations (e.g., flattening the spatial dimensions)
reshaped_image_data = image_data.reshape(2, -1)  # Reshape each image into a 1D array of pixels

print("Reshaped image data into 2D array (batch size, flattened pixels):\n", reshaped_image_data)
print("Shape after reshaping:", reshaped_image_data.shape)  # Shape will be (2, 12288), where 12288 = 64*64*3
print("===================================")

# Step 10: Useful trick: Checking if reshaping is possible
# NumPy provides a very useful way to check if you can reshape an array without changing its data.
try:
    new_shape = (5, 10)  # Arbitrary shape that doesn't match the total number of elements
    invalid_reshaped_array = one_d_array.reshape(new_shape)
except ValueError as e:
    print(f"Reshaping failed with error: {e}")
