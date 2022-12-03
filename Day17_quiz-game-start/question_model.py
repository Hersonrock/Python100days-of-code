class  Question:
    all = []
    def __init__(self,text=str,answer=bool):
        self.text=text
        self.answer=answer
        Question.all.append(self)
    def __repr__(self):
        return f"Question('{self.text}',{self.answer})"

question1=Question("A slug's blood is green.",True)

print(Question.all)