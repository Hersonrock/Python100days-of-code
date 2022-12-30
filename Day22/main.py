from turtle import Screen,Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard,SCREEN_HEIGHT,SCREEN_WIDTH
import time

LOCATION_P1=(20-SCREEN_WIDTH/2,0)
LOCATION_P2=(-27+SCREEN_WIDTH/2,0)
SCOREBOARD_POS_P1=(-40,SCREEN_HEIGHT/2-80)
SCOREBOARD_POS_P2=(40,SCREEN_HEIGHT/2-80)


screen=Screen()
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
game_on=True

def create_divider():
    divider=Turtle()
    divider.color("white")
    divider.hideturtle()
    divider.penup()
    divider.goto((0,SCREEN_HEIGHT/2))
    divider.pendown()
    divider.goto((0,-SCREEN_HEIGHT/2))

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
scoreboard1=Scoreboard(SCOREBOARD_POS_P1)
scoreboard2=Scoreboard(SCOREBOARD_POS_P2)

create_divider()

#----------Screen Input handling--------
screen.listen()
screen.onkey(paddle1.move_up,"w")
screen.onkey(paddle1.move_down,"s") 
screen.onkey(paddle2.move_up,"Up")
screen.onkey(paddle2.move_down,"Down")  

#I don't yet understand how this can be called while game is running on game loop. 
#The logic of Screen.listen seems to be running in parallel?
#In hindsight it makes more sense that Screen is always running and everything else is running as a child of it, but at the same time??
#/--------------------------------------


while game_on:
    ball.move(frame_speed)
    ball.collision()
    screen.update()

    time.sleep(wait)
    


screen.exitonclick()