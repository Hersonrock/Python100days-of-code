
from scoreboard import Scoreboard,SCREEN_HEIGHT,SCREEN_WIDTH
from turtleCross import TurtleCross
from turtle import Screen,Turtle
from cars import Cars
import random
import time


def street_create():
    painter=Turtle()
    painter.hideturtle()
    painter.penup()
    painter.goto(-SCREEN_WIDTH/2,SCREEN_HEIGHT/2-100)
    painter.pendown()
    painter.forward(SCREEN_WIDTH)
    painter.penup()
    painter.goto(-SCREEN_WIDTH/2,-SCREEN_HEIGHT/2+100)
    painter.pendown()
    painter.forward(SCREEN_WIDTH)



game_on=True
counter=1

screen=Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Turtle Cross")
screen.tracer(0)

# def rand_y():
#     y_position=random.randint(-SCREEN_HEIGHT/2+110,SCREEN_HEIGHT/2-110)

#     return y_position

turtle=TurtleCross()
scoreboard=Scoreboard()
cars=Cars()

for i in range(1,21):
    cars.create_traffic()

screen.listen()
screen.onkey(turtle.move,"w")
street_create()


while game_on:
    
    screen.update()
    cars.move()
    time.sleep(0.1)
    if counter<100:
        counter +=1
    else:
        counter=1

    if counter%20==0:
        cars.move_cars()
   