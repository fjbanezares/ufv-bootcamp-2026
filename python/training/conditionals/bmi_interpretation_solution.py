# Start by taking the user's height and weight as inputs.

print(type("default string"))  # <class 'str'>

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


# Calculate the BMI using the formula: weight / (height^2)
bmi = weight / (height ** 2)

# Now, based on the calculated BMI, provide the interpretation.
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f}. You have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f}. You are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi:.2f}. You are obese.")
else:
    print(f"Your BMI is {bmi:.2f}. You are clinically obese.")

# The program calculates the BMI first and then uses a series of conditional
# checks (if-elif-else) to determine and print the user's weight category.
