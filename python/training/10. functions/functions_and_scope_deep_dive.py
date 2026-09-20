# functions_and_scope_deep_dive.py

# Please note: This script is designed to explain the basics of functions, parameters, arguments, and variable scopes in Python.
# We will go step by step to ensure clarity, so please follow along!

# Example 1: Basic Function Definition and Call

# Let's define a simple function named 'greet'
def greet():
    # This function prints a greeting message
    print("Hello!")

# Please remember: Functions are defined using the 'def' keyword followed by the function name and parentheses.
# Inside the parentheses, you can specify parameters if the function needs to accept input.

# Calling the function 'greet'
greet()  # Output: Hello!

# Please note: To execute the code inside a function, you need to 'call' the function by writing its name followed by parentheses.

# Example 2: Function with Parameters and Arguments

# Let's define a function that accepts one parameter
def greet(name):
    # This function takes one parameter 'name' and prints a personalized greeting
    print(f"Hello, {name}!")

# Calling the function with an argument
greet("Alice")  # Output: Hello, Alice!

# Please understand: Parameters are variables that you define in the function definition. 
# Arguments are the actual values you pass to the function when you call it.

# Example 3: Function with Multiple Parameters

# Let's define a function that accepts multiple parameters
def add_numbers(a, b):
    # This function adds two numbers and returns the result
    return a + b

# Calling the function with two arguments
result = add_numbers(5, 7)
print(f"The result of adding 5 and 7 is: {result}")  # Output: The result of adding 5 and 7 is: 12

# Thank you for noting: You can return values from functions using the 'return' keyword.
# The 'return' statement also ends the function execution, so any code after 'return' will not be executed.

# Example 4: Local Variables

# Let's define a function that uses a local variable
def foo():
    # This variable is local to the function 'foo'
    local_var = "I'm local"
    print(local_var)

# Calling the function 'foo'
foo()  # Output: I'm local

# Trying to access the local variable outside the function will raise an error
try:
    print(local_var)
except NameError:
    print("Error: local_var is not defined outside of the function 'foo'")

# Please remember: Variables defined inside a function are called 'local variables'.
# They exist only within the function and cannot be accessed from outside.

# Example 5: Global Variables

# Let's define a global variable
global_var = "I'm global"

# Defining a function that accesses a global variable
def foo_global():
    # Accessing the global variable inside the function
    print(global_var)

# Calling the function
foo_global()  # Output: I'm global

# Accessing the global variable outside the function
print(global_var)  # Output: I'm global

# Please note: Variables defined outside any function are called 'global variables'.
# They can be accessed both inside and outside of functions.

# Example 6: Modifying Global Variables Inside a Function

# To modify a global variable inside a function, use the 'global' keyword
def modify_global():
    global global_var
    global_var = "Changed inside the function"
    print(global_var)

# Calling the function that modifies the global variable
modify_global()  # Output: Changed inside the function

# Checking the value of the global variable outside the function
print(global_var)  # Output: Changed inside the function

# Thank you for understanding: By using the 'global' keyword, you tell Python that you want to use the global variable, not create a local one.
# This allows you to modify the global variable from within the function.

# Example 7: Returning Multiple Values from a Function

# Let's define a function that returns multiple values
def calculate(a, b):
    # This function returns the sum and difference of two numbers
    sum_result = a + b
    diff_result = a - b
    return sum_result, diff_result

# Calling the function and unpacking the returned values
sum_result, diff_result = calculate(10, 5)
print(f"Sum: {sum_result}, Difference: {diff_result}")  # Output: Sum: 15, Difference: 5

# Please understand: A function can return multiple values by separating them with commas.
# When you call the function, you can unpack these values into multiple variables.

# Summary:
# - **Functions**: Reusable blocks of code that perform a specific task. Defined using 'def' keyword.
# - **Parameters**: Variables in function definitions that accept input values.
# - **Arguments**: Actual values passed to functions when called.
# - **Local Variables**: Variables declared inside a function. Accessible only within that function.
# - **Global Variables**: Variables declared outside any function. Accessible throughout the module.
# - **'global' Keyword**: Allows modification of global variables inside a function.
# - **Return Statement**: Used to return values from a function and end the function execution.

# Thank you for exploring these concepts with us! Please continue practicing functions and variable scopes in Python to solidify your understanding.
