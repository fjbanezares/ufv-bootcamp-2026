# global_vs_return.py

# Please note: This script compares two approaches for updating a counter: 
# using a global variable vs. using function parameters and return values.
# We will explore why avoiding global variables can lead to better code practices.

# Example 1: Using Global Variable (Side Effects)

# Let's define a global variable 'counter'
counter = 0

# Now, we'll define a function that increments the global counter
def increment_counter():
    global counter  # This tells Python we're using the global variable 'counter'
    counter += 1  # Increment the global counter

# Calling the function multiple times
increment_counter()
increment_counter()
increment_counter()

# Printing the value of the global counter
print(f"The value of the global counter is: {counter}")  # Output: The value of the global counter is: 3

# Thank you for noting: This function modifies a global variable, which means it has side effects.
# Side effects can make functions unpredictable and harder to test, as the function relies on and modifies external state.

# Side effects mean that the function changes some state outside its own scope.
# In this example, it modifies the global 'counter' variable, which can lead to:
# - **Unpredictability**: The outcome may depend on external factors, making debugging difficult.
# - **Difficulty in Testing**: Since external states need to be accounted for, testing becomes more complex.
# - **Reduced Reusability**: Functions with side effects are less versatile since they depend on specific external states.
# - **Concurrency Issues**: In multi-threaded environments, modifying shared state can cause race conditions.

# Example 2: Using Function Parameters and Return Values (Pure Function)

# Let's reset the counter to zero
counter = 0

# Now, we'll define a function that takes a counter as a parameter and returns the incremented value
def increment_counter_pure(cnt):
    return cnt + 1  # Return the incremented value without modifying any external state

# Using the function to increment the counter
counter = increment_counter_pure(counter)
counter = increment_counter_pure(counter)
counter = increment_counter_pure(counter)

# Printing the value of the counter
print(f"The value of the counter using return is: {counter}")  # Output: The value of the counter using return is: 3

# Please note: This function does not modify any external state. It is a pure function.
# A pure function's output depends only on its input parameters and does not cause any side effects.
# This makes the function predictable, easier to test, reusable, and safe for concurrent execution.

# Advantages of using return instead of global:
# - **Avoid Side Effects**: The function remains pure, meaning given the same inputs, it always produces the same output without causing side effects.
# - **Maintainability**: Functions that don't modify global state are generally easier to maintain and debug because their behavior is predictable.
# - **Reusability**: Functions that don't depend on or alter the global state can be reused in different contexts without unexpected behaviors.
# - **Readability**: The data flow is more evident, as the function's inputs and outputs are explicitly defined.

# Summary:
# - **Global Variables and Side Effects**: Functions that modify global variables have side effects, which can lead to unpredictable behavior, testing difficulties, reduced reusability, and concurrency issues.
# - **Function Parameters and Return Values**: Using function parameters and return values helps create pure functions, leading to predictable behavior, easier testing, higher reusability, and better safety in concurrent environments.

# Thank you for exploring these concepts with us! Please continue practicing by writing functions that avoid global variables and side effects to develop clean and maintainable code.
