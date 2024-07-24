# Create a Spot Painting
# using colormode and turtle modules and their classes and attributes

# Part 1 - use colorgram module to get colors from an image
# colorgram.extract('image.jpg', n) takes an image and returns n # of colors in that image. .rgb returns a tuple
# colorgram manual: https://pypi.org/project/colorgram.py/
# RGB colors: https://www.w3schools.com/colors/colors_rgb.asp

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     # rgb_colors.append(color.rgb)  # doesn't yield a usable list
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# Test colors to remove unwanted background colors
# (245, 243, 238) and (246, 242, 244) are background colors, so delete
# [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136),
#  (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
#  (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
#  (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
#  (176, 192, 208), (168, 99, 102)]

# color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
#               (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
#               (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
#               (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
#               (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# The following didn't work for Part 1, but wasn't needed b/c the module itself had code to extract r, g, b values
# [i.replace("Rgb","") for i in color]
# [i.removeprefix("Rgb") for i in color]
# Part 2 - use turtle module to draw a spot painting

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fastest")
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
              (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
              (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
              (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)  # 10 dots * 50 paces = 500
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
