from turtle import Turtle


class Ball(Turtle):
    """
    Class used to represent a ball

    Attributes
    ----------
    x_move : int
        the number of paces the ball goes along the x-axis

    y_move : int
        the number of paces the ball goes along the y-axis

    move_speed : float
        the speed at which the ball goes

    Methods
    -------
    move()
        moves the ball forward

    bounce_y()
        changes the y direction of the ball

    bounce_x()
        changes the x direction of the ball

    reset_position()
        resets the ball position and speed
    """

    def __init__(self):
        super().__init__()
        # Sets the color of the ball to white
        self.color("white")
        # Shapes the ball as a circle
        self.shape("circle")
        # Lifts up the pen to not leave a trail when the scoreboard moves
        self.penup()
        # Sets the initial size of the ball movement along the x-axis
        self.x_move = 10
        # Sets the initial size of the ball movement along the y-axis
        self.y_move = 10
        # Sets the initial ball speed
        self.move_speed = 0.1

    def move(self):
        """Moves the ball forward"""
        # Computes the new x coordinate of the ball by adding its x movement
        new_x = self.xcor() + self.x_move
        # Computes the new y coordinate of the ball by adding its y movement
        new_y = self.ycor() + self.y_move
        # Sets the ball to its new position
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Changes the y direction of the ball"""
        # Negates the ball's y movement so the ball changes y direction
        self.y_move *= -1

    def bounce_x(self):
        """Changes the x direction of the ball"""
        # Negates the ball's x movement so the ball changes x direction
        self.x_move *= -1
        # Increases ball's speed
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets the ball position and speed"""
        # Sets the ball to the center of the screen
        self.goto(0, 0)
        # Sets the ball's speed to its initial value
        self.move_speed = 0.1
        # Changes ball's x direction
        self.bounce_x()
