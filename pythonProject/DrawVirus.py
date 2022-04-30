from time import sleep
from turtle import *

color('green')
bgcolor('black')
speed(11)
hideturtle()
b = 0
goto(0, 150)
while b < 200:
    right(b)
    forward(b * 3)
    b += 1

sleep(5)
