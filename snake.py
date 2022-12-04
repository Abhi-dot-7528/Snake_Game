from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SNAKE = 20


class Snake:
    def __init__(self):
        # Setup Snake
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for coordinates in STARTING_POSITIONS:
            new_sq = Turtle()
            new_sq.color("white")
            new_sq.shape("square")
            new_sq.penup()
            new_sq.goto(coordinates)
            self.segments.append(new_sq)

    def move(self):
        for num_of_seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num_of_seg - 1].xcor()
            new_y = self.segments[num_of_seg - 1].ycor()
            self.segments[num_of_seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_SNAKE)
