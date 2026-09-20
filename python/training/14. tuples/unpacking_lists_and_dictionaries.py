# Example of Unpacking with Lists
# Let's unpack a list with more elements than variables.

# List with five elements
numbers = [1, 2, 3, 4, 5]

# Unpacking the first two and capturing the rest with *
first, second, *remaining = numbers

print("First number:", first)  # Output: First number: 1
print("Second number:", second)  # Output: Second number: 2
print("Remaining numbers:", remaining)  # Output: Remaining numbers: [3, 4, 5]

# Example of Unpacking with Dictionaries
# Dictionaries can be unpacked by using .items(), .keys(), or .values().

# Dictionary of fruits with their colors
fruit_colors = {"apple": "red", "banana": "yellow", "cherry": "red"}

# Unpacking only the keys using .keys()
for fruit in fruit_colors.keys():
    print("Fruit:", fruit)

# Output:
# Fruit: apple
# Fruit: banana
# Fruit: cherry

# Unpacking both keys and values using .items()
for fruit, color in fruit_colors.items():
    print(f"{fruit.capitalize()} is {color}.")

# Output:
# Apple is red.
# Banana is yellow.
# Cherry is red.

# Unpacking values directly, notice you only get the values.
for color in fruit_colors.values():
    print("Color:", color)

# Output:
# Color: red
# Color: yellow
# Color: red

# Thank you for reviewing these examples!
# Please make sure to experiment with unpacking to fully grasp its versatility.
