# Importing the random module
import random

# Thanks for using random module! Let's start with some basics.

# 1. Random float between 0 and 1 (basic use)
# random.random() generates a random float in the range [0.0, 1.0)
print("Random float between 0 and 1:", random.random())  # Example: 0.674615
# Thanks for checking out the random float generation!

# 2. Random integer between two values using random.randint(a, b)
# Please note: 'a' and 'b' are inclusive
print("Random integer between 1 and 10:", random.randint(1, 10))  # Example: 7

# 3. Random range within specified start, stop, and step using random.randrange()
# This is useful when you want a random integer with specific steps.
print("Random integer from range(0, 100, 10):", random.randrange(0, 100, 10))  # Example: 40

# 4. Random selection from a list using random.choice()
fruits = ["apple", "banana", "cherry", "orange"]
random_fruit = random.choice(fruits)
print(f"Random fruit from the list {fruits}:", random_fruit)  # Example: "cherry"

# 5. Randomly shuffling a list in place using random.shuffle()
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
random.shuffle(numbers)
print("Shuffled list:", numbers)  # Example: [3, 5, 1, 4, 2]

# 6. Generating a random sample of elements from a population using random.sample()
# It returns a new list containing a specified number of unique elements.
population = list(range(1, 21))  # Create a population of numbers 1 to 20
sampled_numbers = random.sample(population, 5)  # Get 5 unique random numbers
print("Random sample of 5 numbers from the population:", sampled_numbers)

# Moving to advanced examples! Thanks for sticking with it.

# 7. Seeding the random number generator using random.seed()
# Using seed() allows the randomness to be predictable for reproducibility.
random.seed(10)
print("With seed 10, random integer between 1 and 10:", random.randint(1, 10))  # Example: 9

# Resetting the seed ensures the same random values appear again.
random.seed(10)
print("Reset seed 10, same random integer:", random.randint(1, 10))  # Example: 9

# Advanced! Let's use random for cryptographic-like scenarios where high randomness is needed.

# 8. Secure random number generation with the secrets module (recommended for cryptography)
import secrets
# secrets.randbelow(n) gives a secure random integer in the range [0, n)
secure_random_int = secrets.randbelow(100)
print("Secure random integer less than 100:", secure_random_int)

# secrets.choice(seq) picks a random element securely from a sequence
secure_fruit = secrets.choice(fruits)
print(f"Secure random choice from {fruits}:", secure_fruit)

# 9. Random floating point numbers in different ranges with random.uniform(a, b)
print("Random float between 10 and 20:", random.uniform(10, 20))  # Example: 15.75322

# 10. Random boolean-like values with random.choice
print("Random Boolean value (True/False):", random.choice([True, False]))  # Example: True

# 11. Non-integer random ranges using random.triangular()
# random.triangular() is useful for distribution with more control over where values are centered.
# It generates a float with a triangular distribution between two bounds, with an optional mode.
print("Random triangular number between 1 and 10 (mode=5):", random.triangular(1, 10, 5))

# We’re wrapping up now! Hopefully, you found these examples useful. Thanks again for learning about the random module.
