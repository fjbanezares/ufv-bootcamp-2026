# 🚨 Initialization Section - Don't change the code below 👇
# Get student scores as a string input, split at spaces, resulting in a list of strings.
student_scores = input("Input a list of student scores ").split()

# Convert each string in the list to an integer using a for loop.
# This is done because the split() function converts input into a list of strings,
# but we want a list of integers for our calculations.
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Print the processed list for reference.
print(student_scores)
# 🚨 End of Initialization Section

# 📝 Problem-solving Strategy:
# 1. Assume the first score in the list as the highest.
# 2. Iterate through each score in the list.
# 3. If the current score is higher than the highest assumed so far, update the highest score.
# 4. Continue this process for all scores.
# 5. By the end of the loop, we'll have the highest score.

# Set the first score as the highest score initially.
highest_score = student_scores[0]

# Iterate through every score in the list starting from the first score.
for score in student_scores:
    # Compare each score with the current highest_score.
    if score > highest_score:
        # If the current score is greater than the highest_score, update highest_score.
        highest_score = score

# Print out the highest score after processing all scores.
print(f"The highest score in the class is: {highest_score}")
