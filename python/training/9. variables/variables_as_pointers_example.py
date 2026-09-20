# variables_as_pointers_example.py

# Please note: In Python, variables act as labels or names that point to locations in the computer's memory where data is stored.
# Think of a variable as a label on a box, where the box represents a memory location and the label (variable) is how we refer to it.

# Initializing a variable with None
my_variable = None
print(my_variable)  # Output: None

# Later, you can assign it a value
my_variable = 10
print(my_variable)  # Output: 10

# Example 1: Basic Variable Declaration and Initialization
# Declaring a variable 'age' and initializing it with a value of 25
age = 25
print(f"The variable 'age' points to the value: {age}")

# Please understand: When we assign a value to a variable, the variable becomes a pointer to that value in memory.
# The equals sign (=) is used to assign values to variables.

# Example 2: Variables Pointing to Different Data Types
# Let's declare more variables with different data types

# Integer
count = 10
print(f"The variable 'count' points to the integer value: {count}")

# String
name = "Alice"
print(f"The variable 'name' points to the string value: {name}")

# Float
pi = 3.14
print(f"The variable 'pi' points to the float value: {pi}")

# Boolean
is_valid = True
print(f"The variable 'is_valid' points to the boolean value: {is_valid}")

# Please remember: Variables can point to different data types, such as integers, strings, floats, and booleans.
# The type of data a variable points to determines how much memory is allocated for it.

# Example 3: Variables as Pointers to the Same Object
# Let's see what happens when two variables point to the same object

# Assigning the variable 'a' with a value of 100
a = 100
# Assigning the variable 'b' to point to the same value as 'a'
b = a

print(f"The variable 'a' points to the value: {a}")
print(f"The variable 'b' also points to the same value as 'a': {b}")

# Please notice: Both 'a' and 'b' point to the same memory location that holds the value 100.
# If we change the value of 'a', 'b' will still point to the original value.

# Changing the value of 'a'
a = 200
print(f"Now, the variable 'a' points to a new value: {a}")
print(f"But the variable 'b' still points to the original value: {b}")

# Example 4: Variables Pointing to Mutable Objects
# Lists are mutable objects in Python, meaning their contents can change.

# Declaring a variable 'my_list' pointing to a list object
my_list = [1, 2, 3]
print(f"The variable 'my_list' points to the list: {my_list}")

# Assigning another variable 'another_list' to point to the same list object
another_list = my_list

print(f"The variable 'another_list' points to the same list: {another_list}")

# Modifying the list through 'another_list'
another_list.append(4)
print(f"After modifying 'another_list', 'my_list' also reflects the change: {my_list}")
print(f"Both variables point to the same memory location, hence both reflect the change.")

# Please note: When working with mutable objects like lists, changing the object through one variable will reflect in all variables pointing to that object.

# Example 5: Checking Memory Addresses
# Let's check the memory addresses of the variables to see where they point in memory.

print(f"The memory address of 'age' is: {id(age)}")
print(f"The memory address of 'count' is: {id(count)}")
print(f"The memory address of 'name' is: {id(name)}")
print(f"The memory address of 'pi' is: {id(pi)}")
print(f"The memory address of 'is_valid' is: {id(is_valid)}")
print(f"The memory address of 'my_list' is: {id(my_list)}")
print(f"The memory address of 'another_list' is: {id(another_list)}")

# Please observe: The 'id()' function returns the memory address of the variable's value, which shows where in memory the value is stored.

# Summary:
# - Variables in Python are pointers to memory locations where data is stored.
# - Different variables can point to different data types, and the type affects memory allocation.
# - Variables can point to the same object, and changes to mutable objects are reflected in all variables pointing to that object.
# - The 'id()' function helps us understand the memory addresses of the variables.

# Thank you for exploring the concept of variables as pointers in Python!
# Please continue experimenting with different types and objects to strengthen your understanding of how variables work.
