from turtle import Turtle
class Lock(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.shapesize(stretch_len=8, stretch_wid=8, outline=20)
        self.color("white", "black")