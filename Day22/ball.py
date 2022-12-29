from turtle import Turtle
# from main import SCREEN_HEIGHT,SCREEN_WIDTH

SCREEN_HEIGHT=600
SCREEN_WIDTH=600

SPEED=20
UP= 90
DOWN=270
LEFT=180
RIGHT=0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.setheading(RIGHT)
        
    def move(self):
        self.forward(SPEED)

    def collision(self):

        if self.position()[0]>(SCREEN_WIDTH/2)-10:
            self.setheading(LEFT)
            self.color("red")
        if self.position()[0]<-(SCREEN_WIDTH/2)+10:
            self.setheading(RIGHT)
            self.color("blue")


    
