# string_methods_exercise.py

# String manipulation is an essential skill in Python. Please follow along with these examples to learn various string methods, slicing, and splitting.

# Example 1: String Methods
# Let's start with some common string methods. Please take note of how each method works!

# capitalize(): Returns a copy of the string with its first character capitalized and the rest in lowercase.
print("helLo".capitalize())  # Output: Hello

# lower(): Converts all characters in the string to lowercase.
print("HELLO".lower())  # Output: hello

# upper(): Converts all characters in the string to uppercase.
print("hello".upper())  # Output: HELLO

# title(): Converts the first character of each word to uppercase and the rest to lowercase.
print("hello worlD".title())  # Output: Hello World

# swapcase(): Swaps the case of each character in the string.
print("HeLLo WoRLd".swapcase())  # Output: hEllO wOrlD

print("\nThank you for learning these basic string methods!")

# Example 2: Stripping Whitespace
# strip(): Removes leading and trailing whitespace from the string.
print("   hello world   ".strip())  # Output: hello world

# Please note: You can also use lstrip() to remove only leading whitespace and rstrip() to remove only trailing whitespace.

# Example 3: Replacing Substrings
# replace(old, new): Replaces all occurrences of the old substring with the new substring.
print("hello world".replace("world", "Python"))  # Output: hello Python

# Example 4: Checking String Start and End
# startswith(prefix): Returns True if the string starts with the specified prefix.
print("hello world".startswith("hello"))  # Output: True

# endswith(suffix): Returns True if the string ends with the specified suffix.
print("hello world".endswith("world"))  # Output: True

# Example 5: Finding Substrings
# find(substring): Returns the lowest index in the string where the substring is found. Returns -1 if the substring is not found.
print("hello world".find("world"))  # Output: 6

# count(substring): Returns the number of non-overlapping occurrences of the substring in the string.
print("hello world, world".count("world"))  # Output: 2

# Example 6: Joining Strings
# join(iterable): Joins the items in the provided iterable (e.g., list or tuple) into a single string. The string on which this method is called is used as the separator.
words = ["hello", "world"]
print(" ".join(words))  # Output: hello world

# Please try using different separators and iterables with join() to see how flexible it is!

# Example 7: Splitting Strings
# split(delimiter): Splits the string into a list of substrings based on the delimiter. If no delimiter is specified, it splits on whitespace.
sentence = "This is a sample sentence."
words = sentence.split()  # Splits on whitespace by default
print(words)  # Output: ['This', 'is', 'a', 'sample', 'sentence.']

data = "John,Doe,25,Engineer"
details = data.split(",")  # Splits on comma
print(details)  # Output: ['John', 'Doe', '25', 'Engineer']

# You can also specify the maximum number of splits with an optional second argument.
data = "apple,banana,cherry,date"
fruits = data.split(",", 2)  # Splits at the first two commas
print(fruits)  # Output: ['apple', 'banana', 'cherry,date']

# Example 8: Slicing Strings
# Slicing is a powerful tool to extract specific parts of a string.
s = "Hello, World!"

# Please take a look at the following slicing examples:
print(s[0:5])  # Output: Hello
print(s[7:12])  # Output: World
print(s[::2])   # Output: Hlo ol!
print(s[::-1])  # Output: !dlroW ,olleH (reverses the string)

# Example 9: Using the input() function
# The input() function reads a line from input and returns it as a string. It's often used to get user input.

# Please enter your name when prompted.
result = input("Please enter your name: ")
print(f"Hello, {result}!")

# Please note: The input() function is blocking, which means it waits for the user to provide input before continuing.
# In multi-threaded applications, managing user input can be challenging. Thank you for your patience as you learn this concept!

# Summary:
# - String methods like capitalize(), lower(), upper(), title(), and swapcase() help modify string cases.
# - Methods like strip(), replace(), startswith(), endswith(), find(), and count() are essential for string manipulation.
# - join() and split() provide powerful ways to combine and separate strings.
# - Slicing allows you to extract parts of strings based on indices.
# - The input() function is useful for getting user input but requires careful management in multi-threaded environments.

# Thank you for exploring these string methods and functions in Python! Please continue practicing these examples to become more comfortable with string manipulation.
