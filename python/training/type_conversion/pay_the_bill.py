# Tip Calculator Program
# This program calculates the total amount each person should pay including tip.

# Welcome the user to the tip calculator.
print("Welcome to the tip calculator!")

# Input the total bill amount, expected tip percentage, and the number of people.
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

# Convert the tip percentage to a decimal (e.g., 12% becomes 0.12).
tip_as_percent = tip / 100

# Calculate the total amount of tip based on the bill and the tip percentage.
total_tip_amount = bill * tip_as_percent

# Calculate the total bill including the tip.
total_bill = bill + total_tip_amount

# Split the total bill among the specified number of people.
bill_per_person = total_bill / people

# Format the final amount each person should pay to 2 decimal places.
final_amount = "{:.2f}".format(round(bill_per_person, 2))

# Display the final amount each person should pay.
print(f"Each person should pay: ${final_amount}")
