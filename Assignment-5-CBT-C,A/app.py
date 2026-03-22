from flask import Flask, render_template, request, redirect, url_for
from models import Question, quiz_questions
from datetime import datetime

app = Flask(__name__)

# Stack to store user answers
user_answers = []

@app.route('/')
def home():
    # Redirect to first question
    return redirect(url_for('quiz', q=0))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Get the answer from the form
        answer = request.form.get('answer')
        if answer:  # Ensure something was selected
            user_answers.append(answer)  # push to stack

        # Determine next question
        next_index = int(request.form.get('index')) + 1
        if next_index < len(quiz_questions):
            return redirect(url_for('quiz', q=next_index))
        else:
            return redirect(url_for('result'))

    # GET request
    index = int(request.args.get('q', 0))
    question = quiz_questions[index]
    return render_template("index.html", question=question, index=index)
# Undo 
@app.route('/undo', methods=['POST'])
def undo():
    # Remove last answer from stack
    if user_answers:
        user_answers.pop()

    # Go back to previous question
    prev_index = int(request.form.get('index')) - 1
    if prev_index < 0:
        prev_index = 0
    return redirect(url_for('quiz', q=prev_index))

@app.route('/result')
def result():
    # Calculate score
    score = 0
    for i, ans in enumerate(user_answers):
        if ans.lower() == quiz_questions[i].correct_answer.lower():
            score += 1

    finished_at = datetime.now()
    return render_template("result.html", score=score, total=len(quiz_questions), timestamp=finished_at)

if __name__ == "__main__":
    app.run(debug=True)