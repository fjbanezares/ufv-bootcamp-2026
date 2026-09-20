import sys

# Define a string
input_string = "Hello, World! 😊"

# Get the byte representation in different encodings
utf8_bytes = input_string.encode('utf-8')
utf16_bytes = input_string.encode('utf-16')
utf32_bytes = input_string.encode('utf-32')

# Print the byte representations
print(f"UTF-8 bytes: {utf8_bytes}")
print(f"UTF-16 bytes: {utf16_bytes}")
print(f"UTF-32 bytes: {utf32_bytes}")

# Using sys.getsizeof to see memory usage
print(f"Memory size of string in Python: {sys.getsizeof(input_string)} bytes")
