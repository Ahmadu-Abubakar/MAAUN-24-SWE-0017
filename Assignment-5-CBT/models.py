from datetime import datetime

# finishing time
finished_at = datetime.now()

# Questions object
class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()
# answer(stack)
user_answer = []

