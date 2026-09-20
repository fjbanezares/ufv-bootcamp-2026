# 🚨 Don't change the code below 👇
# Prompt the user for a string of student scores separated by spaces.
student_scores = input("Input a list of student scores ").split()

# This loop iterates over the range of the length of student_scores.
# The purpose is to convert each string value in the student_scores list to an integer.
# For instance, "78" becomes 78 (an integer).
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Print the resulting list of integer student scores for reference.
print(student_scores)
# 🚨 Don't change the code above 👆

# Here's our plan:
# We'll start by assuming that the first score is the highest.
# Then we'll iterate through the list, and whenever we find a score that is higher than our current highest,
# we'll update the highest score.

# Initialize the highest_score variable with the first student's score.
highest_score = student_scores[0]

# Start iterating from the 1st index (since 0th index is already taken as initial highest score).
for score in student_scores:
    # Check if the current score is greater than the highest_score.
    if score > highest_score:
        # If it is, update highest_score with the current score.
        highest_score = score

# Once all scores have been checked, print the highest score found.
print(f"The highest score in the class is: {highest_score}")
