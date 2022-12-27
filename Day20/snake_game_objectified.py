from turtle import Turtle,Screen
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snek")
# screen.tracer(0)

game_on=True
last_loc=(0,0)
# screen.listen()
starting_positions=[(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self,positions:list):

        for position in positions:

            snake_segment=Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.hideturtle()
            self.segments.append(snake_segment) #A way to track segments and to keep them organized.
            snake_segment.penup()
            snake_segment.goto(position)
            snake_segment.showturtle()

    segments=[]

    def move(segments):
        last_loc=segments[0].position()
        for i in range(1,len(segments)):
            new_loc=last_loc
            last_loc=segments[i].position()
            segments[i].goto(new_loc)
        screen.update()
        time.sleep(0.1)    


Snek=Snake(starting_positions)

print(f"{Snek.segments}")

while game_on:

    Snek.segments[0].forward(2)
    # Snek.move() 
    # TypeError: 'Snake' object is not subscriptable

screen.exitonclick()