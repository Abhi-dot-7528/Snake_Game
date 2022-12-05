import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Serpente")
screen.tracer(0)

# Create snake
snake = Snake()

# Create food
food = Food()

# Show score
score = Scoreboard()

# Control snake movements
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Animate snake movements
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting snake collision with food
    if snake.snake_head.distance(food) < 13:
        food.new_loc()
        score.increment_score()

    # Game Over
    if snake.snake_head.xcor() > 280 or \
            snake.snake_head.xcor() < -280 or \
            snake.snake_head.ycor() > 280 or \
            snake.snake_head.ycor() < -280:
        score.game_over()
        game_is_on = False

screen.exitonclick()
