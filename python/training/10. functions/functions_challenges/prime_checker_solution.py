def is_prime(number):
    """Check if a given number is prime."""
    # 0 and 1 are not prime numbers
    if number <= 1:
        return False

    # Check each number from 2 up to the square root of the input number
    # We check up to the square root because a larger factor of the number must be a multiple of a smaller factor that has been already checked.
    for i in range(2, int(number ** 0.5) + 1):
        # If number is divisible by any i then it is not a prime number
        if number % i == 0:
            return False
    return True


def prime_checker(number):
    """Prints whether a number is prime or not."""
    if is_prime(number):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Taking user input and calling the function
n = int(input("Check this number: "))
prime_checker(number=n)
