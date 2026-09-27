import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pensize(1)

colors = ["red", "blue", "lime", "yellow", "cyan", "magenta", "orange"]

for i in range(120):
    angle = (math.pi * 2 * i) / 120

    x = 16 * math.sin(angle) ** 3
    y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)

    # Scale the heart
    x *= 15
    y *= 15

    t.penup()
    t.goto(0, 0)

    t.pendown()
    t.color(random.choice(colors))
    t.goto(x, y)

turtle.done()