from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

Quiz = QuizBrain(question_bank)

while Quiz.still_have_questions():
    Quiz.next_question()

print("The Quiz is finished!")
print(f"Your score is {Quiz.score}/{Quiz.question_number}!")