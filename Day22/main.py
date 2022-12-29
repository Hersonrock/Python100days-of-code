from turtle import Screen
from ball import Ball
import time

SCREEN_HEIGHT=600
SCREEN_WIDTH=600



screen=Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
# screen.tracer(0)  #Is necesary for animation control.
game_on=True
fps=55
speed=500
wait=(1/fps)
frame_speed=speed/fps

ball=Ball()

while game_on:
    ball.move(frame_speed)
    ball.collision()
    screen.update()
    time.sleep(wait)
    


screen.exitonclick()