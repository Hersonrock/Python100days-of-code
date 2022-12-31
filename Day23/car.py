from turtle import Turtle
import random
from scoreboard import SCREEN_HEIGHT,SCREEN_WIDTH

COLORS=["yellow","red","blue","green","purple"]

class Car (Turtle):
    def __init__(self,y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.seth(180)
        self.color(random.choice(COLORS))
        self.penup()
        self.hideturtle()
        self.goto(SCREEN_WIDTH/2+40,y_pos)
        self.showturtle()

    def rand_color(self):
        random_index=random.randint(0,4)
        color=COLORS[random_index]
        self.color(color)

    def move(self,speed):
        self.forward(speed)

    def end_check(self):
        random_x=random.randint(20,80)
        return self.xcor()<-SCREEN_WIDTH/2-random_x

    def reset(self,y_position):
        self.hideturtle()
        self.goto(SCREEN_WIDTH/2+40,y_position)
        self.showturtle()
    