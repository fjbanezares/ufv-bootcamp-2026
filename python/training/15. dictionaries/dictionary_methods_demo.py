# Example of the update() method
# -----------------------------
# Merges two dictionaries. If keys overlap, values from the second dictionary are used.

# Initial dictionary
dict1 = {"apple": "fruit", "mango": "fruit"}

# Dictionary to be merged
dict2 = {"banana": "fruit", "broccoli": "green vegetable"}

# Using update() to merge dict2 into dict1
dict1.update(dict2)

# The output will have keys from both dict1 and dict2.
# If a key exists in both, the value from dict2 is used.
print("After update():", dict1)
# Output: {'apple': 'fruit', 'mango': 'fruit', 'banana': 'fruit', 'broccoli': 'green vegetable'}

# Example of the copy() method
# ----------------------------
# Returns a shallow copy of the dictionary.

dict3 = dict1.copy()  # Shallow copy of dict1
print("Shallow copy dict3:", dict3)

# Modifying the original dictionary doesn't affect the copy (since it's shallow).
dict1["apple"] = "modified fruit"
print("After modifying dict1:", dict1)
print("Shallow copy dict3 remains unchanged:", dict3)

# Risks of shallow copy:
# Shallow copies only copy the outermost level of a dictionary. If the dictionary has nested dictionaries (or lists),
# changes to the nested objects in the original dictionary will affect the shallow copy as well.
nested_dict = {"key1": {"subkey": "value"}}
shallow_copy = nested_dict.copy()

# Modifying the nested dictionary in the original dictionary affects the shallow copy.
nested_dict["key1"]["subkey"] = "modified value"
print("Original nested_dict:", nested_dict)
print("Shallow copy of nested_dict affected:", shallow_copy)

# To avoid this, we need a deep copy. Use deepcopy() from the copy module.
import copy
deep_copy = copy.deepcopy(nested_dict)

# Now modifying the original will not affect the deep copy.
nested_dict["key1"]["subkey"] = "deeply modified"
print("Original nested_dict after deep modification:", nested_dict)
print("Deep copy remains unchanged:", deep_copy)

# Example of setdefault() method
# ------------------------------
# If the key exists, returns the value. If the key doesn't exist, inserts the key with the specified value.

dict4 = {"apple": "fruit", "banana": "fruit"}

# The key 'grape' does not exist in dict4, so setdefault will add it with the value 'fruit'
dict4.setdefault("grape", "fruit")
print("After setdefault() for 'grape':", dict4)

# If the key already exists, setdefault returns the existing value and doesn't modify the dictionary.
dict4.setdefault("apple", "fruit")
print("After setdefault() for 'apple' (already exists):", dict4)