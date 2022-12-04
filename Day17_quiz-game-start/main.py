from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
i = 0

for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))

quiz=QuizBrain(question_bank)

quiz.next_question()
