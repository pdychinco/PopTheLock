from turtle import Screen
from target import Target
from cursor import Cursor
from lock import Lock
import time
from random import randint

game_speed = 0.1

screen = Screen()
screen.title("Pop the Lock")
screen.setup(width=500, height=500)
screen.tracer(0)
screen.bgcolor("black")

def key_pressed():
    cursor.flip(cursor.INCREASE_SPEED)
    target.spawn(cursor.radius)

lock = Lock()
cursor = Cursor()
target = Target(cursor.radius)
screen.onkey(key_pressed,"space")
screen.listen()


game_is_on = True

while game_is_on:
    time.sleep(game_speed)
    screen.update()
    cursor.circle(radius=cursor.radius, extent=1)

screen.exitonclick()