# 🚨 Don't change the code below 👇
# Prompt the user for a string of student heights separated by spaces.
student_heights = input("Input a list of student heights ").split()

# This loop iterates over the range of the length of student_heights.
# The purpose is to convert each string value in the student_heights list to an integer.
# For instance, "180" becomes 180 (an integer).
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Initialize variables:
# total_height will hold the sum of all student heights.
# number_of_students will keep count of the number of students.
total_height = 0
number_of_students = 0

# The following loop will iterate through each height in student_heights.
# For each height:
# 1. It will be added to total_height.
# 2. The count for number_of_students will be incremented by 1.
for height in student_heights:
    total_height += height  # Adding the current height to the total height.
    number_of_students += 1  # Increasing the count of students by 1.

# Calculate the average height.
# We do this by dividing the total height by the number of students.
# The result is then rounded to the nearest whole number using the round() function.
average_height = round(total_height / number_of_students)

# Finally, print the calculated average height.
print(average_height)
