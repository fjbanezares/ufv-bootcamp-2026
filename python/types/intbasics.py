import sys

print(sys.float_info)


# In Python, integers can be expressed in different bases. By default, they are in base 10.
number_base10 = 10
print(number_base10)  # Output: 10

# Binary representation starts with '0b' or '0B'.
number_base2 = 0b10
print(number_base2)  # Output: 2 (This is the binary representation of the number 2)

# Octal representation starts with '0o' or '0O'.
number_base8 = 0o10
print(number_base8)  # Output: 8 (This is the octal representation of the number 8)

# Hexadecimal representation starts with '0x' or '0X'.
number_base16 = 0x10
print(
    number_base16
)  # Output: 16 (This is the hexadecimal representation of the number 16)

# You can convert a floating-point number to an integer using the 'int()' function.
# Note: This will truncate the decimal, not round it.
converted_float1 = int(3.5)
print(converted_float1)  # Output: 3

converted_float2 = int(-3.5)
print(converted_float2)  # Output: -3 (Note the truncation towards 0)

# The 'int()' function can also be used to convert a string representation of a number into an integer.
converted_string = int("496")
print(converted_string)  # Output: 496

# The 'int()' function allows conversion from different bases.
# Here, the string "10000" is interpreted as a base-3 number.
converted_base3 = int("10000", 3)
print(converted_base3)  # Output: 81 (In base-10, "10000" in base-3 is equivalent to 81)
