import turtle
import random

homework = turtle.Turtle()
da_colors = ["pink", "orange", "yellow", "light green", "light blue", "lavender"]

def h(length):
    for i in range(8):
        homework.color(random.choice(da_colors))
        homework.forward(length)
        homework.left(45)

h(100)

turtleREAL = turtle.Turtle()
pattern = 1

for i in range(500):
    for color in da_colors:
        turtleREAL.speed(0)
        turtleREAL.color(color)
        turtleREAL.forward(pattern)
        turtleREAL.right(90)
        turtleREAL.right(1)
        pattern += 1

print ("The end of homework 13! :)")








