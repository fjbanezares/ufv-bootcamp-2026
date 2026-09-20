# bytes_in_python.py

# Please note: This script will demonstrate various operations with bytes in Python.
# Thank you for following along! Let's dive deep into the topic.

# 1. Creating bytes from a string with encoding
# Please create a bytes object by encoding a string into bytes using a specific encoding.
b = bytes("Hello, World!", "utf-8")

# Let's print the bytes object. Note the b' prefix indicating a bytes literal.
print(b)  # Output: b'Hello, World!'

# Please note: The "utf-8" encoding is used to convert the string to bytes.
# UTF-8 is a standard encoding format that can represent all characters in Unicode.

# 2. Creating bytes from a list of integers
# Bytes can also be created from a list of integers where each integer is in the range 0 <= x < 256.
b_from_ints = bytes([72, 69, 76, 76, 79])

# Let's print the bytes object created from integers.
print(b_from_ints)  # Output: b'HELLO'

# Please note: Each integer represents a byte. 72 is 'H', 69 is 'E', and so on in ASCII.

# 3. Creating a bytearray from a list of integers
# Bytearray is a mutable version of bytes. You can modify the contents of a bytearray.
b_arr = bytearray([72, 69, 76, 76, 79])

# Modifying the first byte in the bytearray
b_arr[0] = 104  # ASCII for 'h'

# Let's print the modified bytearray.
print(b_arr)  # Output: bytearray(b'hELLO')

# Thank you for exploring bytes and bytearrays! Please continue to the next section to learn about indexing and slicing.

# 4. Indexing and Slicing with Bytes
# Like strings, bytes objects support indexing and slicing.

# Let's access individual bytes using indexing
print(b[0])  # Output: 72 (ASCII for 'H')
print(b[1])  # Output: 101 (ASCII for 'e')

# Please perform slicing to get a part of the bytes
print(b[1:5])  # Output: b'ello'

# Please note: The slice b[1:5] returns a new bytes object starting from index 1 up to (but not including) index 5.

# 5. Finding and Counting Substrings in Bytes
# The find method returns the index of the first occurrence of a substring.

# Let's find the index of a substring in bytes
index = b.find(b'World')
print(index)  # Output: 7

# Please note: The substring 'World' starts at index 7 in the bytes object.

# Counting the number of occurrences of a byte
count = b.count(b'l')
print(count)  # Output: 3

# Please note: The byte 'l' occurs three times in the bytes object.

# 6. Replacing Substrings in Bytes
# The replace method replaces occurrences of a substring with another.

# Please replace 'World' with 'Python' in the bytes object.
b_replaced = b.replace(b'World', b'Python')
print(b_replaced)  # Output: b'Hello, Python!'

# Thank you for learning about bytes with us! We hope you now understand the basics of working with bytes in Python.
# Please try creating bytes and bytearrays from different inputs and perform various operations to solidify your understanding.

# 7. Practical Use Case: Reading Binary Data
# In real-world applications, you often work with bytes when handling files, network data, or other binary formats.

# Let's simulate reading raw bytes from a file (here, we'll use bytes directly for demonstration)
file_data = bytes([0x50, 0x4B, 0x03, 0x04])  # Example bytes, resembling the start of a ZIP file

# Please note: When reading files in binary mode, you'd use something like:
# with open('example.zip', 'rb') as f:
#     file_data = f.read()

# Let's print the raw file data
print(file_data)  # Output: b'PK\x03\x04'

# Please note: Understanding bytes is crucial when you need to manipulate raw binary data, such as in file I/O or network communication.
# Thank you for diving into bytes in Python! Please practice more to become proficient in handling bytes and bytearrays.
