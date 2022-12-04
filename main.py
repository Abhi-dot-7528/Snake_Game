from turtle import Turtle, Screen

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Serpente")

# Setup Snake
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for coordinates in starting_positions:
    new_sq = Turtle()
    new_sq.color("white")
    new_sq.shape("square")
    new_sq.goto(coordinates)

screen.exitonclick()
