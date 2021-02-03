from turtle import Turtle


class Scoreboard(Turtle):
    """
    Class used to represent a scoreboard

    Attributes
    ----------
    l_score : int
        the score of the left player

    r_score : int
        the score of the right player

    Methods
    -------
    update_scoreboard()
        clears and updates the scoreboard

    l_point()
        increases the score of the left player by 1

    r_point()
        increases the score of the right player by 1

    """

    def __init__(self):
        super().__init__()
        # Sets the color of the scoreboard to white
        self.color("white")
        # Lifts up the pen to not leave a trail when the scoreboard moves
        self.penup()
        # Hides the arrow
        self.hideturtle()
        # Initializes the left player's score
        self.l_score = 0
        # Initializes the right player's score
        self.r_score = 0
        # Displays the scoreboard
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard"""
        # Clears the scoreboard
        self.clear()
        # Sends the scoreboard to its left part
        self.goto(-100, 200)
        # Writes left player's score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # Sends the scoreboard to its right part
        self.goto(100, 200)
        # Writes the right player's score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increases the score of the left player by 1"""
        # Adds 1 to the left player's score
        self.l_score += 1
        # Updates the scoreboard
        self.update_scoreboard()

    def r_point(self):
        """Increases the score of the right player by 1"""
        # Adds 1 to the right player's score
        self.r_score += 1
        # Updates the scoreboard
        self.update_scoreboard()
