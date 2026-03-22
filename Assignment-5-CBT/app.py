# creating flask routing
from flask import Flask, render_template, request
from models import Question

app = Flask(__name__)

# Homepage / quiz start
@app.route('/')
def home():
    return render_template("index.html")

# Quiz page
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Will handle question display & form submission
    pass

# Result page
@app.route('/result')
def result():
    # Calculate score & display
    pass

if __name__ == "__main__":
    app.run(debug=True)
    