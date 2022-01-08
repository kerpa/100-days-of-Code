from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quizz = QuizzBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print("You've completed the quizz")
print(f"You're final score is: {quizz.score}/{quizz.question_number}")
