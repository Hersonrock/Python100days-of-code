from turtle import Turtle
ALIGNMENT= "center"
FONT= ('Courier',24)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.goto(0,250)
        self.color("white")
        self.update_scoreboard()
        self.penup()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()