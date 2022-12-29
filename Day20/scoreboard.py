from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.goto(0,250)
        self.color("white")
        self.write(f"Score: {self.score}",align="center",font=('Arial',24))
        self.penup()
        
        

    def increase_score(self):
        self.score +=1
        self.write(f"Score: {self.score}",align="center",font=('Arial',24))