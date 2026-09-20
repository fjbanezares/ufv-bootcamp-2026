def write_encoded_files(input_string, file_basename):
    # Define the file names for different encodings
    utf8_file = file_basename + '_utf8.txt'
    utf16_file = file_basename + '_utf16.txt'
    ascii_file = file_basename + '_ascii.txt'
    utf32_file = file_basename + '_utf32.txt'
    
    # Write the string to a UTF-8 encoded file
    with open(utf8_file, 'w', encoding='utf-8') as f:
        f.write(input_string)
    print(f"File written: {utf8_file} (UTF-8 encoding)")

    # Write the string to a UTF-16 encoded file
    with open(utf16_file, 'w', encoding='utf-16') as f:
        f.write(input_string)
    print(f"File written: {utf16_file} (UTF-16 encoding)")

    # Write the string to an ASCII encoded file
    try:
        with open(ascii_file, 'w', encoding='ascii') as f:
            f.write(input_string)
        print(f"File written: {ascii_file} (ASCII encoding)")
    except UnicodeEncodeError:
        print(f"Error: The input string contains characters that cannot be encoded in ASCII. File not written: {ascii_file}")

    # Write the string to a UTF-32 encoded file
    with open(utf32_file, 'w', encoding='utf-32') as f:
        f.write(input_string)
    print(f"File written: {utf32_file} (UTF-32 encoding)")

# Example usage
input_string = "Hello, World! 😊"
file_basename = "example"
write_encoded_files(input_string, file_basename)
