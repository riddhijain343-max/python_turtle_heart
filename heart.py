<<<<<<< HEAD
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

=======
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

>>>>>>> 0e4bb51532c4b90a6642b869ce4b0b569bf86898
turtle.done()