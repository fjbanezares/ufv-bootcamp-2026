# Get input values for a and b
a = input("a: ")
b = input("b: ")

####################################
# Swap the values of a and b
# Python provides a very intuitive way to swap variables.
# The idea is to use tuple unpacking. The expression on the right-hand side creates a tuple (b, a)
# and then immediately unpacks it into the variables on the left-hand side (a, b).
# As a result, the values of a and b are swapped.

a, b = b, a
####################################

# Print the swapped values
print("a: " + a)
print("b: " + b)
