from turtle import Turtle
import random


class Food():
    def __init__(self):
        self.position= (0,0)
        self.create_food()
    
    def create_food(self):
        food = Turtle(shape="circle")
        food.color("blue")
        food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        food.speed("fastest")
        food.hideturtle()
        food.penup()
        food.goto(self.position)
        food.showturtle()
        self.entity=food

    def randomize_position(self):
        self.position= (random.randint(-290,290),random.randint(-290,290))
        self.entity.hideturtle()
        self.entity.goto(self.position)
        self.entity.showturtle()