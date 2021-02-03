###145. Constructing Objects and Accessing their Attributes and Methods###

# Imports the Turtle and Screen objects from the turtle module
from turtle import Turtle, Screen

# Creates a new Turtle object
bob = Turtle()

# Prints the Turtle object
print(bob)

# Changes the shape of Bob as represented in the canvas using the method shape()
bob.shape("turtle")

# Changes the color of Bob as represented in the canvas using the method color()
bob.color("SlateBlue1", "Wheat4")

# Makes Bob goes forward by 100 paces
bob.forward(100)

# Creates a new Screen object
my_screen = Screen()

# Prints the height of the canvas from Screen object using the attribute canvheight
print(my_screen.canvheight)

# Uses the Screen object method exitonclick() to make the canvas not disappear instantly
my_screen.exitonclick()


###146. How to Add Python Packages and use PyPi###

# Imports the package prettytable
from prettytable import PrettyTable

# Creates a new PrettyTable object
table = PrettyTable()

# Adds a column containing Pokemon names
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

# Adds a column containing Pokemon types
table.add_column("Type", ["Electric", "Water", "Fire"])

# Changes the alignment of the table's content
table.align = "l"

# Prints the table
print(table)

