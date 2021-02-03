###175. Python Higher Order Functions & Event Listener###

# Imports Turtle and Screen classes from the turtle module
from turtle import Turtle, Screen

# Creates a new Turtle object
bob = Turtle()

# Creates a new Screen object
screen = Screen()


def move_forwards():
    """Makes the turtle move forward by 10 paces"""
    bob.forward(10)


# Allows the screen to listen to user keyboard inputs
screen.listen()

# Binds a function to a key -> as the onkey function calls another function, it's the higher order function
screen.onkey(move_forwards, "space")


###176. Challenge : Make a Etch-a-Sketch App###


def move_forward():
    """Makes bob move forward by 1 pace"""
    bob.forward(1)


def move_backward():
    """Makes bob move backward by 1 pace"""
    bob.backward(1)


def turn_left():
    """Turns bob left by 10 degrees"""
    bob.left(10)


def turn_right():
    """Turns bob right by 10 degrees"""
    bob.right(10)


def reset_screen():
    """Resets the screen"""
    screen.reset()


# Binds the function move_forward() to the up arrow key
screen.onkey(move_forward, "Up")

# Binds the function move_backward() to the down arrow key
screen.onkey(move_backward, "Down")

# Binds the function turn_left() to the left arrow key
screen.onkey(turn_left, "Left")

# Binds the function turn_right() to the right arrow key
screen.onkey(turn_right, "Right")

# Binds the function reset_screen() to the c key
screen.onkey(reset_screen, "c")

# Sets the screen to exit when the user clicks
screen.exitonclick()
