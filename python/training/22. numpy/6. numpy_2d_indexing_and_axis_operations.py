# Import the necessary library for numerical computing
import numpy as np  # NumPy provides support for handling multi-dimensional arrays and performing numerical operations.

# Let's create a 2D array 'a' to demonstrate two-dimensional indexing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # This is a 3x4 matrix (3 rows, 4 columns)

# Indexing an element from the second row, third column.
element = a[1, 2]  # This accesses the element at row index 1 and column index 2 (0-based indexing).
print(f"The element at row 2, column 3 is: {element}")  # Expected Output: 7

# Extracting the entire second row (index 1) using slicing
second_row = a[1, :]  # This slices all columns from row 1.
print("Entire second row:", second_row)  # Expected Output: [5 6 7 8]

# Extracting the entire third column using slicing
third_column = a[:, 2]  # This slices all rows for column 2.
print("Entire third column:", third_column)  # Expected Output: [3 7 11]

# Please note, you can also slice a submatrix:
submatrix = a[:2, 1:3]  # This slices the first two rows and columns 1 and 2 (excluding column 3).
print("Submatrix (rows 1-2, columns 2-3):\n", submatrix)  # Expected Output: [[2 3] [6 7]]

# Here’s an important distinction: a **view** vs. a **copy** in NumPy.
# A view allows you to access and modify the data in the original array, while a copy creates a new array.

# Creating a view of the first row and modifying it
row_view = a[0, :]
row_view[0] = 100  # Change the first element of the view
print("Modified view:", row_view)  # Expected Output: [100 2 3 4]
print("Original array after modifying the view:\n", a)  # Notice the original array is also changed!

# If you want to avoid modifying the original array, use `.copy()`
row_copy = a[0, :].copy()  # This creates a copy of the first row
row_copy[0] = 1  # Modify the copy
print("Modified copy:", row_copy)  # Expected Output: [1 2 3 4]
print("Original array after modifying the copy:\n", a)  # The original array remains unaffected.

# Now let's talk about the axis argument in operations such as sum().
# The axis argument helps you define whether you want to operate across rows or columns.

# Sum of all elements in the array (no axis specified, it sums everything)
total_sum = a.sum()
print("Total sum of the array:", total_sum)  # Expected Output: 78 (sum of all elements in the matrix)

# Summing along columns (axis=0)
# Axis 0 means summing along the rows and collapsing the rows into one result per column.
column_sums = a.sum(axis=0)
print("Sum along columns:", column_sums)  # Expected Output: [115 18 21 24]

# Summing along rows (axis=1)
# Axis 1 means summing along the columns and collapsing the columns into one result per row.
row_sums = a.sum(axis=1)
print("Sum along rows:", row_sums)  # Expected Output: [109 26 42]

# Please try experimenting with different slicing and axis arguments to fully grasp these concepts!

# Summary:
# - We explored two-dimensional indexing and slicing, including the difference between views and copies.
# - We saw how the axis argument changes the behavior of operations like sum, either summing across rows or columns.
# Thanks for following along with the indexing and axis argument explanation in NumPy!
