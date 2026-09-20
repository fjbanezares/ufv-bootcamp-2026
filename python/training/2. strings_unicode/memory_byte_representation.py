import ctypes

# Define a string
input_string = "Hello, World! 😊"

# By default, Python 3 uses UTF-8 encoding for strings.
# This means that internally, the string is represented using Unicode code points,
# and when encoded without specifying an encoding, UTF-8 is used.

# Create a ctypes string buffer for UTF-32 encoding
buffer_utf32 = ctypes.create_string_buffer(input_string.encode('utf-32'))

# Print the raw bytes from the UTF-32 buffer
print("Raw bytes in memory (UTF-32 encoding):")
for byte in buffer_utf32.raw:
    print(f"{byte:02x}", end=" ")
print()

# Create a ctypes string buffer for UTF-8 encoding
buffer_utf8 = ctypes.create_string_buffer(input_string.encode('utf-8'))

# Print the raw bytes from the UTF-8 buffer
print("Raw bytes in memory (UTF-8 encoding):")
for byte in buffer_utf8.raw:
    print(f"{byte:02x}", end=" ")
print()

# Create a ctypes string buffer for UTF-16 encoding
buffer_utf16 = ctypes.create_string_buffer(input_string.encode('utf-16'))

# Print the raw bytes from the UTF-16 buffer
print("Raw bytes in memory (UTF-16 encoding):")
for byte in buffer_utf16.raw:
    print(f"{byte:02x}", end=" ")
print()

# Create a ctypes string buffer for ASCII encoding
# Note: This will raise an exception if the string contains non-ASCII characters.
try:
    buffer_ascii = ctypes.create_string_buffer(input_string.encode('ascii'))
    # Print the raw bytes from the ASCII buffer
    print("Raw bytes in memory (ASCII encoding):")
    for byte in buffer_ascii.raw:
        print(f"{byte:02x}", end=" ")
    print()
except UnicodeEncodeError as e:
    print(f"Error: {e}")

# Print the buffers
print("UTF-32 Buffer:", buffer_utf32)
print("UTF-8 Buffer:", buffer_utf8)
print("UTF-16 Buffer:", buffer_utf16)
print("ASCII Buffer:", buffer_ascii)  # This will only print if encoding is successful

