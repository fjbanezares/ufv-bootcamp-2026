# challenge.py

# CHALLENGE: Break this single file into multiple files: data.py, question_model.py, quiz_brain.py, and main.py.
# Use appropriate Python import statements to bring everything back together.

# ------ data.py ------
# Challenge: Move this data to a separate file called data.py
question_data = [
    {"question": "The Earth is round.", "correct_answer": "True"},
    {"question": "The Earth is flat.", "correct_answer": "False"},
]

# ------ question_model.py ------
# Challenge: Move this class definition to a separate file called question_model.py


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


# ------ quiz_brain.py ------
# Challenge: Move this class definition to a separate file called quiz_brain.py


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        # Challenge: Complete this method.
        pass

    def next_question(self):
        # Challenge: Complete this method.
        pass

    def check_answer(self, user_answer, correct_answer):
        # Challenge: Complete this method.
        pass


# ------ main.py ------
# Challenge: Move this part of the code to a separate file called main.py

# Create question objects from the data
question_bank = []
for question in question_data:
    # Challenge: Complete this part.
    pass

# Initialize QuizBrain with question objects
quiz = QuizBrain(question_bank)

# Loop through questions and ask them until no questions remain
while quiz.still_has_questions():
    # Challenge: Complete this part.
    pass

# Final score
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
