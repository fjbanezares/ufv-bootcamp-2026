# Dear friend, in this script, we're going to create a 3x3 matrix using list comprehensions in Python.
# We'll carefully explore each step, so please follow along and enjoy the process! 

# PLEASE NOTE: A matrix in Python can be visualized as a list of lists,
# where each inner list represents a row of the matrix.

string_prueba = "Hello Worls"
print(string_prueba[::-2])

# Let's start by initializing our matrix.
matrix = [[0 for _ in range(3)] for _ in range(3)]

# What have we done here? Let's break it down step-by-step, nice and easy! 

# Step 1: Understanding the Inner List Comprehension
# ---------------------------------------------
# Inside the matrix initialization, we have this part first:
# [0 for _ in range(3)]
# 
# This creates a list with three zeros: [0, 0, 0]  
# Here's how it works:
# - The 'for' loop runs 3 times because of 'range(3)'.
# - The underscore '_' is used as a throwaway variable, which means we're not using it.
# - Each time the loop runs, it adds a '0' to the list.
# 
# Please see how much care Python takes to ensure you have exactly what you need!

# Step 2: The Outer List Comprehension
# ---------------------------------------------
# Now, let's look at the outer list comprehension:
# [[0 for _ in range(3)] for _ in range(3)]
#
# This part runs the inner list comprehension (creating [0, 0, 0]) three times.
# - Each time it runs, it adds a new row to the matrix.
# - After three iterations, we have a lovely 3x3 matrix filled with zeros!
# 
# Thank you, Python, for making this so simple and elegant!

# Let's print our matrix to see what we've created with love.
print("Here is our beautiful matrix:")
for row in matrix:
    print(row)
# Output will be:
# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 0]

# Isn't that just wonderful? Each row of the matrix is a list, and we've created a grid of zeros.

# Step 3: Modifying the Matrix
# ---------------------------------------------
# Now let's play a little bit more, shall we? We can modify this matrix to suit our needs.
# Let's change the first element of the first row to 1, just for fun!

matrix[0][0] = 1
print("\nMatrix after modifying the first element of the first row:")
for row in matrix:
    print(row)
# Output will be:
# [1, 0, 0]
# [0, 0, 0]
# [0, 0, 0]

# See how easy it is to make changes? This is because each inner list is an independent list.

# Step 4: Understanding the Independence of Rows
# ---------------------------------------------
# Each inner list in our matrix is a separate object.
# This means if we change one row, other rows are unaffected.
# Let's change the last element of the second row to 5:

matrix[1][2] = 5
print("\nMatrix after modifying the last element of the second row:")
for row in matrix:
    print(row)
# Output will be:
# [1, 0, 0]
# [0, 0, 5]
# [0, 0, 0]

# Thank you, Python, for letting each list be so independent and unique!

# Step 5: Important Note About List Comprehensions
# ---------------------------------------------
# One more important thing, please remember:
# Using list comprehensions ensures that each inner list is a new, unique list.
# If we had used multiplication like this: matrix = [[0]*3]*3, 
# then all the rows would be references to the same list object.
# This could lead to unexpected behavior when modifying the matrix.
#
# Let’s demonstrate what would happen in such a case:

matrix_bad = [[0] * 3] * 3  # Using multiplication to create a matrix

print("\nMatrix created with multiplication:")
for row in matrix_bad:
    print(row)
# Output will be:
# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 0]

# Now, let’s change one element:
matrix_bad[0][0] = 9
print("\nMatrix after modifying the first element of the first row (using multiplication):")
for row in matrix_bad:
    print(row)
# Output will be:
# [9, 0, 0]
# [9, 0, 0]
# [9, 0, 0]

# Oh no! All rows are affected! Why? Because they all reference the same list.
# This is why list comprehensions are so important and beautiful!

# THANK YOU for taking this journey with us! 
# PLEASE keep practicing with Python, and remember, every piece of code is a new opportunity to learn.
