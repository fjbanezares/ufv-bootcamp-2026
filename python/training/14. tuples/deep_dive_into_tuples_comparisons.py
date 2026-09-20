# deep_dive_into_tuples.py

# PLEASE NOTE: Tuples in Python are immutable sequences, meaning their elements cannot be changed once assigned.
# This immutability can be very useful for ensuring data integrity throughout a program. THANK YOU for learning about tuples with us!

# Example 1: Tuple Creation and Single-Element Tuples

# Creating a tuple with multiple elements
multi_element_tuple = (1, 2, 3)
print(multi_element_tuple)  # Outputs: (1, 2, 3)

# Creating a single-element tuple
# The comma is ESSENTIAL here to denote that this is indeed a tuple
single_element_tuple = (4,)
print(single_element_tuple)  # Outputs: (4,)

no_parentheses_single_element_tuple = 4,
print(no_parentheses_single_element_tuple)  # Outputs: (4,) parentheses are just for the weak :)

# Without the comma, Python does not recognize this as a tuple
not_a_tuple = (4)
print(not_a_tuple)  # Outputs: 4 (as an integer, not a tuple)

# THANK YOU for observing the critical difference here!

# Example 2: Tuple Comparison
# Tuples are compared element by element, which allows for intuitive yet powerful comparisons.

# Comparison Example 1
tuple1 = (1, 2)
tuple2 = (1, 2, 3)
print(tuple1 < tuple2)  # True, because tuple1 is shorter than tuple2. In Python, shorter tuples are considered "less than" longer ones if all compared elements are equal.

# Comparison Example 2
tuple3 = (1, 3, 4)
tuple4 = (1, 2, 5)
print(tuple3 > tuple4)  # True, because 3 > 2 when the second elements are compared

# Comparison Example 3
tuple5 = (1, 3, 4, 5)
tuple6 = (1, 3, 4, 2)
print(tuple5 > tuple6)  # True, because 5 > 2 when the last differing elements are compared

# THANK YOU for carefully following these comparison rules!

# Example 3: Comparing Tuples of Different Lengths

# Python allows comparing tuples of different lengths. If all items up to the end of the shorter tuple are equal, 
# then the shorter tuple is considered "less than" the longer one.

tuple7 = (1, 2)
tuple8 = (1, 2, 3)
print(tuple7 < tuple8)  # Outputs: True, because the first two elements are equal, and the first tuple is shorter.

# Example 4: Mixed-Type Comparisons in Tuples
# Python can compare tuples with different types if it knows how to compare the contained elements.

mixed_tuple1 = (1, 'apple')
mixed_tuple2 = (1, 'banana')
print(mixed_tuple1 < mixed_tuple2)  # Outputs: True, because 'apple' < 'banana' lexicographically

# PLEASE BE CAREFUL with mixed-type comparisons. While Python allows them, they can sometimes lead to confusing code if not handled properly.

# Example 5: Mutable Elements Inside Tuples
# Even though tuples are immutable, if they contain mutable elements (like lists), those elements can be changed.

# Creating a tuple with a list inside
mutable_inside_tuple = ([1, 2], 3)
print(mutable_inside_tuple)  # Outputs: ([1, 2], 3)

# Modifying the list inside the tuple
mutable_inside_tuple[0][0] = 'Changed'
print(mutable_inside_tuple)  # Outputs: (['Changed', 2], 3)

# THANK YOU for seeing that while the tuple structure is immutable, its contents can still be altered if they are mutable.

# Example 6: Using Tuples as Dictionary Keys
# Because tuples are immutable, they can be used as keys in a dictionary, unlike lists.

# Dictionary with a tuple key
tuple_key_dict = {('x', 'y'): 'Coordinates'}
print(tuple_key_dict)  # Outputs: {('x', 'y'): 'Coordinates'}

# Accessing the value using the tuple as a key
print(tuple_key_dict[('x', 'y')])  # Outputs: Coordinates

# THANK YOU for noticing how immutability in tuples allows them to be reliable dictionary keys!

# Recap and Key Takeaways:
# - Tuples are immutable sequences in Python.
# - Single-element tuples need a trailing comma to differentiate them from a regular value inside parentheses.
# - Tuple comparisons are done element by element and stop as soon as a difference is found.
# - Tuples can contain mutable elements, but the tuple itself is immutable.
# - Tuples can be used as dictionary keys because of their immutability.
# - Mixed-type comparisons are possible but should be used with care to avoid confusion.

# THANK YOU for learning about tuples with this deep dive! We hope this helps clarify the power and subtleties of Python tuples.

