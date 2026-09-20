# Tuples in Python - A deep dive with examples

# Please note: Tuples are immutable collections of items in Python.
# Once created, the elements of a tuple cannot be modified. Thank you for your attention!

# 1. Creating Tuples
# Tuples can be created using parentheses or the tuple() constructor

# A tuple with multiple elements
my_tuple = (1, 2, 3)
print(f"My tuple: {my_tuple}")

# A single-element tuple needs a comma to differentiate from a mere parenthesized expression
single_element_tuple = (4,)
print(f"Single element tuple: {single_element_tuple}")

# Creating a tuple without parentheses is also possible
another_tuple = 5, 6, 7
print(f"Tuple without parentheses: {another_tuple}")

# Using tuple() constructor to convert a list to a tuple
list_to_convert = [8, 9, 10]
converted_tuple = tuple(list_to_convert)
print(f"Converted tuple: {converted_tuple}")

# Please note: Parentheses are often used for clarity, but they are not strictly required. Thanks for keeping this in mind!

# 2. Accessing Tuple Elements
# Elements in tuples can be accessed using indexing

fruits = ("apple", "banana", "cherry", "date")
print(f"First fruit: {fruits[0]}")  # Accessing the first element

# Negative indexing allows you to access elements from the end
print(f"Last fruit: {fruits[-1]}")  # Accessing the last element

# 3. Slicing Tuples
# Tuples support slicing, similar to lists

# Slicing returns a new tuple with the specified range
sub_tuple = fruits[1:3]  # Includes index 1, but excludes index 3
print(f"Sliced tuple: {sub_tuple}")

# 4. Immutability of Tuples
# Tuples are immutable, meaning their content cannot be changed after creation

# Uncommenting the following line will raise a TypeError:
# fruits[0] = "avocado"  # This would raise an error

# However, you can concatenate tuples to create a new one
new_fruits = fruits + ("elderberry",)
print(f"Concatenated tuple: {new_fruits}")

# Please remember: Tuples cannot be modified in place. Once created, they remain the same. Thank you!

# 5. Tuple Methods
# Tuples have limited built-in methods compared to lists

# count() returns the number of occurrences of a specified value
example_tuple = (1, 2, 2, 3, 4)
print(f"Number of 2's in the tuple: {example_tuple.count(2)}")

# index() returns the index of the first occurrence of a specified value
print(f"Index of 3 in the tuple: {example_tuple.index(3)}")

# 6. Unpacking Tuples
# Tuple unpacking allows assigning elements of a tuple to variables in one go

coordinates = (5, 10)
x, y = coordinates
print(f"x: {x}, y: {y}")

# This is particularly useful in functions returning multiple values
def get_name_age():
    return ("Alice", 30)

name, age = get_name_age()
print(f"Name: {name}, Age: {age}")

# 7. Swapping Variables Using Tuples
# Tuple unpacking is a Pythonic way to swap values without needing a temporary variable

a = 1
b = 2
print(f"Before swap - a: {a}, b: {b}")
a, b = b, a
print(f"After swap - a: {a}, b: {b}")

# Please note: This tuple swap mechanism is concise and efficient. Thanks for using Pythonic ways!

# 8. Tuples as Dictionary Keys
# Because tuples are immutable, they can be used as keys in dictionaries

coordinates_dict = {(0, 0): "origin", (1, 2): "point A"}
print(f"Coordinates dictionary: {coordinates_dict}")

# 9. Nested Tuples
# Tuples can contain other tuples, allowing for complex data structures

nested_tuple = ((1, 2, 3), ("a", "b", "c"))
print(f"Nested tuple: {nested_tuple}")

# Accessing elements in nested tuples
print(f"Second element of the first tuple: {nested_tuple[0][1]}")

