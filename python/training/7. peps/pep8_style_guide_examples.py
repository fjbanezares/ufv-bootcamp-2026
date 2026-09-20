"""
This Python script demonstrates the PEP 8 style guide through practical examples.
PEP 8 is Python's official style guide for writing clean, readable, and maintainable code.
We will cover key PEP 8 guidelines like naming conventions, indentation, line length, spacing,
comments, and much more. Please follow the guidelines to ensure consistent code quality.
Thanks for reading!
"""

# 1. Import statements should be placed at the top of the file.
# Imports should be on separate lines.
import os  # Correct
import sys  # Correct

# Please avoid writing multiple imports on the same line.
# import os, sys  # Incorrect

# 2. Indentation: PEP 8 recommends using 4 spaces per indentation level, not tabs.
def example_function():
    # Please use 4 spaces, as demonstrated here.
    # Thanks for not using tabs!
    variable = 5
    if variable == 5:
        print("Variable is 5")  # Indented properly with 4 spaces

# 3. Line length: Limit all lines to a maximum of 79 characters.
# Please break long lines for better readability.
def long_function_name(
        var_one, var_two, var_three, var_four):  # Break lines after 79 characters
    return var_one + var_two + var_three + var_four


# Example of splitting function arguments for readability
result = long_function_name(1, 2, 3, 4)
print(result)

###############################################################################
# 4. Blank lines: Use 2 blank lines before a top-level function or class definition.
# Inside classes, methods should be separated by a single blank line.
###############################################################################

class MyClass:
    """A simple example class following PEP 8 guidelines."""

    def __init__(self, name):
        # Please follow the class and method spacing rules
        self.name = name  # Single blank line between methods

    def greet(self):
        return f"Hello, {self.name}!"


# Creating an object and calling the greet method
my_obj = MyClass("Francisco")
print(my_obj.greet())

# 5. Inline comments: Place comments on the same line as the statement they refer to.
# Please separate them by at least two spaces.
x = 42  # This is an inline comment

# 6. Block comments: Use them to explain more complex code or sections of code.
# Please ensure that block comments are indented to the same level as the code they describe.

###############################################################################
# Example: Block comment explaining this entire section of code.
# The following code demonstrates best practices in variable naming, 
# spacing, and function definitions.
###############################################################################

def calculate_area_of_rectangle(length, width):
    """Calculate the area of a rectangle."""
    # Variable names should be lowercase, with words separated by underscores.
    area = length * width
    return area

# Calling the function with proper spacing
area = calculate_area_of_rectangle(5, 3)
print(f"Area: {area}")  # Output: Area: 15


# 7. Naming conventions: Use meaningful variable, function, and class names.
# Please avoid single-letter variable names, except in very short loops.
# Thanks for using descriptive names!

# Class names should follow CamelCase convention.
class RectangleAreaCalculator:
    """A class to calculate the area of rectangles."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        # Method names should be lowercase, with words separated by underscores.
        return self.length * self.width


# Creating an instance of the class and calculating the area
rectangle = RectangleAreaCalculator(5, 7)
print(f"Rectangle Area: {rectangle.calculate_area()}")  # Output: 35

###############################################################################
# 8. Whitespace in expressions and statements: Avoid unnecessary whitespace.
# Please follow these guidelines:
###############################################################################

# No space before or after parentheses, brackets, or braces.
# Correct:
my_list = [1, 2, 3]
my_dict = {'key': 'value'}

# Incorrect:
# my_list = [ 1, 2, 3 ]  # Please avoid extra spaces

# Please use spaces around operators, but not immediately inside parentheses.
x = 3 + 2  # Correct
y = (x + 5) * (x - 1)  # Correct

# Avoid:
# x=3+2  # No spaces around operators

###############################################################################
# 9. Docstrings: Use triple quotes for all docstrings, even for one-liners.
###############################################################################

def example_with_docstring(param):
    """
    This function serves as an example of how to use docstrings.
    
    Args:
        param (int): A number to process.
    
    Returns:
        int: The square of the number.
    """
    return param ** 2


# Let's call the function and see how it works
square = example_with_docstring(4)
print(f"Square: {square}")  # Output: Square: 16

###############################################################################
# 10. Error handling: Use exceptions instead of returning error codes.
# Please ensure proper error handling using try-except blocks.
###############################################################################

def divide(a, b):
    """Divide two numbers, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        # Please handle exceptions gracefully
        return "Cannot divide by zero!"

# Example of using the divide function
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Cannot divide by zero!

###############################################################################
# 11. Shebang: If your file is intended to be executed as a script, 
# please include a shebang line at the top of the file.
# Example: #!/usr/bin/env python3
###############################################################################

# 12. End of file: Always leave a single newline at the end of the file.
# Thanks for following this best practice!
