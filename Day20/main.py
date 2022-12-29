from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)  #Is necesary for animation control.
game_on=True

snek=Snake()
food=Food()

#----------Screen Input handling--------
screen.listen()
screen.onkey(snek.left,"Left")
screen.onkey(snek.right,"Right")
screen.onkey(snek.up,"Up")
screen.onkey(snek.down,"Down")     
#I don't yet understand how this can be called while game is running on game loop. 
#The logic of Screen.listen seems to be running in parallel?
#In hindsight it makes more sense that Screen is always running and everything else is running as a child of it, but at the same time??
#/--------------------------------------


while game_on:

    screen.update()  #Update goes along with tracer for animation control. Especifies the time the screen is updated.
    time.sleep(0.1) 
    snek.move() 

screen.exitonclick()