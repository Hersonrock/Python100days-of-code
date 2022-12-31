from turtle import Turtle
from scoreboard import SCREEN_HEIGHT,SCREEN_WIDTH,START

SPEED=10


class TurtleCross(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(START)
        self.showturtle()
        self.seth(90)

    def move(self):
        self.forward(SPEED)