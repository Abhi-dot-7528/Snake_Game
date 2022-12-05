from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.new_loc()

    # Relocate food after snake collide with it.
    def new_loc(self):
        x_cord = randint(-280, 280)
        y_cord = randint(-280, 280)
        self.goto(x_cord, y_cord)
