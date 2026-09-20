# This is a dictionary that contains names of students as keys and their scores as values.
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
# We will populate this dictionary with student names as keys and their respective grades as values.
student_grades = {}

# TODO-2: Add grades to student_grades based on student_scores.

# We loop through each student in student_scores.
for student in student_scores:
    # Using the student's score, we determine their grade.
    # If the score is >= 91, the grade is "Outstanding".
    # If the score is >= 81, the grade is "Exceeds Expectations".
    # If the score is >= 71, the grade is "Acceptable".
    # Otherwise, the grade is "Fail".
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# This will print the final dictionary containing student names as keys and their grades as values.
print(student_grades)
