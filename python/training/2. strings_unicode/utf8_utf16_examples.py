def utf8_binary_representation(character: str) -> str:
    """
    Converts a character to its binary representation using UTF-8 encoding.

    Args:
        character (str): A single character.

    Returns:
        str: The binary representation of the UTF-8 encoded character.
    """
    utf8_encoded = character.encode('utf-8')
    binary_repr = ' '.join(format(byte, '08b') for byte in utf8_encoded)
    return binary_repr

def utf16_binary_representation(character: str) -> str:
    """
    Converts a character to its binary representation using UTF-16 encoding.

    Args:
        character (str): A single character.

    Returns:
        str: The binary representation of the UTF-16 encoded character.
    """
    utf16_encoded = character.encode('utf-16')
    binary_repr = ' '.join(format(byte, '08b') for byte in utf16_encoded)
    return binary_repr

def render_character_info(character: str) -> None:
    """
    Displays the Unicode code point, UTF-8 binary representation, and UTF-16 binary representation of a character.

    Args:
        character (str): A single character.
    """
    utf8_binary = utf8_binary_representation(character)
    utf16_binary = utf16_binary_representation(character)
    print(f"Character: {character}")
    print(f"Unicode Code Point: U+{ord(character):04X}")
    print(f"UTF-8 Binary: {utf8_binary}")
    print(f"UTF-16 Binary: {utf16_binary}")

# Example usage for 'A' (BMP character)
render_character_info('A')

# Example usage for 'é' (BMP character)
render_character_info('é')

# Example usage for '中' (BMP character)
render_character_info('中')

# Example usage for '𐍈' (Character beyond BMP)
render_character_info('𐍈')

# Example usage for '😃' (Emoji character beyond BMP)
render_character_info('😃')
