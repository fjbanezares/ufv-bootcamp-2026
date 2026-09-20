print("Welcome to the Love Calculator!")

# Input both names
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Convert the names to lowercase so that our counting is case-insensitive.
combined_names = (name1 + name2).lower()

# Count occurrences of each letter in "TRUE" within the combined names.
t_count = combined_names.count("t")
r_count = combined_names.count("r")
u_count = combined_names.count("u")
e_count = combined_names.count("e")

# Calculate the total for the first digit of the score
true_total = t_count + r_count + u_count + e_count

# Count occurrences of each letter in "LOVE" within the combined names.
l_count = combined_names.count("l")
o_count = combined_names.count("o")
v_count = combined_names.count("v")
# We already have e_count from earlier

# Calculate the total for the second digit of the score
love_total = l_count + o_count + v_count + e_count

# Combine the two totals to get the final love score
love_score = int(str(true_total) + str(love_total))

# Display the result based on the computed score
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
