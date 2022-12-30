from turtle import Turtle
import random
from scoreboard import SCREEN_HEIGHT,SCREEN_WIDTH

COLORS=["yellow","red","blue","green","purple"]


relative_speed=70
global_speed=SCREEN_WIDTH/relative_speed


class Car (Turtle):
    def __init__(self,y_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.seth(180)
        self.rand_color()
        self.penup()
        self.hideturtle()
        self.goto(SCREEN_WIDTH/2+40,y_pos)
        self.showturtle()
        self.speed=0

    def rand_color(self):
        random_index=random.randint(0,4)
        color=COLORS[random_index]
        self.color(color)


    def move(self):
        self.forward(self.speed)

    def end_check(self):
        random_x=random.randint(20,80)
        return self.xcor()<-SCREEN_WIDTH/2-random_x

    def reset(self,y_position):
        self.hideturtle()
        self.goto(SCREEN_WIDTH/2+40,y_position)
        self.showturtle()
    
    def change_speed(self,magnitude):
        self.speed=magnitude