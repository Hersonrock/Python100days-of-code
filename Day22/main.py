from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import SCREEN_HEIGHT,SCREEN_WIDTH
import time

LOCATION_P1=(20-SCREEN_WIDTH/2,0)
LOCATION_P2=(-27+SCREEN_WIDTH/2,0)




screen=Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
# screen.tracer(0)  #Is necesary for animation control.
game_on=True

#-------Animation stuff---------
#Had to play with the numbers to make it look "pretty"
fps=55
speed=500
wait=(1/fps)
frame_speed=speed/fps
#/------------------------------

ball=Ball()
paddle1=Paddle(LOCATION_P1,3)
paddle2=Paddle(LOCATION_P2,7)

while game_on:
    ball.move(frame_speed)
    ball.collision()
    screen.update()

    time.sleep(wait)
    


screen.exitonclick()