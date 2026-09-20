# Importing necessary libraries
import numpy as np  # NumPy for handling arrays and mathematical operations.
import pandas as pd  # Pandas for more advanced data handling, especially Series and DataFrames.

# Create a NumPy array of numbers
arr = np.array([1, 2, 3])  # This is a simple NumPy array containing three elements: 1, 2, and 3.

# Finding the maximum value in the array
max_value = np.max(arr)  # np.max() returns the largest value in the array.
print(f"The maximum value is: {max_value}")  # Expected Output: 3

# Finding the minimum value in the array
min_value = np.min(arr)  # np.min() returns the smallest value in the array.
print(f"The minimum value is: {min_value}")  # Expected Output: 1

# Finding the index of the maximum value in the array
argmax_value = np.argmax(arr)  # np.argmax() returns the index of the largest value.
print(f"The index of the maximum value is: {argmax_value}")  # Expected Output: 2 (0-based index)

# Finding the index of the minimum value in the array
argmin_value = np.argmin(arr)  # np.argmin() returns the index of the smallest value.
print(f"The index of the minimum value is: {argmin_value}")  # Expected Output: 0 (0-based index)

# Sum of all elements in the array
sum_value = np.sum(arr)  # np.sum() returns the sum of all elements in the array.
print(f"The sum of all elements is: {sum_value}")  # Expected Output: 6

# Variance of the array
variance_value = np.var(arr)  # np.var() calculates the variance of the array.
print(f"The variance is: {variance_value:.2f}")  # Expected Output: 0.67

# Standard deviation of the array
std_value = np.std(arr)  # np.std() calculates the standard deviation, by default population standard deviation.
print(f"The standard deviation is: {std_value:.2f}")  # Expected Output: 0.82

# Standard deviation with Bessel's correction (ddof=1), for sample standard deviation
sample_std_value = np.std(arr, ddof=1)  # ddof=1 applies Bessel's correction, used in sample standard deviation.
print(f"The sample standard deviation is: {sample_std_value:.2f}")  # Expected Output: 1.00

# Now, let's use Pandas Series and observe the behavior of std()

# Creating a Pandas Series
series = pd.Series([1, 2, 3])  # A Pandas Series is a one-dimensional array-like object with labeled indices.

# Standard deviation using Pandas (ddof=1 by default)
series_std = series.std()  # Pandas' std() method automatically applies Bessel's correction (ddof=1).
print(f"The standard deviation from Pandas Series is: {series_std:.2f}")  # Expected Output: 1.00

# Observing how rounding works with NumPy
# We can round, floor, and ceil arrays
arr2 = np.array([1.1, 1.5, 1.9, 2.5])

# Using np.floor() - rounds values down to the nearest integer
floor_arr = np.floor(arr2)
print(f"Floored array: {floor_arr}")  # Expected Output: [1. 1. 1. 2.]

# Using np.ceil() - rounds values up to the nearest integer
ceil_arr = np.ceil(arr2)
print(f"Ceiled array: {ceil_arr}")  # Expected Output: [2. 2. 2. 3.]

# Using np.round() - rounds values to the nearest integer
round_arr = np.round(arr2)
print(f"Rounded array: {round_arr}")  # Expected Output: [1. 2. 2. 2.]
