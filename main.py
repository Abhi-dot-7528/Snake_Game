from turtle import Turtle, Screen
import time

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Serpente")
screen.tracer(0)

# Setup Snake
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for coordinates in starting_positions:
    new_sq = Turtle()
    new_sq.color("white")
    new_sq.shape("square")
    new_sq.penup()
    new_sq.goto(coordinates)
    segments.append(new_sq)

# Animate snake movements
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for num_of_seg in range(len(segments) - 1, 0, -1):
        new_x = segments[num_of_seg-1].xcor()
        new_y = segments[num_of_seg-1].ycor()
        segments[num_of_seg].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
