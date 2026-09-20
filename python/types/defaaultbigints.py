# Importing the 'math' module to access mathematical functions
import math

# Using the sqrt function from the math module to calculate the square root of 81
print(math.sqrt(81))  # Expected output: 9.0

# Finding the factorial of 5 using the factorial function from the math module
print(math.factorial(5))  # Expected output: 120

# Factorial of 16
print(math.factorial(16))  # Expected output: 20922789888000

# Setting values for n and k
n = 5
k = 3

# Calculating combination (n choose k) using factorials
# This formula is derived from the combination formula: n! / (k! * (n-k)!)
combination = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
print(combination)  # Expected output: 10.0

# Using an alternative way to import the factorial function, which avoids prefixing with the module name
from math import factorial

# Using the imported factorial function directly
print(factorial(n) / (factorial(k) * factorial(n - k)))  # Expected output: 10.0

# Renaming the imported factorial function for convenience
from math import factorial as fac

# Using the renamed factorial function (fac)
print(fac(n) / (fac(k) * fac(n - k)))  # Expected output: 10.0

# Demonstrating integer division (returns the quotient without the remainder)
print(fac(n) // (fac(k) * fac(n - k)))  # Expected output: 10

# Calculating 2 raised to the power of 31 minus 1
print(2**31 - 1)  # Expected output: 2147483647

# Checking if factorial of 13 is greater than 2^31 - 1
print(fac(13) > 2**31 - 1)  # Expected output: True

# Setting new values for n and k
n = 100
k = 2

# Calculating combination (n choose k) for larger values using integer division
print(fac(n) // (fac(k) * fac(n - k)))  # Expected output: 4950

# Printing the factorial of 100
print(fac(n))  

# Demonstrating how to find the length (number of digits) of factorial of 100
print(len(str(fac(n))))  # Expected output: 158

# Python excels at seamlessly handling arbitrarily large
#  integers, unlike many languages which are constrained by 
# fixed-size integer data types.