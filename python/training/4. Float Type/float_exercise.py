import sys

# Basic floating-point numbers
a = 3.14
b = 2.71e2  # Scientific notation for 2.71 * 10^2 = 271.0

# Display the numbers
print(f"a = {a}")  # a = 3.14
print(f"b = {b}")  # b = 271.0

# Demonstrating floating-point precision issues
sum_example = 0.1 + 0.2
print(f"0.1 + 0.2 = {sum_example} (might not be exactly 0.3 due to representation error)")

# Special floating-point values
inf = float('inf')
neg_inf = float('-inf')
nan = float('nan')

# Display the special values
print(f"float('inf') = {inf}")       # inf
print(f"float('-inf') = {neg_inf}")  # -inf
print(f"float('nan') = {nan}")       # nan

# Division by zero with floats
try:
    result = 1.0 / 0
except ZeroDivisionError:
    result = "undefined"
print(f"1.0 / 0 = {result}")  # inf

# sys.float_info provides details about the float representation on the system
print("System float info:", sys.float_info)

# Precision limitations and rounding errors
print(f"Example of precision limitation: 0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False

# Using the decimal module for exact decimal results
from decimal import Decimal

decimal_sum = Decimal('0.1') + Decimal('0.2')
print(f"Using Decimal for exact results: 0.1 + 0.2 = {decimal_sum} (should be exactly 0.3)")

# Special floating-point values in arithmetic
print(f"inf + 1 = {inf + 1}")  # inf
print(f"inf - inf = {inf - inf}")  # nan
print(f"nan == nan: {nan == nan}")  # False, as nan is not equal to itself
