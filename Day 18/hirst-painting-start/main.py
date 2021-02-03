# Imports the module colorgram used to extract colors from an image
import colorgram

# Imports the random module
import random

# Imports the turtle module
import turtle as t

# Initializes the List that will contain colors
rgb_colors = []

# Extracts 30 colors from image.jpg
colors = colorgram.extract('image.jpg', 30)

# Goes through all colors extracted
for color in colors:
    # Extract red component from the current color
    r = color.rgb.r

    # Extract green component from the current color
    g = color.rgb.g

    # Extract blue component from the current color
    b = color.rgb.b

    # Appends a Tuple built from the three color components to the list of colors
    rgb_colors.append((r, g, b))

# Creates a new Screen object named screen
screen = t.Screen()

# Sets the coordinates of the screen
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

# Creates a new Turtle object named Bob
bob = t.Turtle()

# Changes the color mode to 255
t.colormode(255)

# Changes the speed of Bob to the fastest
bob.speed("fastest")

# Hides Bob
bob.hideturtle()

# Lifts the pen up to not draw lines when moving
bob.penup()

# Sets Bob starting position
bob.setpos(40, 15)

# Creates ten rows of dots
for i in range(10):
    # For each line creates 10 dots
    for j in range(10):
        # Draw a dot with a diameter of 20 and a random color
        bob.dot(20, random.choice(rgb_colors))

        # Sets the position of Bob to the position of the next dot in the row
        bob.setpos(bob.xcor()+70, bob.ycor())

    # Sets the position of Bob to the first dot of the next row
    bob.setpos(40, bob.ycor() + 70)

# Sets the screen to exit when the user click
screen.exitonclick()
