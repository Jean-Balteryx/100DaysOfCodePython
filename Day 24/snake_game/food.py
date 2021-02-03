# Imports the Turtle class from the turtle module
from turtle import Turtle

# Imports the random module
import random


class Food(Turtle):
    """Creates a piece of food that the snake has to eat."""

    def __init__(self):
        super().__init__()
        # Changes the shape of the food to a circle
        self.shape("circle")

        # Lifts up the pen to not leave a trail
        self.penup()

        # Resizes the circle half its original size
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        # Changes the circle color to blue
        self.color("blue")

        # Changes the circle speed to fastest so the user doesn't
        # see it move from the center to its random position
        self.speed("fastest")

        # Sets the food to a new random position
        self.refresh()

    def refresh(self):
        # Generates a random x coordinate between -280 and 280 for the food
        random_x = random.randint(-280, 280)

        # Generates a random y coordinate between -280 and 280 for the food
        random_y = random.randint(-280, 280)

        # Sets the food to its new random position
        self.goto(random_x, random_y)
