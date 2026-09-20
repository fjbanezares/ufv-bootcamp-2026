# string_interpolation_examples.py

# String interpolation is a way of inserting variables or expressions into strings.
# Python offers several ways to do this, with f-strings being the most modern and recommended method.

# Example 1: f-strings (formatted string literals)
# Introduced in Python 3.6, f-strings offer a concise and convenient way to embed expressions inside string literals, using {}.

name = "Alice"
age = 30

# Using an f-string to interpolate variables
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 30 years old.

# f-strings can also evaluate expressions inside the curly braces.
x, y = 10, 20
print(f"The sum of x and y is {x + y}.")
# Output: The sum of x and y is 30.

# Example 2: Using f-strings with custom objects
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Defining the __str__ method for custom string representation
    def __str__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"

point = Point3D(3, 4, 5)
print(f"The point is: {point}")
# Output: The point is: Point3D(3, 4, 5)

# Please note: f-strings are preferred for their readability and conciseness.
# They are also faster than other formatting methods because they are evaluated at runtime.

# Example 3: str.format() method
# Before f-strings, the str.format() method was the primary way to format strings in Python.
# You can also use positional and keyword arguments to specify the order.

# Using positional arguments
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 30 years old.

# Using keyword arguments
print("My name is {n} and I am {a} years old.".format(n=name, a=age))
# Output: My name is Alice and I am 30 years old.

# Example 4: %-formatting
# %-formatting is an older method borrowed from C.
# It's less intuitive than the other methods but is still occasionally seen in older codebases.

# %s is a placeholder for a string, and %d is a placeholder for an integer.
print("My name is %s and I am %d years old." % (name, age))
# Output: My name is Alice and I am 30 years old.

# Please note: %-formatting can be more error-prone and harder to read,
# so it's generally recommended to use f-strings or str.format() instead.

# Example 5: Template Strings
# Python also provides a template string module for simpler string substitutions.
# Template strings are useful when you need a format that you can pass around and apply multiple times.

from string import Template

t = Template("My name is $name and I am $age years old.")
print(t.substitute(name=name, age=age))
# Output: My name is Alice and I am 30 years old.

# Please note: Template strings are less powerful than f-strings or str.format() because they don't support arbitrary expressions.
# They are mainly useful for situations where you want to perform simple, safe substitutions.

# Summary:
# - f-strings are the most modern and recommended way for string interpolation in Python due to their readability and performance.
# - str.format() offers more flexibility with positional and keyword arguments.
# - %-formatting is older and less intuitive but still seen in some codebases.
# - Template strings are useful for simpler, safe substitutions.

# Thank you for exploring the different ways to format strings in Python!
# Please try these examples and choose the one that best fits your needs.
