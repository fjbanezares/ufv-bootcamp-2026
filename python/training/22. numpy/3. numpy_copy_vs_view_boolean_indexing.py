# Let's import numpy as usual
import numpy as np

# --- Copy vs Views ---
# Understanding the difference between copies and views in NumPy is essential
# because views don't create a new copy of the data but rather point to the same memory,
# meaning that modifying a view modifies the original array. Copies, however, are independent.

# Create a NumPy array
a = np.array([1, 2, 3])

# --- Scenario 1: Assigning an array to another variable (No Copy) ---
# In this case, 'b' is just a reference to 'a', not a copy.
b = a
# Any modification to 'b' will also affect 'a' since both point to the same data in memory.

b[0] = 100  # Let's modify the first element of 'b'
print("Array a after modifying b:", a)  # Notice that 'a' is also modified to [100, 2, 3]
# Please note: 'b' is not a copy; it’s just a reference to 'a'.

# --- Scenario 2: Creating a slice of the array (No Copy - A View) ---
# A slice of a NumPy array does NOT create a copy; it creates a view.
c = a[:]
# 'c' points to the same memory location as 'a'. Modifying 'c' will modify 'a'.

c[1] = 200  # Modifying the second element of 'c'
print("Array a after modifying slice c:", a)  # Notice that 'a' is modified to [100, 200, 3]
# Please note: Slicing creates a view, not a copy.

# --- Scenario 3: Using the copy method (Copy) ---
# Here, we create a true copy of 'a', independent of 'a' itself.
d = a.copy()
# Changes to 'd' will not affect 'a', and vice versa, because they are stored in different memory locations.

d[2] = 300  # Modifying the third element of 'd'
print("Array a after modifying copy d:", a)  # 'a' remains unchanged: [100, 200, 3]
print("Array d:", d)  # 'd' is [100, 200, 300]
# Please note: Using 'copy()' creates a separate copy in memory.

# --- Important Lessons on Copies and Views ---
# When working with large datasets, it is important to know when you're working with views or copies,
# especially if you want to avoid unintended side effects or want to save memory.

# ALWAYS use `copy()` when you need an independent copy of the data and don't want the original array modified.
# Be mindful when slicing or assigning arrays because this will often create views, not copies!

# --- Boolean Indexing ---
# Boolean indexing allows you to select elements from an array based on conditions.
# This creates a new array (it is a copy, not a view), so you won't affect the original array unless you assign back.

a = np.array([1, 2, 3, 4, 5, 6, 7])

# Condition: selecting elements greater than 5
bool_arr = a > 5
print("Boolean array (a > 5):", bool_arr)  # Output: [False False False False False  True  True]

# Use this boolean array to select elements that satisfy the condition
selected_elements = a[a > 5]
print("Elements greater than 5:", selected_elements)  # Output: [6, 7]

# Please note: Boolean indexing creates a copy of the array with the selected elements.

# --- Modifying elements based on a condition (in-place modification) ---
# You can use boolean indexing to modify parts of the array.
a[a > 5] = 0  # Setting all elements greater than 5 to 0
print("Array after setting elements greater than 5 to 0:", a)  # Output: [1 2 3 4 5 0 0]
# Please note: Here we modify 'a' directly by using boolean indexing.

# --- np.any() and np.all() ---
# np.any(): Returns True if at least one element satisfies the condition.
print("Are any elements greater than 5?", np.any(a > 5))  # Output: False (since we set them to 0)

# np.all(): Returns True if all elements satisfy the condition.
print("Are all elements greater than 5?", np.all(a > 5))  # Output: False

# --- np.where() ---
# np.where() is a more explicit way to select elements or assign values based on a condition.
# It returns indices of the elements that satisfy the condition or can be used to replace values conditionally.

# Example: Get the indices of elements greater than 5
indices_where = np.where(a > 5)
print("Indices where a > 5:", indices_where)  # Output: (array([], dtype=int64),) because no element is > 5

# Using np.where to create a new array with conditional values
new_arr = np.where(a >= 5, 1, 0)  # Set elements >= 5 to 1, else 0
print("Array with np.where (a >= 5 -> 1, else 0):", new_arr)  # Output: [0 0 0 0 1 0 0]

# --- np.nonzero() ---
# np.nonzero() returns the indices of the non-zero elements in the array.
nonzero_indices = np.nonzero(a)
print("Indices of non-zero elements in array 'a':", nonzero_indices)  # Output: (array([0, 1, 2, 3, 4]),)

# --- np.clip() ---
# np.clip() limits the values in an array to a given range.
# Any value below the lower limit is set to the lower bound, and any value above the upper limit is set to the upper bound.

# Clipping values between 2 and 5
clipped_arr = np.clip(a, 2, 5)
print("Array after clipping values between 2 and 5:", clipped_arr)  # Output: [2 2 3 4 5 2 2]
# Please note: Values < 2 are set to 2, and values > 5 are set to 5.


# --- Conclusion ---
# Thank you for following through this exploration of views, copies, and boolean indexing in NumPy.
# Remember that slicing creates a view, meaning changes to the view affect the original array.
# Always use the `copy()` method when you want to ensure changes don't affect the original array.
# Boolean indexing creates a copy, which is a very powerful feature for selecting and modifying elements in an array.
# Functions like `np.where`, `np.nonzero`, and `np.clip` help in controlling and transforming data.
# Please experiment further with these concepts for a deeper understanding. Thanks for your attention!
