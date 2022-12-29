from turtle import Screen
from ball import Ball

SCREEN_HEIGHT=600
SCREEN_WIDTH=600

screen=Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
# screen.tracer(0)  #Is necesary for animation control.
game_on=True


ball=Ball()

while game_on:
    ball.move()
    ball.collision()

screen.exitonclick()