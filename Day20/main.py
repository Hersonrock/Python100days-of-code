from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_HEIGHT=600
SCREEN_WIDTH=600

screen=Screen()
screen.setup(width=SCREEN_WIDTH+20,height=SCREEN_HEIGHT+20)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)  #Is necesary for animation control.
game_on=True




snek=Snake()
food=Food()
scoreboard=Scoreboard()

def collision_check(food):

    if snek.head.distance(food)<15:
        print("contact")
        food.randomize_position()
        scoreboard.increase_score()

def boundary_check():
    if (snek.head.position()[0]>(SCREEN_WIDTH/2)-20) or (snek.head.position()[0]<-(SCREEN_WIDTH/2)+13) or (snek.head.position()[1]>(SCREEN_HEIGHT/2)-13) or (snek.head.position()[1]<-(SCREEN_HEIGHT/2)+20) :
        return False
    return True

def  draw_boundary():
    boundary=Turtle()
    boundary.hideturtle()
    boundary.penup()
    boundary.color("white")
    boundary.goto((-(SCREEN_WIDTH/2)+9,(SCREEN_HEIGHT/2)-9))
    boundary.pendown()
    boundary.goto(((SCREEN_WIDTH/2)-10,(SCREEN_HEIGHT/2)-9))
    boundary.goto(((SCREEN_WIDTH/2)-10,-(SCREEN_HEIGHT/2)+10))
    boundary.goto((-(SCREEN_WIDTH/2)+9,-(SCREEN_HEIGHT/2)+10))
    boundary.goto((-(SCREEN_WIDTH/2)+9,(SCREEN_HEIGHT/2)-9))
    screen.update()

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

draw_boundary()

while game_on:

    screen.update()  #Update goes along with tracer for animation control. Especifies the time the screen is updated.
    time.sleep(0.1) 
    snek.move() 
    collision_check(food)
    game_on = boundary_check()

scoreboard.game_over()
for segment in snek.segments:
    segment.hideturtle()
food.hideturtle()
screen.update()

screen.exitonclick()