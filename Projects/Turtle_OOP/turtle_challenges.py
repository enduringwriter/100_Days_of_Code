# Challenges 1, 2, 3, 4, and 4.5
# Day 18 of 100 Days of Code, using replit.com

# turtle is the module. Turtle and Screen are classes
import turtle as t
# from turtle import Turtle, Screen
import random

tim = t.Turtle()
# tim = Turtle()
# jane = Turtle()
# terry = Turtle()


# Challenge 4.5 - Draw using random RGB colors applied to Project 4
t.colormode(255)  # colormode is applied to turtle module not the object


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_rand_color = (r, g, b)
    return rgb_rand_color


# # colors are use for Challenges 3 and 4
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
#           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# # Challenge 4 - Random Walk
directions = [0, 90, 180, 270]
tim.pensize(12)
tim.speed("normal")

for _ in range(200):
    tim.forward(30)
    tim.color(random_color())
    # tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))

# # Challenge 3 - Draw multiple shapes polygons with different colors

# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)

# for multiple_shapes in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(multiple_shapes)


# # Challenge 2 - Draw a dashed line, add click to exit screen
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# # Challenge 1 - Draw polygon with 4 sides, add click to exit screen
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# screen = t.Screen()
# screen.exitonclick()
