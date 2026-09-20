# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# 1. Ensure that the entered value is of length 2. If not, print an error.
if len(two_digit_number) != 2:
    print("Please enter a valid two digit number.")
else:
    # 2. Extract the first and second digits.
    # For a string '35', two_digit_number[0] will be '3' and two_digit_number[1] will be '5'
    first_digit = int(two_digit_number[0])
    second_digit = int(two_digit_number[1])

    # 3. Sum the two digits.
    result = first_digit + second_digit

    # 4. Print the result.
    print(f"The sum of the digits is: {result}")
