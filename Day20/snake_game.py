from turtle import Turtle,Screen
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

segments=[]
game_on=True
last_loc=(0,0)
# screen.listen()
starting_positions=[(0,0),(-20,0),(-40,0)]

def move_forwards(head):
    head.forward(20)

#Code that cannot be used-------
def turn_right(head):
    print("right")
    new_heading=head.heading()+90
    head.seth(new_heading)
    
def turn_left(head):
    print("left")
    new_heading=head.heading()-90
    head.seth(new_heading)
#Code that cannot be used-------



def move(segments):
    
    last_loc=segments[0].position()
    for i in range(1,len(segments)):
        new_loc=last_loc
        last_loc=segments[i].position()
        segments[i].goto(new_loc)
    screen.update()
    time.sleep(0.1)


for position in starting_positions:

    snake_segment=Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(position)
    segments.append(snake_segment) #A way to track segments and to keep them organized.

while game_on:
   
    # screen.onkey(turn_left(segments[0]),"Left")
    # screen.onkey(turn_right(segments[0]),"Right")

    segments[0].forward(20) #This will just move the snake forward.
    move(segments)



screen.exitonclick()