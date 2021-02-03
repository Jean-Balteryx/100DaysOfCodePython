from turtle import Turtle


class Paddle(Turtle):
    """
    Class used to represent a paddle

    Methods
    -------
    go_up()
        makes the paddle go up

    go_down()
        makes the paddle go down
    """

    def __init__(self, starting_position):
        """
        Parameters
        ----------
        starting_position : tuple
            the position at which the paddle starts
        """

        super().__init__()
        # Sets the color of the paddle to white
        self.color("white")
        # Shapes the paddle as a square
        self.shape("square")
        # Stretches the width of the paddle 5 times to make it a vertical bar
        self.shapesize(stretch_wid=5, stretch_len=1)
        # Lifts up the pen to not leave a trail when the paddle moves
        self.penup()
        # Sets the paddle to its starting position
        self.goto(starting_position)

    def go_up(self):
        """Makes the paddle go up"""
        # Adds 20 to the paddle's y coordinate
        new_y = self.ycor() + 20
        # Sets the paddle to its new position
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Makes the paddle go down"""
        # Subtracts 20 to the paddle's y coordinate
        new_y = self.ycor() - 20
        # Sets the paddle to its new position
        self.goto(self.xcor(), new_y)