# string_literals_and_escape_characters.py

# Please note: In Python, strings can be enclosed in either single quotes (' ') or double quotes (" ").
# This provides flexibility and makes it easier to use quotes within strings.

# Using single quotes
single_quoted_string = 'using single quotes.'
print(single_quoted_string)

# Using double quotes
double_quoted_string = "using double quotes."
print(double_quoted_string)

print("\nThank you for understanding the basics of string literals!")

# Please understand: If you want to include a single quote inside a single-quoted string, you need to escape it with a backslash (\).
quote_within = 'It\'s a sunny day.'
print(quote_within)

# Similarly, to use a double quote inside a double-quoted string, you escape it with a backslash (\).
quote_within_double = "She said, \"Hello, World!\""
print(quote_within_double)

# Also, remember: Using different types of quotes can avoid the need for escaping.
# For instance, if a string contains a lot of single quotes, it might be more convenient to use double quotes to enclose the string.

# A string containing single quotes, easier with double quotes around it
string_with_single_quotes = "It's easier to use double quotes here."
print(string_with_single_quotes)

# A string containing double quotes, easier with single quotes around it
string_with_double_quotes = 'She prefers the term "expert".'
print(string_with_double_quotes)

print("\nThank you for using different quotes to make your strings clearer!")

# Please note: Python also provides raw string notation, which is very useful when you want to avoid escaping backslashes.
# This is common in regular expressions, file paths, etc.

# Example of a raw string
raw_string = r"This is a raw string. It won't interpret \n as a newline."
print(raw_string)

# Please see: Using a raw string prevents the backslash from being treated as an escape character.
# Instead, it treats the backslash as a literal character.

# Dealing with multiple lines in strings
# You can use the newline escape sequence (\n) to insert a newline character within a string.

single_line_string = "Hello\nWorld"
print(single_line_string)
# Output:
# Hello
# World

# Also, for multi-line strings or docstrings, Python provides triple single quotes (''') or triple double quotes (""").
multiline_string = """Hello World
This is a multiline string."""
print(multiline_string)

# The triple quotes allow for multiple lines of text without the need for newline characters.
# This is very useful for writing docstrings or any text that spans several lines.

# Please remember: On Windows, the newline character is represented as \r\n, but Python handles this platform-specific detail for you.
# You can usually just use \n for consistency.

# Thank you for learning how to effectively use strings in Python!
# Please feel free to explore more about strings and practice writing different types of strings to get comfortable with these concepts.


