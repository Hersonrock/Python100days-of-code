from turtle import Turtle


SCREEN_HEIGHT=600
SCREEN_WIDTH=600


ALIGNMENT= "center"
FONT= ('Courier',40)

class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.update_scoreboard()
        self.penup()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self,score):
        self.score = score
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align=ALIGNMENT,font=FONT)

