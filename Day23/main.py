
from scoreboard import Scoreboard,SCREEN_HEIGHT,SCREEN_WIDTH
from turtleCross import TurtleCross
from turtle import Screen,Turtle
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

screen=Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Turtle Cross")
screen.tracer(0)
turtle=TurtleCross()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(turtle.move,"w")
street_create()

while game_on:
    
    screen.update()
    time.sleep(0.1)