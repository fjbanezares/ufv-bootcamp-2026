# Sets in Python - A Deep Dive


# A set is an unordered collection of unique elements in Python.
# It is mutable, meaning you can add or remove elements from a set after it is created.

# Please, let's start by creating a basic set and adding elements to it. Thank you!

# Creating an empty set
my_set = set()
print("Empty set created:", my_set)  # Outputs: Empty set created: set()

# Adding elements to a set
my_set.add(1)
my_set.add(2)
my_set.add(3)
print("Set after adding elements:", my_set)  # Outputs: Set after adding elements: {1, 2, 3}

# Notice that sets do not allow duplicate elements. Please observe the behavior below. Thanks!
my_set.add(3)  # Attempting to add '3' again.
print("Set after adding a duplicate element:", my_set)  # Outputs: {1, 2, 3}

# Sets are unordered, so the order of elements when printed may not match the order they were added.
# Also, the elements in a set must be hashable, meaning they must be immutable types like numbers, strings, and tuples.

# Let's discuss how sets use hashing for quick lookups. This is why the elements' order can appear random.

# Checking membership with 'in'
print(1 in my_set)  # Outputs: True
print(4 in my_set)  # Outputs: False

# Checking membership is very fast due to the underlying hash table.
# This is an O(1) operation on average.

# Let's explore some set operations. We will perform union, intersection, difference, and symmetric difference.
# Thank you for your patience as we cover these important operations.

# Creating two sets for demonstration
A = {1, 2, 3}
B = {3, 4, 5}

# Union of sets A and B
union_set = A | B
print("Union of A and B:", union_set)  # Outputs: Union of A and B: {1, 2, 3, 4, 5}

# Intersection of sets A and B
intersection_set = A & B
print("Intersection of A and B:", intersection_set)  # Outputs: Intersection of A and B: {3}

# Difference of sets A and B (elements in A but not in B)
difference_set = A - B
print("Difference of A and B (A - B):", difference_set)  # Outputs: Difference of A and B (A - B): {1, 2}

# Symmetric difference of sets A and B (elements in either A or B but not both)
sym_diff_set = A ^ B
print("Symmetric difference of A and B:", sym_diff_set)  # Outputs: Symmetric difference of A and B: {1, 2, 4, 5}

# You can also use methods like union(), intersection(), difference(), and symmetric_difference()
# These methods work the same as the operators |, &, -, and ^

# Checking if one set is a subset or superset of another
# A set A is a subset of set B if all elements of A are also in B

C = {1, 2}
print("Is C a subset of A?", C.issubset(A))  # Outputs: True

# A set A is a superset of set B if all elements of B are in A
print("Is A a superset of C?", A.issuperset(C))  # Outputs: True

# Adding elements to a set
# Adding a single element
A.add(4)
print("Set A after adding an element:", A)  # Outputs: {1, 2, 3, 4}

# Adding multiple elements using update()
A.update({5, 6, 7})
print("Set A after adding multiple elements:", A)  # Outputs: {1, 2, 3, 4, 5, 6, 7}

# Removing elements from a set
# Removing an element that exists in the set using remove()
A.remove(7)
print("Set A after removing an element:", A)  # Outputs: {1, 2, 3, 4, 5, 6}

# Attempting to remove an element that doesn't exist using remove() will raise a KeyError
# Uncomment the line below to see the error
# A.remove(8)

# Removing an element that may or may not exist using discard() does not raise an error
A.discard(8)  # Does nothing because 8 is not in the set
print("Set A after discarding a non-existent element:", A)  # Outputs: {1, 2, 3, 4, 5, 6}

# Clearing all elements from a set
A.clear()
print("Set A after clearing all elements:", A)  # Outputs: set()

# Practical use of sets: Removing duplicates from a list
fruits = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
unique_fruits = set(fruits)
print("Unique fruits:", unique_fruits)  # Outputs: {'cherry', 'apple', 'banana'}

# Sets are great for membership tests, removing duplicates, and performing mathematical operations.
# Please make sure to use sets where the order does not matter, and you only need unique elements. Thanks!

# Summary:
# - Sets are unordered collections of unique elements.
# - Elements in a set must be hashable.
# - Sets support union, intersection, difference, and symmetric difference operations.
# - Sets are useful for removing duplicates and checking membership quickly.

# THANK YOU for taking the time to learn about sets with us!
# PLEASE use sets in your Python programs whenever you need a collection of unique, unordered elements.
