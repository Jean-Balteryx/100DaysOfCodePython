# Imports the Screen class from the turtle module
from turtle import Screen

# Imports the Snake class from the snake module
from snake import Snake

# Imports the Food class from the food module
from food import Food

# Imports the Scoreboard class from the scoreboard module
from scoreboard import Scoreboard

# Imports the time module
import time

# Creates a new Screen object
screen = Screen()

# Sets the size of the screen to 600*600
screen.setup(width=600, height=600)

# Sets the screen's background color to black
screen.bgcolor("black")

# Sets the screen title to "My Snake Game"
screen.title("My Snake Game")

# Sets delays for updating drawing to 0
screen.tracer(0)

# Creates a new Snake object
snake = Snake()

# Creates a new Food object
food = Food()

# Creates a new Scoreboard object
scoreboard = Scoreboard()

# Adds a event listener to the screen
screen.listen()

# Binds the up function of the snake object to the key "Up"
screen.onkey(snake.up, "Up")

# Binds the down function of the snake object to the key "Down"
screen.onkey(snake.down, "Down")

# Binds the left function of the snake object to the key "Left"
screen.onkey(snake.left, "Left")

# Binds the right function of the snake object to the key "Right"
screen.onkey(snake.right, "Right")

# Initializes the variable that tells whether the game is running or not
game_is_on = True

# As long as the variable game_is_on is True, the game goes on
while game_is_on:
    # Updates the screen with the new information
    screen.update()

    # The program halts for 0.1 second
    time.sleep(0.1)

    # The snake moves forward
    snake.move()

    # Tests the distance between the snake's head and the food
    if snake.head.distance(food) < 15:
        # The snake ate the food

        # The food goes to a new position
        food.refresh()

        # The snake gains a new segment
        snake.extend()

        # The score is incremented by 1
        scoreboard.increment_score()

    # Tests the coordinates of the snake to determine if he hit a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # The snake hit a wall

        # THe game is over
        game_is_on = False

        # Displays the game over message
        scoreboard.game_over()

    # Goes through all the segments except the head
    for segment in snake.segments[1:]:
        # Tests if the head crossed its tail
        if snake.head.distance(segment) < 10:
            # The head crossed its tail

            # The game is over
            game_is_on = False

            # Displays the game over message
            scoreboard.game_over()

# Sets the screen to exit when the user clicks on it
screen.exitonclick()