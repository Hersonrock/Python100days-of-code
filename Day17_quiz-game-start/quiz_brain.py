class QuizBrain:

    question_list = []
    question_number=0
    score=0
    def __init__(self,questions):
        QuizBrain.question_list=questions
    def next_question(self):

        current_question = QuizBrain.question_list[QuizBrain.question_number]
        QuizBrain.question_number += 1
        user_answer= input(f"Q.{QuizBrain.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer)

    def still_has_question(self):

        return QuizBrain.question_number<len(QuizBrain.question_list)

    def check_answer(self,answer):
        if QuizBrain.question_list[QuizBrain.question_number-1].answer.lower() == answer:
            print ("You got it right!")
            QuizBrain.score +=1
        else:
            print ("That's wrong!")
        print(f"The correct answer is {QuizBrain.question_list[QuizBrain.question_number-1].answer} ")
        print(f"Score: {QuizBrain.score}/{QuizBrain.question_number} \n")