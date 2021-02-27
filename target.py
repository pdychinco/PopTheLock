from turtle import Turtle
from random import randint, choice
x_cor = -40
y_cor = 0
MIN_DISTANCE = 40
Y_POSITION_FLIP = -1
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

    def randomChoice(self):
        return choice([True, False])

    def random_cor(self, radius):
        global x_cor
        global y_cor
        last_x_cor = self.xcor()

        # if radius positive, cursor going left. if radius negative, cursor going right
        # current target quad 1
        if self.xcor() >= 0 and self.ycor() >= 0:
            if radius > 0:
                x_cor = randint(int(self.xcor() - 75), int(self.xcor() - MIN_DISTANCE))
                y_cor = (radius ** 2 - x_cor ** 2) ** 0.5
            elif radius < 0:
                diff = abs(80 - int(self.xcor()))
                x_cor = randint(-int(self.xcor()), int(self.xcor() - diff))
                # check if target x coordinate is behind last x coordinate
                if last_x_cor < self.xcor():
                    y_cor = Y_POSITION_FLIP * (radius ** 2 - x_cor ** 2) ** 0.5
                else:
                    if self.randomChoice():
                        y_cor = Y_POSITION_FLIP * (radius ** 2 - x_cor ** 2) ** 0.5
                    else:
                        y_cor = (radius ** 2 - x_cor ** 2) ** 0.5
        # if radius positive, cursor going left. if radius negative, cursor going right
        # current target quad 2
        elif self.xcor() < 0 and self.ycor() >= 0:
            if radius < 0:
                x_cor = randint(int(self.xcor() + MIN_DISTANCE), int(self.xcor() + 75))
                y_cor = (radius ** 2 - x_cor ** 2) ** 0.5
            elif radius > 0:
                diff = abs(-80 - int(self.xcor()))
                x_cor = randint(int(self.xcor() - diff), int(self.xcor() + 75))
                if last_x_cor < self.xcor():
                    y_cor = Y_POSITION_FLIP * (radius ** 2 - x_cor ** 2) ** 0.5
                else:
                    if self.randomChoice():
                        y_cor = Y_POSITION_FLIP * (radius ** 2 - x_cor ** 2) ** 0.5
                    else:
                        y_cor = (radius ** 2 - x_cor ** 2) ** 0.5
        # if radius positive, cursor going left. if radius negative, cursor going right
        # current target quad 3
        elif self.xcor() < 0 and self.ycor() < 0:
            if radius < 0:
                diff = abs(-80 - int(self.xcor()))
                x_cor = randint(int(self.xcor() - diff), int(self.xcor() + 75))
                if last_x_cor > self.xcor():
                    y_cor = (radius ** 2 - x_cor ** 2) ** 0.5
                else:
                    y_cor = Y_POSITION_FLIP * (radius ** 2 - x_cor ** 2) ** 0.5
        # if radius positive, cursor going left. if radius negative, cursor going right
        # current target quad 4
        elif self.xcor() > 0 and self.ycor() < 0:
            if radius < 0:
                diff = abs(80 - int(self.xcor()))
                x_cor = randint(int(self.xcor() - MIN_DISTANCE), int(self.xcor() + diff))
                if last_x_cor > self.xcor():
                    y_cor = (radius ** 2 - x_cor ** 2) ** 0.5
                else:
                    if self.randomChoice():
                        y_cor = Y_POSITION_FLIP * (radius ** 2 - x_cor ** 2) ** 0.5
                    else:
                        y_cor = (radius ** 2 - x_cor ** 2) ** 0.5
        cor = (x_cor, y_cor)
        return cor

    def first_spawn(self, radius):
        first_x_cor = randint(10,80)
        y_spawn = randint(1,2)
        if y_spawn == 1:
            y_cor = (radius ** 2 - first_x_cor ** 2) ** 0.5
        else:
            y_cor = -((radius ** 2 - first_x_cor ** 2) ** 0.5)
        self.goto(first_x_cor, y_cor)
        self.showturtle()