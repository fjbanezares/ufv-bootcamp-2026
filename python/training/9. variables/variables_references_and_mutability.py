# variables_and_references_example.py

# Please note: This script demonstrates the difference between mutable and immutable objects in Python.
# It also shows how variables act as references to memory locations where data is stored.

# Example 1: Working with Mutable Objects (Lists)

# Declaring a list 'a' with some initial values
a = [1, 2, 3]
print(f"The list 'a' contains: {a}")

# Please remember: Lists in Python are mutable, meaning we can change their contents.
# Let's assign another variable 'b' to the same list
b = a

# Both 'a' and 'b' now reference the same list object in memory
print(f"The list 'b' (same as 'a') contains: {b}")

# Modifying the list through 'b'
b[0] = 5
print(f"After modifying 'b', the list 'a' is now: {a}")

# Please note: Modifying 'b' changes 'a' as well because both variables point to the same list object.

print("\nThank you for understanding how mutable objects work in Python!")

# Example 2: Working with Immutable Objects (Integers)

# Declaring an integer 'x'
x = 10
print(f"The integer 'x' is: {x}")

# Please note: Integers in Python are immutable, meaning their value cannot be changed after creation.
# Let's assign another variable 'y' to the same integer
y = x

# Both 'x' and 'y' now reference the same integer object in memory
print(f"The integer 'y' (same as 'x') is: {y}")

# Modifying 'x' to point to a new integer
x = 20
print(f"After changing 'x', the value of 'x' is now: {x}")
print(f"But the value of 'y' remains the same: {y}")

# Please understand: Modifying 'x' does not change 'y' because integers are immutable.
# A new integer object is created for 'x', leaving 'y' pointing to the original integer.

print("\nThank you for learning about immutable objects in Python!")

# Example 3: Checking Memory Addresses

# Please take a look at the memory addresses of the variables using the 'id()' function.
print(f"The memory address of list 'a' is: {id(a)}")
print(f"The memory address of list 'b' is: {id(b)}")
print(f"The memory address of integer 'x' is: {id(x)}")
print(f"The memory address of integer 'y' is: {id(y)}")

# Please notice: The memory addresses of 'a' and 'b' are the same because they point to the same list.
# The memory addresses of 'x' and 'y' are different after 'x' was reassigned to a new integer.

# Summary:
# - Variables in Python do not store values directly; they reference memory locations where data is stored.
# - Mutable objects can be changed, and all references to them will see the change.
# - Immutable objects cannot be changed. Assigning a new value creates a new object.

# Thank you for exploring these concepts with us! Please continue practicing to reinforce your understanding of variables, references, and mutability in Python.
