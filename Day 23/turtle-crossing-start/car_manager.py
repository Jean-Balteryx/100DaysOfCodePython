from turtle import Turtle
import random

# The cars colors
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# The starting speed
STARTING_MOVE_DISTANCE = 5
# The speed increment when the player pass a level
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """
    Class to represent a car manager

    Attributes
    ----------
    cars
        the List of all the cars

    speed
        the forward movement made by the cars

    Methods
    -------
    add_car()
        adds a new car to the car manager

    move()
        makes all the cars move forward

    increase_speed()
        increases the speed of all the cars
    """
    def __init__(self):
        super().__init__()
        # Hides the arrow
        self.hideturtle()
        # Initializes the list of cars
        self.cars = []
        # Initializes the speed
        self.speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        """Adds a new car to the car manager"""
        # Generates a new car with a probability of 1/7
        if random.randint(0, 6) == 1:
            # Creates the new car as a square
            new_car = Turtle("square")
            # Sets a random color ot the car
            new_car.color(random.choice(COLORS))
            # Lifts the pen to not leave a trail
            new_car.penup()
            # Stretches the car length by 2
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            # Generates a random starting x coordinate
            random_x = random.randint(320, 360)
            # Generates a random starting y coordinate
            random_y = random.randint(-250, 250)
            # Sets the car to its random starting position
            new_car.goto(random_x, random_y)
            # Sets heading car to the left
            new_car.setheading(180)
            # Adds the new car to the list of cars
            self.cars.append(new_car)

    def move(self):
        """Makes all the cars move forward"""
        for car in self.cars:
            # Makes the current car go forward
            car.forward(self.speed)

    def increase_speed(self):
        """Increases the speed of all the cars"""
        # Increases cars speed by the value of the constant MOVE_INCREMENT
        self.speed += MOVE_INCREMENT
