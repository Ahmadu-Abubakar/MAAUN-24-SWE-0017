from flask import Flask, render_template, request, redirect, url_for
from models import Question, quiz_questions
from datetime import datetime

app = Flask(__name__)

# Store user answers in a stack (LIFO)
user_answers = []

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Get the answer from the form
        answer = request.form.get('answer')
        user_answers.append(answer)  # push to stack
        next_index = int(request.form.get('index')) + 1
        if next_index < len(quiz_questions):
            return redirect(url_for('quiz', q=next_index))
        else:
            return redirect(url_for('result'))

    # GET request
    index = int(request.args.get('q', 0))
    question = quiz_questions[index]
    return render_template("index.html", question=question, index=index)


@app.route('/result')
def result():
    # Calculate score
    score = 0
    for i, ans in enumerate(user_answers):
        if ans.lower() == quiz_questions[i].correct_answer.lower():
            score += 1

    finished_at = datetime.now()
    return render_template("result.html", score=score, total=len(quiz_questions), timestamp=finished_at)

# adding undo features
@app.route('/undo', methods=['POST'])
def undo():
    if user_answers:
        user_answers.pop()  # Remove the last answer (LIFO)
    # Go back to the previous question
    prev_index = int(request.form.get('index')) - 1
    if prev_index < 0:
        prev_index = 0
    return redirect(url_for('quiz', q=prev_index))


if __name__ == "__main__":
    app.run(debug=True)