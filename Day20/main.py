from turtle import Turtle,Screen
import time
from snake import Snake

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)
game_on=True


screen.listen()
      
Snek=Snake()

while game_on:

    screen.onkey(Snek.left,"Left")
    screen.onkey(Snek.right,"Right")
    screen.onkey(Snek.up,"Up")
    screen.onkey(Snek.down,"Down")

    Snek.move() 
    screen.update()
    time.sleep(0.1) 


screen.exitonclick()