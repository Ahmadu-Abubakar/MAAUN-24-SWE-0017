# models.py

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()


# Example questions
quiz_questions = [
    Question(
        "What is a set in mathematics?",
        ["A collection of ordered numbers",
         "A collection of well-defined distinct objects",
         "A group of random variables",
         "A sequence of numbers"],
        "b"
    ),
    Question(
        "Which of the following is a programming language?",
        ["HTML", "CSS", "Python", "HTTPs"],
        "c"
    ),
    Question(
        "Which data structure follows LIFO principle?",
        ["Queue", "Tree", "Graph", "Stack"],
        "d"
    )
]