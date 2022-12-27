from turtle import Turtle,Screen
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)
game_on=True
last_loc=(0,0)
screen.listen()
starting_positions=[(0,0),(-20,0),(-40,0)]

class Snake:

    segments=[]


    def __init__(self,positions:list):

        for position in positions:

            snake_segment=Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.hideturtle()
            self.segments.append(snake_segment) #A way to track segments and to keep them organized.
            snake_segment.penup()
            snake_segment.goto(position)
            snake_segment.showturtle()
        self.head=self.segments[0]

    def move(self):
        last_loc=self.head.position()
        self.move_forwards()
        for i in range(1,len(self.segments)):
            new_loc=last_loc
            last_loc=self.segments[i].position()
            self.segments[i].goto(new_loc)
        screen.update()
        time.sleep(0.1) 
        

    def move_forwards(self):
        self.head.forward(20)

   
    def right(self):
        if self.head.heading()!=180:
            new_heading=0
            self.head.seth(new_heading)
    def left(self):
        if self.head.heading()!=0:
            new_heading=180
            self.head.seth(new_heading)
            
    def up(self):
        if self.head.heading()!=270: 
            new_heading=90
            self.head.seth(new_heading)
            
    def down(self):
        if self.head.heading()!=90:
            new_heading=270
            self.head.seth(new_heading)
            
       
Snek=Snake(starting_positions)

while game_on:

    screen.onkey(Snek.left,"Left")
    screen.onkey(Snek.right,"Right")
    screen.onkey(Snek.up,"Up")
    screen.onkey(Snek.down,"Down")

    Snek.move() 


screen.exitonclick()