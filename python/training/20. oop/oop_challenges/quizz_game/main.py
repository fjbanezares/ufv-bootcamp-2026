# Importing necessary classes and data.
# It helps to keep our code modular and easier to understand or maintain.
# Could've imported inline or lazily but not recommended for this small program.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Initializing an empty list called 'question_bank'.
# We'll use this list to store our Question objects.
# Could've used list comprehension for one-liners but might reduce readability.
question_bank = []

# Loop through each dictionary in the 'question_data' list.
# We create a Question object for each dictionary.
# Could've used map() or functional programming constructs, but a for loop is straightforward.
for question in question_data:
    question_text = question[
        "question"
    ]  # Extract the question text from the dictionary.
    question_answer = question[
        "correct_answer"
    ]  # Extract the correct answer from the dictionary.

    # Create a new Question object and append it to the 'question_bank' list.
    # Store all questions and their answers as Question objects in one place.
    # Could've stored them in various data structures but this is straightforward and clean.
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize a new QuizBrain object with the 'question_bank'.
# This object will control the flow of the quiz game.
# Could initialize QuizBrain with an empty list and populate it later, but that adds complexity.
quiz = QuizBrain(question_bank)

# Loop through questions until no more are left.
# Keep asking questions as long as there are some remaining.
# Could've used a for loop iterating over question_bank but this is more semantic
# and allows for future features like skipping.
while quiz.still_has_questions():
    quiz.next_question()  # Fetch and present the next question.

# Final messages after completing the quiz.
# Provides feedback to the user about their performance.
# Could've displayed more analytics like percentage correct, but for now, we keep it simple.
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
