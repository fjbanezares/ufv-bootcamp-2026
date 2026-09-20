import sys

# Check and print the default encoding used by Python
# sys.getdefaultencoding() returns the default encoding, which should be 'utf-8'
default_encoding = sys.getdefaultencoding()
print(f"Default encoding in Python: {default_encoding}")

# Define a sample string containing both ASCII and non-ASCII characters
# This will help demonstrate encoding with UTF-8
input_string = "Hello, World! 😊"

# Encode the string without specifying the encoding
# This uses the default encoding, which is UTF-8
encoded_string = input_string.encode()
print(f"Encoded string (default encoding): {encoded_string}")

# Decode the encoded string back to a regular string
# This uses the default decoding, which should also be UTF-8
decoded_string = encoded_string.decode()
print(f"Decoded string (default encoding): {decoded_string}")

# Cross-check by explicitly encoding the string using UTF-8
encoded_utf8 = input_string.encode('utf-8')
print(f"Encoded string (explicit UTF-8): {encoded_utf8}")

# Decode the UTF-8 encoded string back to a regular string
decoded_utf8 = encoded_utf8.decode('utf-8')
print(f"Decoded string (explicit UTF-8): {decoded_utf8}")

# Confirm that the encoded bytes are the same whether using default encoding or explicit UTF-8
assert encoded_string == encoded_utf8, "Default encoding is not UTF-8"
print("Default encoding matches explicit UTF-8 encoding.")

# Final friendly message to confirm that everything works as expected
print("All tests passed! UTF-8 is confirmed as the default encoding in Python 3.")
