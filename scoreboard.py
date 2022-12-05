from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(280, 270)
        self.hideturtle()
        self.show_score()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", move=False, align='right', font=('Fira Code', 14, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER.\nYour Score: {self.score}", move=False, align='center', font=('Fira Code', 14, 'bold'))
