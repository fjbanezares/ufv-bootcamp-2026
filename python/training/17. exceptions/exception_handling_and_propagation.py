# Let's start with a basic function that raises an exception when something goes wrong.
def divide(x, y):
    # Check if 'y' is zero to prevent a division by zero error.
    if y == 0:
        # Raising a ValueError if 'y' is zero.
        # This informs the caller that an invalid operation has been attempted.
        raise ValueError("Cannot divide by zero!")
    # If no exception, proceed with the division.
    return x / y

# Example 1: Handling an Exception
# Here, we will try to divide by zero and catch the exception.
try:
    result = divide(5, 0)  # This will raise a ValueError.
except ValueError as e:
    # Catching the ValueError and printing a user-friendly message.
    print(f"An error occurred: {e}")  # Output: An error occurred: Cannot divide by zero!

# THANK YOU for understanding that catching exceptions allows us to handle errors gracefully!

# Example 2: Handling the exception within the caller function.
# This shows how an exception can be passed up the call stack.
def safe_divide(x, y):
    try:
        # Attempt to perform the division.
        return divide(x, y)
    except ValueError as e:
        # Handle the exception, preventing the program from crashing.
        print(f"Handled in safe_divide: {e}")  # Output: Handled in safe_divide: Cannot divide by zero!

# Calling safe_divide to demonstrate exception handling.
safe_divide(10, 0)

# Example 3: Propagating an Exception Up the Call Stack
# This function does not handle the exception; it lets it propagate up.
def propagate_divide(x, y):
    # No try...except here, so any exception will propagate up to the caller.
    return divide(x, y)

# Top-level caller, which might be part of a larger application.
try:
    propagate_divide(10, 0)  # This will raise a ValueError.
except ValueError as e:
    # The exception is finally caught here, at the top level.
    print(f"An error reached the top level: {e}")  # Output: An error reached the top level: Cannot divide by zero!

# PLEASE notice how the exception bubbles up to the top, allowing higher levels to decide how to handle it.

# Example 4: Custom Exception to Represent a Specific Error Case
class NegativeNumberError(Exception):
    """Custom exception for handling negative numbers in our specific context."""
    pass

def process_number(n):
    # Raise a custom exception if the number is negative.
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    print(f"Processing number: {n}")

try:
    process_number(-5)  # This will raise NegativeNumberError.
except NegativeNumberError as e:
    print(f"Caught custom exception: {e}")  # Output: Caught custom exception: Negative numbers are not allowed!

# THANK YOU for recognizing the use of custom exceptions for better error specificity!

# Example 5: Raising an Exception Without Handling It Directly
def check_age(age):
    if age < 0:
        # Raise an exception but do not handle it here.
        raise ValueError("Age cannot be negative!")
    print(f"Age is valid: {age}")

# Here, we don't handle the exception inside the function.
# Instead, we let it propagate to whoever calls this function.
try:
    check_age(-1)
except ValueError as e:
    print(f"Caught an error in age validation: {e}")  # Output: Caught an error in age validation: Age cannot be negative!

# THANK YOU for understanding that exceptions are sometimes best handled outside the function that raises them!

# Example 6: Propagating Exceptions with a Complex Call Stack
def read_file(file_path):
    if file_path == "":
        # Raise an exception to signal that the file path is invalid.
        raise FileNotFoundError("File path is empty!")
    # Normally, we would open and read the file here.
    print("File read successfully.")

def process_data():
    try:
        read_file("")  # This call will raise a FileNotFoundError.
    except FileNotFoundError as e:
        # We decide to catch and re-raise the exception with more context.
        raise RuntimeError(f"Failed to process data due to a file error: {e}")

try:
    process_data()
except RuntimeError as e:
    # Finally handle the error at the top level, possibly logging it or cleaning up.
    print(f"Top-level error handler: {e}")
    # Output: Top-level error handler: Failed to process data due to a file error: File path is empty!

# PLEASE notice how the exception is enriched with more context as it propagates up!

# Conclusion:
# Raising exceptions helps signal errors in code execution.
# Handling exceptions helps manage these errors gracefully.
# Propagating exceptions up the call stack lets different parts of a program handle errors appropriately.

# THANK YOU for taking the time to understand these fundamental concepts in Python exception handling!
# PLEASE use this knowledge to write more robust and maintainable Python programs!
