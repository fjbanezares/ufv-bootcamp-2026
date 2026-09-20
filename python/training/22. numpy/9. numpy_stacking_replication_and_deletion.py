# Importing the NumPy library for array manipulation
import numpy as np

# Example 1: Horizontal stacking (hstack)
# Please note that horizontal stacking aligns the arrays side by side (along axis=1)
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
c = np.array([[1, 2], [3, 4], [5, 6]])

# Using np.hstack to horizontally stack arrays 'a' and 'c'.
# Arrays must have the same number of rows.
hstack_result = np.hstack((a, c))
print("Horizontally stacked arrays (hstack):\n", hstack_result)

# Example 2: Vertical stacking (vstack)
# Vertical stacking aligns arrays on top of each other, row by row (along axis=0)
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Using np.vstack to vertically stack arrays 'a' and 'b'.
# Arrays must have the same number of columns.
vstack_result = np.vstack((a, b))
print("Vertically stacked arrays (vstack):\n", vstack_result)

# Example 3: Stacking a 1D array with a 2D matrix using hstack
# Arrays must be aligned by rows, so we need to reshape the 1D array to a column vector.
d = np.array([1, 3, 5])  # 1D array
column_vector = d[:, np.newaxis]  # Reshaping into a column vector for alignment
hstack_with_1d = np.hstack((a, column_vector))
print("Horizontally stacked with 1D array (after reshaping to column):\n", hstack_with_1d)

# Example 4: Replicating arrays using tile and repeat
# np.tile repeats an array by creating copies of it in both row and column directions
a_tile = np.tile(a, (2, 3))  # Repeats 'a' 2 times along rows and 3 times along columns
print("Replicating array with np.tile:\n", a_tile)

# np.repeat repeats elements within an array along a specified axis
a_repeat = np.repeat(a, 3, axis=1)  # Repeats each element in 'a' 3 times along columns
print("Repeating elements with np.repeat (axis=1):\n", a_repeat)

# We can also repeat along the rows (axis=0)
a_repeat_rows = np.repeat(a, 2, axis=0)  # Repeats rows twice
print("Repeating rows with np.repeat (axis=0):\n", a_repeat_rows)

# Example 5: Deleting specific columns or rows from an array using np.delete
# Deleting the second and fourth columns from 'a'
a_delete_cols = np.delete(a, [1, 3], axis=1)  # axis=1 means column-wise deletion
print("Array after deleting columns 2 and 4:\n", a_delete_cols)

# Deleting the second row from 'a'
a_delete_rows = np.delete(a, 1, axis=0)  # axis=0 means row-wise deletion
print("Array after deleting row 2:\n", a_delete_rows)

# Example 6: Combining 1D arrays and matrices using column_stack
# np.column_stack stacks 1D arrays as columns in a 2D array
e = np.array([1, 2, 3])
f = np.array([4, 5, 6])

# Stacking two 1D arrays to form a 2D array with two columns
column_stack_result = np.column_stack((e, f))
print("Column-stacked 1D arrays:\n", column_stack_result)

# Example 7: Advanced deletion using slice objects
# Deleting a slice of columns (from index 1 to index -1)
a_delete_slice = np.delete(a, slice(1, -1), axis=1)  # Deletes columns 2 to second-last
print("Array after deleting a slice of columns (2 to 2nd last):\n", a_delete_slice)

# Deleting rows using a slice
a_delete_row_slice = np.delete(a, slice(1, 3), axis=0)  # Deletes rows 2 and 3
print("Array after deleting a slice of rows (2 and 3):\n", a_delete_row_slice)
