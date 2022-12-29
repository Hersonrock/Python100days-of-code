from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.goto(-40,250)
        self.color("white")
        self.write(f"Score: {self.score}",font=('Arial',12))
        self.penup()
        
        

    def increase_score(self):
        self.score +=1
        self.write(f"Score: {self.score}",font=('Arial',12))