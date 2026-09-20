# Let's start by taking the user input.
number = int(input("Which number do you want to check? "))

# The modulo operator % returns the remainder of a division.
# If a number is even, it is cleanly divisible by 2, i.e., the remainder is 0.
# Otherwise, it's odd.
if number % 2 == 0:
    # If the remainder is 0, the number is even.
    print(f"The number {number} is an even number.")
else:
    # If there's any remainder, the number is odd.
    print(f"The number {number} is an odd number.")

# An important aspect here is the use of the modulo operator.
# It divides the number on the left by the number on the right and returns the remainder.
# So, for any even number, "number % 2" will always be 0.
# For an odd number, "number % 2" will be 1.
