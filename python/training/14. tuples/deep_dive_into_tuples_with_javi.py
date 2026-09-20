# Tuples in Python are used to store multiple items in a single variable.
# Please remember that tuples are immutable, meaning their content cannot be changed once created. Thanks for noting this!

# 1. Creating tuples using parentheses
tuple1 = (1, 2, 3)
print("Tuple1:", tuple1)  # Output: Tuple1: (1, 2, 3)

# 2. Creating tuples without parentheses (also valid)
tuple2 = 4, 5, 6
print("Tuple2:", tuple2)  # Output: Tuple2: (4, 5, 6)

# 3. Single-element tuple: Use a comma to differentiate from a regular value in parentheses
single_element_tuple = (7,)
print("Single-element Tuple:", single_element_tuple)  # Output: Single-element Tuple: (7,)

# 4. Using the tuple() constructor to convert a list to a tuple
list_to_convert = [8, 9, 10]
converted_tuple = tuple(list_to_convert)
print("Converted Tuple:", converted_tuple)  # Output: Converted Tuple: (8, 9, 10)

# 5. Indexing and slicing tuples
fruits = ("apple", "banana", "cherry", "date")
print("First fruit:", fruits[0])  # Output: First fruit: apple
print("Last fruit:", fruits[-1])  # Output: Last fruit: date
print("Slice of fruits:", fruits[1:3])  # Output: Slice of fruits: ('banana', 'cherry')

# Tuples are immutable, so attempting to change a value raises an error
try:
    fruits[1] = "blueberry"  # This will raise a TypeError
except TypeError as e:
    print("Error:", e)

# 6. Unpacking tuples
coordinates = (4, 5)
x, y = coordinates  # Unpacking tuple into variables
print(f"X: {x}, Y: {y}")  # Output: X: 4, Y: 5

# 7. Swapping variables using tuple unpacking
a, b = 1, 2
print("Before swap:", a, b)  # Output: Before swap: 1 2
a, b = b, a  # Swap values
print("After swap:", a, b)  # Output: After swap: 2 1

# 8. Tuple methods: count() and index()
my_tuple = (1, 2, 2, 3, 4)
print("Count of 2s:", my_tuple.count(2))  # Output: Count of 2s: 2
print("Index of 3:", my_tuple.index(3))  # Output: Index of 3: 3

# 9. Nested tuples and accessing nested elements
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested Tuple:", nested_tuple)  # Output: Nested Tuple: ((1, 2), (3, 4), (5, 6))
print("Element from nested tuple:", nested_tuple[1][0])  # Output: Element from nested tuple: 3

# 10. Using tuples as keys in a dictionary
# Tuples can be used as dictionary keys because they are immutable
my_dict = {(1, 2): "value1", (3, 4): "value2"}
print("Value for key (1, 2):", my_dict[(1, 2)])  # Output: Value for key (1, 2): value1

# 11. Beware of modifying mutable objects inside tuples
mutable_inside_tuple = ([1, 2], [3, 4])
mutable_inside_tuple[0][1] = "modified"
print("Tuple with mutable inside:", mutable_inside_tuple)  # Output: Tuple with mutable inside: ([1, 'modified'], [3, 4])
# Note: The tuple itself is immutable, but its elements (like lists) can still be modified

# THANK YOU for going through this example!
# PLEASE ensure you understand that while tuples are immutable, their contents can still be mutable objects like lists.
# This behavior is crucial to avoid bugs in your code when using tuples with mutable elements. Thanks again for paying attention!


box_a = ["apple", "banana"]
box_b = ["grape", "cherry"]
inventory_list_1 = [box_a, box_b]
inventory_list_2 = inventory_list_1.copy()

box_a.append("kiwi")
print(inventory_list_1[0]) 
print(inventory_list_2[0]) 
 # Outputs: ["apple", "banana", "kiwi"]
