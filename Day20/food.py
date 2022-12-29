from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()
    
    def create_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

    def randomize_position(self):
        self.randposition= (random.randrange(-290,290,10),random.randrange(-290,290,10))
        self.hideturtle()
        self.goto(self.randposition)
        self.showturtle()