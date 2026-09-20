# Defining a class named 'QuizBrain' that will control the flow of the quiz game.
class QuizBrain:
    # Constructor method to initialize attributes of the QuizBrain object.
    # It takes 'q_list' as an argument which will be a list of Question objects.
    def __init__(self, q_list):
        self.question_number = (
            0  # Keeps track of which question the quiz is currently on.
        )
        self.score = 0  # Keeps track of the user's score.
        self.question_list = q_list  # List of all Question objects to be asked.

    # Method to check if there are still questions left to be asked.
    def still_has_questions(self):
        # Checks if the current question number is less than the total number of questions.
        return self.question_number < len(self.question_list)

    # Method to proceed to the next question in the list.
    def next_question(self):
        current_question = self.question_list[
            self.question_number
        ]  # Fetching the current Question object from the list.
        self.question_number += 1  # Increment the question number by 1.

        # Taking the user's answer. Showing the question text and asking for a True/False answer.
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): "
        )
        # Checking the user's answer and updating the score accordingly.
        self.check_answer(user_answer, current_question.answer)

    # Method to check if the user's answer is correct.
    def check_answer(self, user_answer, correct_answer):
        # Comparing the user's answer with the correct answer.
        # Both are converted to lowercase to make the comparison case-insensitive.
        if user_answer.lower() == correct_answer.lower():
            self.score += 1  # Increment the score by 1 if the answer is correct.
            print("You got it right!")  # Provide feedback to the user.
        else:
            print(
                "That's wrong."
            )  # Provide feedback to the user if the answer is incorrect.

        # Print the correct answer and the current score for the user's reference.
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")  # Print a new line for better readability.
