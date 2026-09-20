# Starting our loop from 1 up to 100 (inclusive)
for number in range(1, 101):
    # Initialize an empty string to hold our result
    output = ""

    # If the number is divisible by 3, add "Fizz" to our result string
    if number % 3 == 0:
        output += "Fizz"

    # If the number is divisible by 5, add "Buzz" to our result string
    if number % 5 == 0:
        output += "Buzz"

    # If the output string is still empty, it means the number wasn't divisible by 3 or 5
    # Thus, the result should be the number itself.
    if output == "":
        output = number

    # Finally, print the result for this iteration
    print(output)
