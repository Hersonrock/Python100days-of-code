class QuizBrain:

    question_list = []
    question_number=0
    def __init__(self,questions):
        QuizBrain.question_list=questions
    def next_question(self):

        current_question = QuizBrain.question_list[QuizBrain.question_number]
        QuizBrain.question_number += 1
        input(f"Q.{QuizBrain.question_number}: {current_question.text} (True/False)")
        