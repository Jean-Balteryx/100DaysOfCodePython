# Imports the Turtle class from the turtle module
from turtle import Turtle


class Scoreboard(Turtle):
    """Creates a scoreboard that keeps track of the score and tells the user the game is over."""

    def __init__(self):
        super().__init__()

        # Initializes the score to 0
        self.score = 0

        # Sets the color of the text to white
        self.color("white")

        # Hides the default arrow
        self.hideturtle()

        # Lifts up the pen to not leave a trail
        self.penup()

        # Sets the position of the scoreboard to the top of the screen
        self.goto(0, 250)

        # Writes the scoreboard
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def update_scoreboard(self):
        """Clears the scoreboard and rewrites it."""

        # Clears the scoreboard
        self.clear()

        # Writes the scoreboard
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        """Displays the game over message."""

        # Sets the position of the message to the center of the screen
        self.goto(0, 0)

        # Writes the game over message
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increment_score(self):
        """Increments the user's score by 1."""

        # Increments the score by 1
        self.score += 1

        # Updates the scoreboard
        self.update_scoreboard()
