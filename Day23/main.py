
from scoreboard import Scoreboard,SCREEN_HEIGHT,SCREEN_WIDTH
from turtleCross import TurtleCross
from turtle import Screen
import time

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


while game_on:
    
    screen.update()
    time.sleep(0.1)