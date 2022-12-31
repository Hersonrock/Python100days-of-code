from turtle import Turtle


SCREEN_HEIGHT=600
SCREEN_WIDTH=600
START=(0,-SCREEN_HEIGHT/2+20)


ALIGNMENT= "center"
FONT= ('Courier',20)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.hideturtle()
        self.goto(-SCREEN_WIDTH/2+80,SCREEN_HEIGHT/2-40)
        self.color("black")
        self.update_scoreboard()
        self.penup()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}",align=ALIGNMENT,font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align=ALIGNMENT,font=FONT)