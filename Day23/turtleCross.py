from turtle import Turtle
from scoreboard import START
from cars import Cars

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

    def reset(self):
        self.hideturtle()
        self.goto(START)
        self.showturtle()

    def collision(self,cars):
        collided=False
        for car in cars.traffic:
            if (self.distance(car)<20) and (self.ycor()+10>car.ycor()-10):
                collided=True
            print(f"distance: {(self.distance(car)<40)}")
            print(f"line: {(self.ycor()+10>car.ycor()-10)}")
        return collided
