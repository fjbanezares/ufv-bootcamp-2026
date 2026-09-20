# Understanding the None Type in Python

# Assigning None to a variable
a = None

# Checking if a variable has a value of None
# The most recommended way is using the 'is' operator
if a is None:
    print("'a' has a value of None!")

# It's not recommended to check using equality operator '=='
# Because a class can override its equality behavior.
# However, in the case of None, it will still work. But 'is' is more readable and safer.
if a == None:
    print("'a' is equal to None, but better use 'is' for checking.")

# When functions don't return anything, they actually return None by default.


def no_return_function():
    pass


result = no_return_function()
if result is None:
    print("The function returned None!")

# Remember, None is not:
# - an empty string
# - zero of any numeric type
# - empty collections (list, tuple, etc.)
# It's a datatype of its own: NoneType
