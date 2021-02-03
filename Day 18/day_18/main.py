###163. Understanding Turtle Graphics and How to use the Documentation###
###165. Importing Modules, Installing Packages, and Working with Aliases###
###169. Python Tuples and How to Generate Random RGB Colours###

# Imports the module turtle and gives it an alias t
import turtle as t

# Imports the random module
import random

# Imports Turtle and Screen classes from the turtle module
# from turtle import Turtle, Screen

# Creates a new Turtle object named Bob
bob = t.Turtle()

# Changes the shape of Bob
bob.shape("turtle")

# Changes the color mode to 255
t.colormode(255)

# Declares a new Tuple
my_tuple = (1, 3, 8)

# Accessing a value in a Tuple is the same as in a List
my_tuple[2]


def random_color():
    """Returns a random color using RGB values"""
    # Picks a random integer between 0 and 255 as the R component
    r = random.randint(0, 255)

    # Picks a random integer between 0 and 255 as the G component
    g = random.randint(0, 255)

    # Picks a random integer between 0 and 255 as the B component
    b = random.randint(0, 255)

    # Returns a Tuple of the RGB components of the color
    return r, g, b


# TypeError -> values in a Tuple can't be modified
# my_tuple[2] = 12

# Changes the color of Bob
# bob.color("red", "blue")

# Makes Bob go forward by 100 paces
# bob.forward(100)

# Makes Bob turn right by 90 degrees
# bob.right(90)


###164. Turtle Challenge 1 : Draw a Square###

# Loops 4 times to draw the 4 sides of the square
for i in range(4):
    # Turns Bob by 90 degrees on the right
    bob.right(90)

    # Makes Bob go forward by 100 paces
    bob.forward(100)


###166. Turtle Challenge 2 : Draw a Dashed Line###

# Loops 15 times to draw 15 dashes
for i in range(15):
    # Makes Bob go forward by 10 paces
    bob.forward(10)

    # Lifts up the pen -> white space
    bob.penup()

    # Makes Bob go forward by 10 paces
    bob.forward(10)

    # Downs the pen -> dash
    bob.pendown()


###167. Turtle Challenge 3 : Drawing Different Shapes###


def draw_shape(number_of_sides):
    """Draws a polygon with the specified number of sides"""
    # Computes the angle's value of the polygon
    angle = 360 / number_of_sides

    # Draw the input number of sides
    for stroke in range(number_of_sides):
        # Makes Bob go forward by 100 paces
        bob.forward(100)

        # Turns Bob by the computed angle on the right
        bob.right(angle)


# Draws polygon from 3 sides (triangle) to 10 sides (decagon)
for sides in range(3, 11):
    # Assigns a random color to Bob
    bob.color(random_color())

    # Draw the shape matching the current number of sides
    draw_shape(sides)


###168. Turtle Challenge 4 : Drawing Random Walk###

# Creates a list of the possible directions
directions = [0, 90, 180, 270]


def random_move():
    """Moves the turtle in a random direction"""
    # Turns the turtle in a random direction
    bob.right(random.choice(directions))

    # Assigns a random color to Bob
    bob.color(random_color())

    # Makes Bob go forward by 10 paces
    bob.forward(10)


# Changes the speed of Bob to the fastest
bob.speed("fastest")

# Sets the pen size to 10
bob.pensize(10)

# Makes a 100 random moves
for i in range(100):
    random_move()


###170. Turtle Challenge 5 : Draw a Spirograph###

def draw_spirograph(gap_size):
    """Draws a spirograph with the specified gap size"""
    # Draws as many circles as needed based on the gap size
    for i in range(int(360 / gap_size)):
        # # Assigns a random color to Bob
        bob.color(random_color())

        # Draws a circle with a diameter of 100
        bob.circle(100)

        # Turns Bob by the gap size to the left
        bob.left(gap_size)


# Draw a spirograph with a gap size of 1
draw_spirograph(1)

# Creates a new Screen object named screen
screen = t.Screen()

# Sets the screen to exit when the user click
screen.exitonclick()