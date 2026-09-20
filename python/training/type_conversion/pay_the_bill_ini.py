# Tip Calculator Challenge
# Fill in the missing code to complete the tip calculator program!

print("Welcome to the tip calculator!")
bill = _______(input("What was the total bill? $"))
tip = _______(input("How much tip would you like to give? 10, 12, or 15? "))
people = _______(input("How many people to split the bill?"))

# Calculate the tip as a percentage.
tip_as_percent = _______

# Calculate the total amount of tip.
total_tip_amount = _______

# Calculate the total bill including the tip.
total_bill = _______

# Split the total bill among the people.
bill_per_person = _______

# Format the amount each person should pay.
final_amount = "{:.2f}".format(_______(bill_per_person, 2))

print(f"Each person should pay: ${final_amount}")
