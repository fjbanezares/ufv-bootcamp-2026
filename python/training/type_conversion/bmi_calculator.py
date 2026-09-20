# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# The `input` function in Python always returns data as a string type.
# This is because whatever is entered by the user is text, even if it's a number.
# Since we need to perform mathematical operations on the height and weight,
# we have to convert these strings into numbers. In this case, we'll use floats
# (floating point numbers) because height and weight can be decimal values.

height_in_m = float(height)  # Convert height string to a floating-point number
# Convert weight string to a floating-point number
weight_in_kg = float(weight)

# The Body Mass Index (BMI) is a measure to check for the amount of body fat
# based on an individual's weight relative to their height. The formula is:
# BMI = weight / height^2
# Here, `**` denotes the power operation in Python. So `height_in_m ** 2` will
# raise the height to the power of 2 (i.e., square the height).
# In the context of the BMI (Body Mass Index) calculation, using integer division (//)
# would not be appropriate because it would result in a loss of precision.

bmi = weight_in_kg / (height_in_m ** 2)

# Finally, we print the calculated BMI. We use the `round` function to limit
# the BMI to 2 decimal places for clarity. The `f-string` (formatted string
# literal) allows us to embed expressions inside string literals, using `{}`.
# This helps in dynamically inserting the BMI value into the string.

print(f"Your BMI is: {round(bmi, 2)}")
