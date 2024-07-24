# Turtle Race Project
# Day 19 learn State and Multiple Instances and Event Listeners
# learn how to create multiple states and instances

from turtle import Turtle, Screen
import random, turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your better.", prompt="Which turtle will will the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
racers = []

# create 'n' number of turtles
number_of_racers = 6
for i in range(0, number_of_racers):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_position[i])
    racers.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Each racer moves forward a random amount
        random_distance = random.randint(0, 10)
        racer.forward(random_distance)

screen.exitonclick()
