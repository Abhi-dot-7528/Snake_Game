from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SNAKE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # Setup Snake
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for coordinates in STARTING_POSITIONS:
            self.add_snake(coordinates)

    def add_snake(self, position):
        new_sq = Turtle()
        new_sq.color("white")
        new_sq.shape("square")
        new_sq.penup()
        new_sq.goto(position)
        self.segments.append(new_sq)

    def extend_snake(self):
        self.add_snake(self.segments[-1].position())

    def move(self):
        for num_of_seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num_of_seg - 1].xcor()
            new_y = self.segments[num_of_seg - 1].ycor()
            self.segments[num_of_seg].goto(new_x, new_y)
        self.snake_head.forward(MOVE_SNAKE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
