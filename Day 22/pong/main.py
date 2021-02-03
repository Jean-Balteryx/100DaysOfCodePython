# Imports useful classes and modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Creates the screen
screen = Screen()
# Sets the screen background color to black
screen.bgcolor("black")
# Sets the screen's size to 800*600
screen.setup(width=800, height=600)
# Sets screen's title to "Pong"
screen.title("Pong")
# Deactivates screen's tracer
screen.tracer(0)

# Creates the right paddle
r_paddle = Paddle((350, 0))
# Creates the left paddle
l_paddle = Paddle((-350, 0))
# Creates the ball
ball = Ball()
# Creates the scoreboard
scoreboard = Scoreboard()

# Makes the screen listen the keyboard events
screen.listen()
# Makes the right paddle go up when user press the up arrow key
screen.onkey(r_paddle.go_up, "Up")
# Makes the right paddle go down when user press the up arrow key
screen.onkey(r_paddle.go_down, "Down")

# Makes the left paddle go up when user press the z key
screen.onkey(l_paddle.go_up, "z")
# Makes the left paddle go down when user press the s key
screen.onkey(l_paddle.go_down, "s")

# Creates the variable that controls whether the game goes on or not
game_is_on = True


while game_is_on:
    # Uses ball speed to pause the animation : the higher the speed value, the higher the pause
    time.sleep(ball.move_speed)
    # Updates the screen
    screen.update()
    # Moves the ball
    ball.move()

    # Detects collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # As the ball hit a wall the y direction changes
        ball.bounce_y()

    # Detects collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # As the ball hit a paddle the x direction changes
        ball.bounce_x()

    # Detects when the right paddle misses the ball
    if ball.xcor() > 380:
        # Resets the ball position and speed
        ball.reset_position()
        # Adds a point to the left player
        scoreboard.l_point()

    # Detects when the left paddle misses the ball
    if ball.xcor() < -380:
        # Resets the ball position and speed
        ball.reset_position()
        # Adds a point to the right player
        scoreboard.r_point()

# Sets the screen to exit when the user click
screen.exitonclick()
