from turtle import Turtle
from random import randint
x_cor = -40
MIN_DISTANCE = 40
class Target(Turtle):
    def __init__(self, radius):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.hideturtle()
        self.first_spawn(radius)

    def spawn(self, radius):
        self.goto(self.random_cor(radius))
        self.showturtle()

    def random_cor(self, radius):
        global x_cor
        if radius > 0 and self.xcor() >= -4:
            x_cor = randint(int(self.xcor() - 75), int(self.xcor() - MIN_DISTANCE))
        elif radius > 0 and self.xcor() <= -4:
            diff = abs(-80 - int(self.xcor()))
            x_cor = randint(int(self.xcor() - diff), int(self.xcor() - MIN_DISTANCE))
        elif radius < 0 and self.xcor() <= 4:
            x_cor = randint(int(self.xcor() + MIN_DISTANCE), int(self.xcor() + 75))
        elif radius < 0 and self.xcor() >= 4:
            diff = abs(80 - int(self.xcor()))
            x_cor = randint(int(self.xcor() + MIN_DISTANCE), int(self.xcor() + diff))
        y_cor = (radius**2 - x_cor**2)**0.5
        cor = (x_cor, y_cor)
        return cor

    def first_spawn(self, radius):
        first_x_cor = randint(2,80)
        y_spawn = randint(1,2)
        if y_spawn == 1:
            y_cor = (radius ** 2 - first_x_cor ** 2) ** 0.5
        else:
            y_cor = -((radius ** 2 - first_x_cor ** 2) ** 0.5)
        self.goto(first_x_cor, y_cor)
        self.showturtle()