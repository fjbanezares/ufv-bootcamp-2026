# Assertions in Python are used for debugging purposes.
# They are used to test if a condition in your code returns True.

# Let's start with a simple assertion example.

# Initialize a variable with an integer value
x = 10

# An assertion to check if x equals 10
assert x == 10, "x should be 10"

# The above assertion will pass since x is indeed 10.
# If x were any value other than 10, the assertion would raise an AssertionError.

# Let's see what happens when an assertion fails:

y = 50

# An assertion to check if y is greater than 10
assert y > 10, "y should be greater than 10"  # This will raise an AssertionError.

# Output:
# AssertionError: y should be greater than 10

# PLEASE NOTE: When an assertion fails, Python raises an AssertionError with the message provided.

# Why use assertions?
# Assertions are mainly used to check conditions that should always be true in your code.
# They help catch bugs early by making assumptions explicit.

# Difference between Assertions and Exceptions:
# - Assertions are used to check for conditions that should never happen if the code is correct.
# - Exceptions are used to handle conditions that can happen during normal operation, like user input errors or file not found errors.

# Let's compare them directly:

def divide(a, b):
    # Using an exception to handle a condition we expect could happen.
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero: {e}")
        return None
    return result

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Cannot divide by zero: division by zero

# The above function uses a try/except block to handle a ZeroDivisionError.
# This is a situation we expect might happen (dividing by zero).

def positive_number_assert(num):
    # Using an assertion to check a condition we assume to be true.
    assert num > 0, "Number must be positive"
    return num

print(positive_number_assert(5))  # Output: 5
#print(positive_number_assert(-1))  # Uncommenting this will raise an AssertionError: Number must be positive

# PLEASE NOTE: Assertions should not be used to handle expected errors in user input or system operations.
# They are not a substitute for proper exception handling.

# Best Practices:
# 1. Use assertions to check for conditions that should never occur.
# 2. Use exceptions to handle conditions that could occur and need a recovery strategy.
# 3. Assertions can be disabled in production with the -O and -OO flags, so they should not be used for runtime logic or error handling.

# THANK YOU for following along with these examples on assertions and exceptions!
# PLEASE use assertions wisely as a debugging tool to enforce assumptions and catch bugs early in development.

# Symbol Explanation:
# The symbol on the page appears to be a laboratory flask, often used to represent experimentation or testing.
# This aligns with the concept of assertions, which are used to test assumptions during development.
