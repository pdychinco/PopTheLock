from turtle import Turtle

radius = 79
START_POSITION = (0, 80)

class Cursor(Turtle):
    def __init__(self):
        super().__init__()
        self.FLIP_HEADING = 180
        self.FLIP_DIRECTION = -1
        self.INCREASE_SPEED = 0.9
        self.radius = -79
        self.shape("square")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=1)
        self.goto(START_POSITION)
        # self.setheading(self.FLIP_HEADING)

    def flip_direction(self):
        self.setheading(self.heading() + self.FLIP_HEADING)
        self.radius *= self.FLIP_DIRECTION