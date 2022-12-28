from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]

class Snake:

    
    def __init__(self):
        self.segments=[]
        self.create_snake()


    def create_snake(self):

        for position in STARTING_POSITIONS:
            
            segment=Turtle(shape="square")
            segment.color("white")
            segment.hideturtle()
            segment.penup()
            segment.goto(position)
            segment.showturtle()
            self.segments.append(segment) #A way to track segments and to keep them organized.
        self.head=self.segments[0]

    def move(self):
        last_loc=self.head.position()
        self.move_forwards()
        for i in range(1,len(self.segments)):
            new_loc=last_loc
            last_loc=self.segments[i].position()
            self.segments[i].goto(new_loc)
        
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
        