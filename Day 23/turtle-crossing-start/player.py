from turtle import Turtle

# The starting position of the turtle
STARTING_POSITION = (0, -280)
# The number of paces the turtle goes forward when the player press up arrow
MOVE_DISTANCE = 10
# THe y coordinate of the finish line
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Class to represent the player's avatar

    Methods
    -------
    up()
        moves the turtle up

    reset_position()
        resets the position of the turtle to its starting position
    """

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        # Lifts the pen up to not leave a trail
        self.penup()
        # Sets the heading of the turtle up
        self.setheading(90)
        # Sets the turtle to its starting position
        self.goto(STARTING_POSITION)

    def up(self):
        """Moves the turtle up"""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Resets the position of the turtle to its starting position"""
        self.goto(STARTING_POSITION)
