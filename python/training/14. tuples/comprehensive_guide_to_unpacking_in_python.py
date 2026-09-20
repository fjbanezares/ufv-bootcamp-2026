# Comprehensive Guide to Unpacking in Python
# This script covers various unpacking techniques in Python with detailed examples and explanations.
# Thank you for exploring these concepts, and please take your time to go through each example.

# -------------------
# Basic Tuple Unpacking
# -------------------

# Tuples are immutable sequences, and unpacking allows you to assign each element of a tuple to a variable in a single line.

coordinates = (4, 5)  # A simple tuple with two elements

# Unpacking the tuple 'coordinates' into variables 'x' and 'y'
x, y = coordinates  # 'x' gets the first element (4), and 'y' gets the second element (5)

print("x:", x)  # Output: x: 4
print("y:", y)  # Output: y: 5

# THANK YOU for starting with us on this unpacking journey! Now, let's move on to unpacking with lists.

# -------------------
# Unpacking with Lists
# -------------------

# Lists are mutable sequences. You can also unpack lists just like tuples.

fruits = ["apple", "banana", "cherry"]  # A list of fruits

# Unpacking the list into three variables
first_fruit, second_fruit, third_fruit = fruits  # Each variable gets a corresponding element from the list

print("First fruit:", first_fruit)  # Output: First fruit: apple
print("Second fruit:", second_fruit)  # Output: Second fruit: banana
print("Third fruit:", third_fruit)  # Output: Third fruit: cherry

# PLEASE note: The number of variables must match the number of elements in the list. Thanks for your attention!

# -------------------
# Unpacking with Default Pattern (Using *)
# -------------------

# The asterisk (*) can be used to capture multiple elements into a list when unpacking.

numbers = [1, 2, 3, 4, 5]  # A list of numbers

# 'a' gets the first element, 'b' the second, and 'rest' captures all remaining elements as a list
a, b, *rest = numbers

print("a:", a)  # Output: a: 1
print("b:", b)  # Output: b: 2
print("rest:", rest)  # Output: rest: [3, 4, 5]

# THANK YOU for keeping up! The asterisk allows us to unpack more flexibly. Now, let's explore nested unpacking.

# -------------------
# Unpacking with Nested Structures
# -------------------

# Unpacking works with nested data structures like lists of tuples.

nested_list = [("John", 25), ("Jane", 22)]  # A list of tuples, each containing a name and age

# Unpacking the nested list within a loop
for name, age in nested_list:
    print(f"Name: {name}, Age: {age}")  # Prints each name and age on a new line

# Output:
# Name: John, Age: 25
# Name: Jane, Age: 22

# PLEASE remember, unpacking simplifies data extraction, especially in loops. Thanks for paying attention!

# -------------------
# Unpacking Dictionary Items
# -------------------

# You can unpack dictionary items to work with key-value pairs directly in loops.

student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}  # A dictionary with student names and grades

# Unpacking dictionary items
for student, grade in student_grades.items():
    print(f"Student: {student}, Grade: {grade}")  # Prints each student and their grade

# Output:
# Student: Alice, Grade: 85
# Student: Bob, Grade: 92
# Student: Charlie, Grade: 78

# THANK YOU for sticking around! Now let's see how unpacking can help us swap variables.

# -------------------
# Unpacking for Swapping Variables
# -------------------

# A Pythonic way to swap variables without a temporary variable

x = 10
y = 20

# Swapping 'x' and 'y'
x, y = y, x  # 'x' now becomes 20 and 'y' becomes 10

print("x:", x)  # Output: x: 20
print("y:", y)  # Output: y: 10

# PLEASE note: This concise swap uses unpacking to avoid temporary storage. Thanks for learning with us!

# -------------------
# Unpacking Multiple Return Values from Functions
# -------------------

# Functions can return multiple values as a tuple, which can be unpacked.

def get_min_max(numbers):
    return min(numbers), max(numbers)  # Returns two values: the minimum and maximum of the list

min_val, max_val = get_min_max([4, 1, 9, 7])  # Unpacking the returned tuple into two variables

print("Min:", min_val)  # Output: Min: 1
print("Max:", max_val)  # Output: Max: 9

# THANKS for watching! Unpacking helps handle multiple returned values efficiently.

# -------------------
# Why is Unpacking Hard to Understand?
# -------------------

# 1. Implicit Behavior: Unpacking does multiple assignments in one go, which can be confusing without a clear understanding.
# 2. Exact Match Requirement: The number of variables must match the number of elements being unpacked, or else Python raises a ValueError.
# 3. Versatility: Unpacking works with various data structures and patterns, making it seem complex initially.
# 4. Nested and Advanced Patterns: Combining unpacking with loops, conditions, or nested structures adds layers of complexity.

# PLEASE keep practicing unpacking to become more comfortable with it. It's an invaluable tool in Python that helps write more concise and readable code.

# THANK YOU once again for exploring unpacking with us!
