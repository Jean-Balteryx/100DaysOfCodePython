# Imports the Turtle and Screen classes from the turtle module
from turtle import Turtle, Screen

# Imports the random module
import random

# Initializes the variable that will allow to start/stop the race
is_race_on = False

# Creates a new Screen object
screen = Screen()

# Sets the size of the screen
screen.setup(width=500, height=400)

# Creates a user input for him to place his bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color :")

# Stores turtles colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Stores turtles starting positions
y_position = [-100, -60, -20, 20, 60, 100]

# Initializes a List that will contain the turtles
all_turtles = []

# Creates 6 turtles
for turtle_index in range(6):
    # Creates a new Turtle object with the shape of a turtle
    new_turtle = Turtle("turtle")

    # Lifts up the pen for the turtle so it doesn't leave a trail
    new_turtle.penup()

    # Assign a color to the turtle
    new_turtle.color(colors[turtle_index])

    # Sets the starting position of the turtle
    new_turtle.goto(x=-230, y=y_position[turtle_index])

    # Adds the turtle to the List of turtles
    all_turtles.append(new_turtle)

# When the user places is bet, the race can begin
if user_bet:
    is_race_on = True

# THe race goes on while no turtle has finished
while is_race_on:
    # Goes through all the turtles
    for turtle in all_turtles:
        # Tests whether the turtle has finished
        if turtle.xcor() > 230:
            # The turtle has finished

            # The race is off
            is_race_on = False

            # Retrieves the color of the winning turtle
            winning_color = turtle.pencolor()

            # Compares the color of the winning turtle and the color bet by the user
            if winning_color == user_bet:
                # The user picked the winner turtle
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                # The user picked one of the loser turtle
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Makes the turtle go forward by a random distance between 1 and 10 paces
        turtle.forward(random.randint(0, 10))

# Sets the screen to exit when the user click
screen.exitonclick()
