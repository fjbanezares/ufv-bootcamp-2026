# variable_arguments_functions.py

# Please note: This script is designed to explain how to handle an unknown number of arguments in Python functions.
# We will explore *args for positional arguments and **kwargs for keyword arguments. Let's start!

# Example 1: Basic Function with Positional Arguments

# Let's define a function that describes a pet using two positional arguments
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

# Calling the function with two arguments
describe_pet('hamster', 'Harry')

# Please remember: Positional arguments are the most common type of arguments.
# They are required and must be provided in the correct order when calling the function.

# Example 2: Function with Keyword Arguments

# Let's define a function that prints a full name using keyword arguments
def print_full_name(first_name, last_name):
    print(f"My full name is {first_name} {last_name}.")

# Calling the function with keyword arguments
print_full_name(last_name="Doe", first_name="John")

# Please note: Keyword arguments allow you to pass arguments in any order.
# Each keyword argument has a key (parameter name) and a value.

# Example 3: Function with Variable Number of Positional Arguments (*args)

# Let's define a function that accepts a variable number of positional arguments
def print_all_args(*args):
    print("Positional arguments received:")
    for arg in args:
        print(arg)

# Calling the function with varying numbers of arguments
print_all_args(1, 2, 3)
print_all_args('a', 'b', 'c', 'd')

# Please understand: *args allows you to pass a variable number of positional arguments to a function.
# Inside the function, args is treated as a tuple, which means it's immutable and ordered.

# Example 4: Function with Variable Number of Keyword Arguments (**kwargs)

# Let's define a function that accepts a variable number of keyword arguments
def print_key_value_pairs(**kwargs):
    print("Keyword arguments received:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Calling the function with varying numbers of keyword arguments
print_key_value_pairs(name="Alice", age=30, job="Engineer")
print_key_value_pairs(city="New York", country="USA")

# Thank you for noting: **kwargs allows you to handle an unknown number of keyword arguments.
# Inside the function, kwargs behaves like a dictionary, allowing you to access the keys and values.

# Example 5: Combining *args and **kwargs in a Function

# Let's define a function that accepts both *args and **kwargs
def example_func(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

# Calling the function with both positional and keyword arguments
example_func(1, 2, 3, name="Alice", age=30, job="Engineer")

# Please remember: When defining a function with both *args and **kwargs, 
# *args must come before **kwargs in the function definition.
# This order ensures that Python correctly interprets the incoming arguments.

# Example 6: Using *args and **kwargs in Different Scenarios

# Let's create a function that uses *args to sum numbers
def sum_numbers(*args):
    return sum(args)

# Calling the function with different numbers of arguments
print(f"Sum of 1, 2, 3: {sum_numbers(1, 2, 3)}")  # Output: Sum of 1, 2, 3: 6
print(f"Sum of 5, 10, 15, 20: {sum_numbers(5, 10, 15, 20)}")  # Output: Sum of 5, 10, 15, 20: 50

# Let's create a function that uses **kwargs to display information
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different keyword arguments
display_info(name="John", age=25, location="San Francisco")

# Thank you for following along! By using *args and **kwargs, 
# we can create highly flexible functions that can handle varying numbers of inputs.
# This flexibility allows us to write more generic code that can be reused in different scenarios.

# Summary:
# - **Positional Arguments**: Required and must be provided in the correct order.
# - **Keyword Arguments**: Optional and can be provided in any order using key-value pairs.
# - **Variable Number of Positional Arguments (*args)**: Allows a function to accept any number of positional arguments.
# - **Variable Number of Keyword Arguments (**kwargs)**: Allows a function to accept any number of keyword arguments.
# - **Combining *args and **kwargs**: Enables the creation of highly flexible functions that can handle multiple types of inputs.

# Thank you once again for exploring these concepts with us!
# Please keep practicing with different examples to master the use of *args and **kwargs in Python functions.
# Hope you are liking the course so far
# Remember I show you the door you have to cross it 