def ascii_to_binary(character: str) -> str:
    """
    Converts an ASCII character to its binary representation.

    Args:
        character (str): A single ASCII character.

    Returns:
        str: The binary representation of the ASCII character.
    """
    # ord() function gets the ASCII code (decimal) of the character
    ascii_code = ord(character)
    # format() function converts the ASCII code to an 8-bit binary string
    binary_repr = format(ascii_code, '08b')
    return binary_repr

def render_character(character: str) -> None:
    """
    Simulates the process of rendering a character on the screen by displaying
    its ASCII code and binary representation.

    Args:
        character (str): A single ASCII character.
    """
    # Get the binary representation of the character
    binary_repr = ascii_to_binary(character)
    
    # Print the character
    print(f"Character: {character}")
    
    # Print the ASCII code of the character
    print(f"ASCII Code: {ord(character)}")
    
    # Print the binary representation of the character
    print(f"Binary Representation: {binary_repr}")

# Example usage: render the character '0'
#character = '0'
character = '世'
character = '😎'



render_character(character)


# Output Explanation:
# Character: 0
# The character '0' that was input.
# ASCII Code: 48
# The ASCII code for '0' is 48 in decimal.
# Binary Representation: 00110000
# The binary representation of the ASCII code 48, which is 00110000 in 8-bit binary form.
