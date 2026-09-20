# Python has two boolean values: True and False.
print(True)  # Output: True
print(False)  # Output: False

# The 'bool()' function is used to evaluate the truthiness or falsiness of a value.

# For numbers, 0 (zero) is considered False, while any other number is considered True.
print(bool(0))  # Output: False
print(bool(42))  # Output: True
print(bool(-1))  # Output: True
print(bool(0.0))  # Output: False
print(bool(0.207))  # Output: True
print(bool(-1.117))  # Output: True

# For lists, an empty list is considered False, while a list with at least one item is considered True.
print(bool([]))  # Output: False
print(bool([1, 5, 9]))  # Output: True

# For strings, an empty string is considered False, while a non-empty string is considered True.
print(bool(""))  # Output: False
print(bool("Spam"))  # Output: True

# Even if the string contains the word "False" or "True", it doesn't affect its truthiness.
# It's the presence of characters in the string that makes it True.
print(bool("False"))  # Output: True
print(bool("True"))  # Output: True
