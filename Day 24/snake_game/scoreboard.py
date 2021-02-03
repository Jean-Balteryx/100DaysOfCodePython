# Imports the Turtle class from the turtle module
from turtle import Turtle


class Scoreboard(Turtle):
    """Creates a scoreboard that keeps track of the score and tells the user the game is over."""

    def __init__(self):
        super().__init__()

        # Initializes the score to 0
        self.score = 0

        with open("data.txt") as file:
            self.high_score = int(file.read())

        # Sets the color of the text to white
        self.color("white")

        # Hides the default arrow
        self.hideturtle()

        # Lifts up the pen to not leave a trail
        self.penup()

        # Sets the position of the scoreboard to the top of the screen
        self.goto(0, 250)

        # Writes the scoreboard
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def update_scoreboard(self):
        """Clears the scoreboard and rewrites it."""

        # Clears the scoreboard
        self.clear()

        # Writes the scoreboard
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    def increment_score(self):
        """Increments the user's score by 1."""

        # Increments the score by 1
        self.score += 1

        # Updates the scoreboard
        self.update_scoreboard()
