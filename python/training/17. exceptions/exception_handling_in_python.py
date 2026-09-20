# This script demonstrates various aspects of exception handling in Python
# including try, except, else, finally, raising exceptions, and custom exceptions.

# Let's start with a simple example of exception handling.

try:
    # TRY BLOCK: This is where we put code that might throw an exception.
    # Dividing by zero will raise a ZeroDivisionError.
    x = 1 / 0
except ZeroDivisionError:
    # EXCEPT BLOCK: This is where we handle the exception.
    # If a ZeroDivisionError occurs, this block will run.
    print("Cannot divide by zero!")  # Output: Cannot divide by zero!

# Now, let's see how we can catch multiple exceptions.

try:
    # Here, we'll try to perform multiple operations.
    # The following operation raises a TypeError.
    result = '2' + 2
except (TypeError, ValueError) as e:
    # This except block will catch both TypeError and ValueError.
    # `as e` allows us to access the exception object itself.
    print(f"Error occurred: {e}")  # Output: Error occurred: can only concatenate str (not "int") to str
except IndexError:
    # A different except block for a different type of error.
    print("Index out of range error")

# PLEASE NOTE: The second except block won't be executed because the first one already caught the exception.

# Using ELSE with TRY/EXCEPT
try:
    # No error in this block, so the except block will be skipped.
    y = 10 / 2  # No division by zero here.
    print(f"Result: {y}")  # Output: Result: 5.0
except ZeroDivisionError:
    print("This won't be printed because there's no exception.")
else:
    # ELSE block runs if no exception was raised in the try block.
    print("No errors occurred. Great!")  # Output: No errors occurred. Great!

# Using FINALLY with TRY/EXCEPT
try:
    # This will raise a KeyError since 'missing_key' is not in the dictionary.
    sample_dict = {"key": "value"}
    print(sample_dict["missing_key"])
except KeyError as e:
    print(f"KeyError encountered: {e}")  # Output: KeyError encountered: 'missing_key'
finally:
    # FINALLY block always runs, regardless of whether an exception occurred or not.
    print("This runs no matter what!")  # Output: This runs no matter what!

# THANK YOU for following along! Let's move on to RAISING EXCEPTIONS manually.

def set_age(age):
    if age < 0:
        # RAISING an exception manually.
        # This is useful for enforcing certain conditions in your code.
        raise ValueError("Age cannot be negative!")
    return f"Age is set to {age}"

try:
    set_age(-5)  # This will raise a ValueError.
except ValueError as e:
    print(f"An error occurred: {e}")  # Output: An error occurred: Age cannot be negative!

# PLEASE NOTE: Raising exceptions helps prevent invalid data from causing problems later.

# Creating CUSTOM EXCEPTIONS by subclassing the Exception class.
class NegativeAgeError(Exception):
    """Custom exception for invalid age input."""
    pass

def set_age_improved(age):
    if age < 0:
        # Raising a custom exception
        raise NegativeAgeError("Age cannot be negative!")
    return f"Age is set to {age}"

try:
    set_age_improved(-3)  # This will raise a NegativeAgeError.
except NegativeAgeError as e:
    print(f"Custom error occurred: {e}")  # Output: Custom error occurred: Age cannot be negative!

# Assertions can also be used for error checking.
x = 10
assert x == 10, "Value is not 10"  # This assertion passes, no error.
assert x > 10, "Value is not greater than 10"  # This will raise an AssertionError.

# PLEASE USE assertions wisely; they should not be used for handling runtime errors.

# THANK YOU for exploring these aspects of exception handling in Python!
