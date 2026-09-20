# ASCII and Unicode Example

def print_binary_representation(text: str) -> None:
    print(f"Text: {text}")
    for char in text:
        binary_repr = format(ord(char), '08b')
        print(f"Character: {char}, ASCII Code: {ord(char)}, Binary: {binary_repr}")

# ASCII Example
ascii_text = "Hello"
print("ASCII Example:")
print_binary_representation(ascii_text)

print("\nUnicode Example:")
# Unicode Example with some non-ASCII characters
unicode_text = "Hello, 世界"  # "Hello, World" in English and Chinese
for char in unicode_text:
    # Unicode characters can be multiple bytes long, use 'utf-8' encoding to show this
    utf8_encoded = char.encode('utf-8')
    binary_repr = ' '.join(format(byte, '08b') for byte in utf8_encoded)
    print(f"Character: {char}, Unicode Code Point: U+{ord(char):04X}, Binary: {binary_repr}")

# Explanation:
# ASCII Example:
# - ASCII characters are represented using 7 or 8 bits (1 byte).
# - The text "Hello" is shown with each character's ASCII code and binary representation.
# Unicode Example:
# - Unicode characters can be more than 1 byte long.
# - The text "Hello, 世界" includes ASCII and non-ASCII characters.
# - Non-ASCII characters are encoded in UTF-8, where each character may use multiple bytes.
# - The binary representation of each character is shown, highlighting the difference in encoding length.
