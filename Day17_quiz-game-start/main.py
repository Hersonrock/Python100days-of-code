#Using quiz API from
#   https://opentdb.com/api_config.php
# 
#Using "requests" , installed with command "pip install requests"
#   see: https://www.geeksforgeeks.org/get-post-requests-using-python/

import requests
import json # used for manipulating JSON data

from data import question_data  # This is not really needed 
from question_model import Question
from quiz_brain import QuizBrain

ammount=10
quiz_list_url = f"https://opentdb.com/api.php?amount={ammount}&category=15&difficulty=hard&type=boolean"
quiz_list = requests.get(url=quiz_list_url).json()

question_bank=[]
i = 0

for question in quiz_list["results"]:
    question["question"]=question["question"].replace("&quot;",'"')
    question["question"]=question["question"].replace("&#039;","'")
    question_bank.append(Question(question["question"],question["correct_answer"]))

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print (f"You completed the quiz \nYour final score was {QuizBrain.score}/{len(QuizBrain.question_list)}")