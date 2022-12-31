
from scoreboard import Scoreboard,SCREEN_HEIGHT,SCREEN_WIDTH
from turtleCross import TurtleCross
from turtle import Screen,Turtle
from cars import Cars
import random
import time

CAR_AMMOUNT=20
LEVEL_FACTOR=0.2
relative_speed=70
global_speed=SCREEN_WIDTH/relative_speed

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
game_init=True
level=0

screen=Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("white")
screen.title("Turtle Cross")
screen.tracer(0)

turtle=TurtleCross()
scoreboard=Scoreboard()
cars=Cars()

cars.create_traffic(CAR_AMMOUNT)
screen.listen()
screen.onkey(turtle.move,"w")
street_create()

while game_on:
    
    if game_init: 
        cars.move_init()
        game_init=False
    else: 
        if turtle.ycor()>SCREEN_HEIGHT/2-100:
            turtle.reset()
            scoreboard.increase_level()
            level+=1
            
            
        cars.move(global_speed+LEVEL_FACTOR*global_speed*level)
        cars.reset_car()
        time.sleep(0.1)
        screen.update()
    