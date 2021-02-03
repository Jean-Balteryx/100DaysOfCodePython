from turtle import Turtle

# Default font for writing on the screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Class to represent a scoreboard on the screen

    Attributes
    ----------
    level
        the current level the player is playing

    Methods
    -------
    update_scoreboard()
        clears and updates the scoreboard

    increment_level()
        increments the level by 1

    game_over()
        displays game over message
    """
    def __init__(self):
        super().__init__()
        # Initializes the level
        self.level = 1
        # Lifts the pen to not leave a trail
        self.penup()
        # Hides the arrow
        self.hideturtle()
        # Sets the scoreboard to the top-left corner
        self.goto(-220, 250)
        # Displays the first level
        self.write("Level: " + str(self.level), align="center", font=FONT)

    def update_scoreboard(self):
        """Clears and updates the scoreboard"""
        # Clears the scoreboard
        self.clear()
        # Displays the current level
        self.write("Level: " + str(self.level), align="center", font=FONT)

    def increment_level(self):
        """Increments the level by 1"""
        # Increments the level by 1
        self.level += 1
        # Updates the scoreboard
        self.update_scoreboard()

    def game_over(self):
        """Displays game over message"""
        # Sets the scoreboard to the center of the screen
        self.goto(0, 0)
        # Displays the game over message
        self.write("GAME OVER", align="center", font=FONT)
