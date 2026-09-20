# Naïve vs. Pro Error Handling in Python
# Please go through each example to see the differences in handling errors. Thanks!

# First, let's define our DIGIT_MAP for conversion
DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# Naïve approach to converting string numbers to integers
def convert_naive(s):
    """Convert a list of strings to an integer, return -1 if conversion fails."""
    try:
        number = ""

        # Loop through each string token in the list
        for token in s:
            # Attempt to append its corresponding digit from DIGIT_MAP
            number += DIGIT_MAP[token]

        # Convert the final string to an integer
        x = int(number)

        # Print the successful conversion (not ideal for reusable code)
        print(f"Conversion succeeded! x = {x}")
    except (KeyError, TypeError):
        # Catching broad exceptions makes it unclear what went wrong
        print("Conversion failed!")
        return -1

    # Return the converted integer if successful
    return x

# Pro approach with custom error handling
class ConversionError(Exception):
    """Custom exception for conversion failures."""
    pass

def convert_pro(s):
    """Convert a list of strings to an integer with improved error handling."""
    # Validate the input is a list or tuple, raising a specific exception if not
    if not isinstance(s, (list, tuple)):
        raise ConversionError("Input must be a list or tuple of strings.")

    number = ""
    for token in s:
        # Check if each token is valid, providing a specific error if not
        if token not in DIGIT_MAP:
            raise ConversionError(f"'{token}' is not a valid string number.")

        # Append the corresponding digit to the number string
        number += DIGIT_MAP[token]

    # Convert the assembled string to an integer and return it
    return int(number)

# Let's test both functions with the same input
inputs = [
    ['one', 'two', 'three'],     # Valid input
    ['ten', 'two', 'three'],     # Invalid input - 'ten' is not in DIGIT_MAP
    'onetwothree',               # Invalid input type - not a list or tuple
    ['one', 'three', 'banana']   # Invalid input - 'banana' is not in DIGIT_MAP
]

print("\nTesting Naïve Approach:")
for i, input_value in enumerate(inputs, start=1):
    print(f"\nTest {i}: Input = {input_value}")
    result = convert_naive(input_value)
    print(f"Result: {result}")

print("\nTesting Pro Approach:")
for i, input_value in enumerate(inputs, start=1):
    print(f"\nTest {i}: Input = {input_value}")
    try:
        result = convert_pro(input_value)
        print(f"Conversion succeeded! Result: {result}")
    except ConversionError as e:
        # Thanks for catching errors with a detailed message!
        print(f"Conversion failed! Error: {e}")

# Please note:
# - The naive function is likely to return -1 and print generic error messages.
# - The pro function provides specific exceptions and avoids printing directly,
#   making it better for real-world applications and debugging.
