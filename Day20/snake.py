from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP= 90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        
        self.head=self.segments[0]  #sets snake head for convenience.

    def create_snake(self):

        for position in STARTING_POSITIONS:

            #Initializes all segments and keeps turtle hidden.
            segment=Turtle(shape="square")
            segment.color("white")
            segment.hideturtle()
            segment.penup()
            segment.goto(position)
            segment.showturtle()

            self.segments.append(segment) #A way to track segments and to keep them organized.
        

#------------Segment Follow-----------------------
# Moves head forward, and pulls all remaining segments to the position of the one ahead of it.
    def move(self):
        last_loc=self.head.position()
        self.move_forwards()

        for i in range(1,len(self.segments)):
            new_loc=last_loc
            last_loc=self.segments[i].position()
            self.segments[i].goto(new_loc)
#/-------------------------------------------------      

#---------------Movement control-------------------
    def move_forwards(self):
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading()!=180:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading()!=0:
            self.head.seth(LEFT)
            
    def up(self):
        if self.head.heading()!=270: 
            self.head.seth(UP)
            
    def down(self):
        if self.head.heading()!=90:
            self.head.seth(DOWN)
#/-------------------------------------------------     