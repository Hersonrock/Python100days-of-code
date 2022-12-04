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
import os
#HINT: Clearing the Screen
#   os.system('cls')

game_started=True

while game_started:
    os.system('cls')
    ammount=input("Type ammount of questions: ")
    difficulty=input("Select Difficulty (easy/medium/hard): ").lower()
    quiz_list_url = f"https://opentdb.com/api.php?amount={ammount}&category=15&difficulty={difficulty}&type=boolean"
    quiz_list = requests.get(url=quiz_list_url).json()
    question_bank=[]

    for question in quiz_list["results"]:
        question["question"]=question["question"].replace("&quot;",'"')
        question["question"]=question["question"].replace("&#039;","'")
        question_bank.append(Question(question["question"],question["correct_answer"]))

    print(question_bank[0].text)
    quiz=QuizBrain(question_bank)

    while quiz.still_has_question():
        quiz.next_question()

    print (f"You completed the quiz \nYour final score was {QuizBrain.score}/{len(QuizBrain.question_list)}\n")
    continue_game=input("Do you want to continue playing (y/n): ").lower()
    if continue_game!="y":
        game_started=False

os.system('cls')
print("Thanks for playing!")