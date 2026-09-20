# Defining a class called Question to model a trivia question
class Question:
    # This is the constructor method (__init__) for the class.
    # When a new object is created based on this class, this method gets called.
    # It sets up the initial attributes of the object.
    # The 'self' parameter refers to the instance (object) itself, and is automatically passed by Python.
    # 'q_text' is the question text that will be passed when creating an object.
    # 'q_answer' is the answer to the question that will also be passed when creating an object.
    def __init__(self, q_text, q_answer):
        # The 'self.text' attribute is initialized with the value of 'q_text' passed to the constructor.
        # This attribute holds the text for each trivia question.
        self.text = q_text

        # The 'self.answer' attribute is initialized with the value of 'q_answer' passed to the constructor.
        # This attribute holds the answer to each trivia question (True or False).
        self.answer = q_answer
