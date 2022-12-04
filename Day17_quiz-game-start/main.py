from data import question_data
from question_model import Question


question_bank=[]
i = 0

for question in question_data:
    question_bank.append(Question(question["text"],question["answer"]))
    
print(question_bank)