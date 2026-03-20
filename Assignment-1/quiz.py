
print("==== MINI QUIZ APP ====")
quiz = [
    {
        "question" : "what is a set in mathematics ?",
        "options" : [ 
            "(a) A collection of ordered numbers",
            "(b) A collection of well-define distinct objects",
            "(c) A group of random variable",
            "(d) A sequence od numbers"
        ],
        "correct_answer" : 'b'
    },

    {
        "question" : "which of the following is a programming language ?",
        "options" : [ 
            "(a) HTML",
            "(b) CSS",
            "(c) Python",
            "(d) HTTPs"
        ],
        "correct_answer" : "c"
    },

    {
        "question" : "which data structure follows last-in first-out (LIFO) principle ?",
        "options" : [
            "(a) Queue",
            "(b) Tree",
            "(c) Graph",
            "(d) stack"
        ],
        "correct_answer" : "d"
    }

]


total_score = 0
for q in quiz:
    print("\n", q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").lower()
    

    choice = ['a','b','c','d']
    if user_answer not in choice:
        print("Invalid option")  
    else: 
        if user_answer == q["correct_answer"].lower():
            print("correct!!")
            total_score += 1
        else:
            print("The correct answer is :",q["correct_answer"])
        
print("you're total score is: ", total_score)

def calculate_result(score, total_questions):
    percentage = (score / total_questions) * 100
    print(f"you score :{score}/{total_questions} ")
    print(f"Your percentage is: {percentage:.2f}%")
    

    if percentage >= 50:
        print("You passed the quiz!")
    else:
        print("You failed the quiz. Try again!")

calculate_result(total_score, len(quiz))
