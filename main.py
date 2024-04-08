import random
import turtle
from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -100, -50, 0, 50, 100]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_positions[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Congrats! You are the winner! {winner}! ")
            else:
                print(f"You lost! The winner was {winner}")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()