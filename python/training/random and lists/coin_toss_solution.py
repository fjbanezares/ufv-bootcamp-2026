# To use random functions, we need to import the random module.
import random

# Generate a random number: either 0 or 1.
random_side = random.randint(0, 1)

# Check the random number and print the appropriate result.
if random_side == 1:
    print("Heads")
else:
    print("Tails")
