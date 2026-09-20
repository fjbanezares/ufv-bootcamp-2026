import copy

# Original list with mutable inner lists
original_list = [[1, 2, 3], [4, 5, 6]]

# Method 1: Slicing for shallow copy
shallow_copy_1 = original_list[:]
shallow_copy_1[0][0] = 'Modified'  # Modifies the inner list
print("Original after modifying shallow_copy_1:", original_list)  # Affected

# Resetting for next example
original_list = [[1, 2, 3], [4, 5, 6]]

# Method 2: Using list() for shallow copy
shallow_copy_2 = list(original_list)
shallow_copy_2[0][0] = 'Modified'
print("Original after modifying shallow_copy_2:", original_list)  # Affected

# Resetting for next example
original_list = [[1, 2, 3], [4, 5, 6]]

# Method 3: Using the copy() method for shallow copy
shallow_copy_3 = original_list.copy()
shallow_copy_3[0][0] = 'Modified'
print("Original after modifying shallow_copy_3:", original_list)  # Affected

# Resetting for next example
original_list = [[1, 2, 3], [4, 5, 6]]

# Method 4: Using copy.copy() for shallow copy
shallow_copy_4 = copy.copy(original_list)
shallow_copy_4[0][0] = 'Modified'
print("Original after modifying shallow_copy_4:", original_list)  # Affected

# Resetting for next example
original_list = [[1, 2, 3], [4, 5, 6]]

# Method 5: Using copy.deepcopy() for deep copy
deep_copy = copy.deepcopy(original_list)
deep_copy[0][0] = 'Modified'
print("Original after modifying deep_copy:", original_list)  # Not affected

# Resetting for next example
original_list = [[1, 2, 3], [4, 5, 6]]

# Method 6: Manual copy using a loop
manual_copy = []
for inner_list in original_list:
    manual_copy.append(inner_list.copy())  # Creates shallow copies of each inner list

manual_copy[0][0] = 'Modified'
print("Original after modifying manual_copy:", original_list)  # Not affected
print("Copy after modifying manual_copy:", manual_copy)  #  affected

# But what if we go deeper...Resetting for next example
original_list = [[[1,1,1], 2, 3], [4, 5, 6]]

# Method 7: show how delicate this is
manual_copy = []
for inner_list in original_list:
    manual_copy.append(inner_list.copy())  # Creates shallow copies of each inner list

manual_copy[0][0][0] = 'Modified' # Here we go DEEP
print("Original after EVILISH modifying manual_copy:", original_list)  #  affected
print("Copy after EVILISH modifying manual_copy:", manual_copy)  #  affected

# Resetting for next example ... Go deep but  with deepcopy() to see how it behaves...
original_list = [[[1,1,1], 2, 3], [4, 5, 6]]

# Method 8: Test copy.deepcopy() for Evil
deep_copy = copy.deepcopy(original_list)
deep_copy[0][0][0] = 'Modified'
print("Original after EVILISH modifying deep_copy:", original_list)  # Not  affected which means it is safe uses recursion to do deep_copy until only has references to immutables
print("Copy after EVILISH modifying deep_copy:", manual_copy)  #  affected

# Recap:
# Shallow copies (slicing, list(), copy(), copy.copy()) share references of inner lists.
# Deep copies (copy.deepcopy()) do not share references, fully independent copies.
# Manually copying can control copy depth but can be complex and error-prone.

# THANK YOU for exploring these examples!
# PLEASE ensure you understand the difference between these copies to avoid bugs.

# Additional Considerations for Shallow Copies
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy_5 = original_list[:]

# Changing the reference in shallow_copy_5 won't affect the original list
shallow_copy_5[0] = ['New', 'List']
print("Original list after reassigning a shallow copy element:", original_list)  # Not affected

# However, changing the inner list in shallow_copy_5 affects the original list
shallow_copy_5[1][0] = 'Still Affected'
print("Original list after modifying inner list of shallow copy:", original_list)  # Affected

# PLEASE REMEMBER that shallow copies are only safe when your lists contain immutable objects!
# THANK YOU for paying attention to these nuances to write more robust Python code.

# Original list with mutable inner lists
original_list = [[1, 2, 3], [4, 5, 6]]

# Method 1: Slicing for shallow copy
shallow_copy_1 = original_list[:]
shallow_copy_1[0] = [7,7,7]  # Modifies the inner list
print("Original after changing first element:", original_list)  # Not Affected
print("How copy looks like:", shallow_copy_1)  #  Affected


# Original list with nested mutable objects
original_list = [[[1, 2, 3], [4, 5, 6]], [7, 8, 9]]

# Manual Deep Copy using Recursion
def manual_deepcopy(item):
    """Recursively deep copies a list or dictionary"""
    # Check if the item is a list
    if isinstance(item, list):
        # Create a new list to hold the copied items
        return [manual_deepcopy(element) for element in item]
    # Check if the item is a dictionary
    elif isinstance(item, dict):
        # Create a new dictionary to hold the copied key-value pairs
        return {key: manual_deepcopy(value) for key, value in item.items()}
    else:
        # If the item is neither a list nor a dictionary, return it as it is (base case)
        return item

# Method 1: Using custom manual deep copy
manual_copy_recursive = manual_deepcopy(original_list)
manual_copy_recursive[0][0][0] = 'Modified Recursively'
print("Original after modifying manual_copy_recursive:", original_list)  # Not affected
print("Copy after modifying manual_copy_recursive:", manual_copy_recursive)  # Affected

# Resetting for next example
original_list = [[[1, 2, 3], [4, 5, 6]], [7, 8, 9]]

# Method 2: Using copy.deepcopy() for comparison
deep_copy = copy.deepcopy(original_list)
deep_copy[0][0][0] = 'Modified with deepcopy'
print("Original after modifying deep_copy:", original_list)  # Not affected
print("Copy after modifying deep_copy:", deep_copy)  # Affected

# Recap of deep copying methods:
# - `manual_deepcopy()` uses recursion to ensure all nested lists and dictionaries are fully copied.
# - `copy.deepcopy()` is a built-in method that also uses a recursive approach to handle nested objects.
# - Both methods ensure that the original object remains unchanged when the copy is modified.

# THANK YOU for exploring the importance of deep copies with recursive functions!
# PLEASE remember that understanding these concepts is crucial for preventing unintended side effects in your code.

