from turtle import Turtle
from random import randint
x_cor = 1
class Target(Turtle):
    def __init__(self, radius):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.hideturtle()
        self.spawn(radius)

    def spawn(self, radius):
        self.goto(self.random_cor(radius))
        self.showturtle()

    def random_cor(self, radius):
        global x_cor
        if self.xcor() >= 0:
            x_cor = randint(-80, int(self.xcor() - 5))
        elif self.xcor() < 0:
            x_cor = randint(int(self.xcor() + 5), 80)
        y_cor = (radius**2 - x_cor**2)**0.5
        cor = (x_cor, y_cor)
        return cor

