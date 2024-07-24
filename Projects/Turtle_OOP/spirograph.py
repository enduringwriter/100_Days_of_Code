# Spirograph
# Challenge 5 - draw a Spirograph using turtle module

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
t.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


# # This works, but it draws circles over circles, and
# # you don't know how many circles are needed to complete the spirograph
# for _ in range(100):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading() + 10)


draw_spirograph(5)  # 360 draws one circle

screen = t.Screen()
screen.exitonclick()
