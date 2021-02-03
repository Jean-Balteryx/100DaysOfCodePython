# Imports the Turtle class from the turtle module
from turtle import Turtle

# Defines the constants for starting positions and distance to cover when moving
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Defines the constants for degree values of each direction
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Creates a snake the user controls."""

    def __init__(self):
        # Initializes the List that will contain snake segments
        self.segments = []

        # Creates the snake by creating its segments
        self.create_snake()

        # Defines the head of the snake as the first segment
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the snake by creating its starting segments"""
        # Goes through all starting positions
        for position in STARTING_POSITIONS:
            # Creates a segment at the current position
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment ot the snake"""
        # Creates a new segment as a square
        new_segment = Turtle("square")

        # Sets the square's color to white
        new_segment.color("white")

        # Lifts up the pen to not leave a trail
        new_segment.penup()

        # Sets the position of the new segment using the parameter position
        new_segment.goto(position)

        # Adds the new segment to the snake's ones
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Extends the snake as he ate a food"""
        # Adds a new segment on the last one
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward by a constant number of paces"""
        # Goes through all snake's segments backwards except the head
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Sets the new x coordinate of the current segment to the actual x coordinate of the previous segment
            new_x = self.segments[seg_num - 1].xcor()

            # Sets the new x coordinate of the current segment to the actual x coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()

            # Sets the position of the current segment to its new coordinates
            self.segments[seg_num].goto(new_x, new_y)

        # Moves the snake's head forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Changes the snake's direction to make it go up"""
        # If the snake is not going down then it goes up
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes the snake's direction to make it go down"""
        # If the snake is not going up then it goes down
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes the snake's direction to make it go left"""
        # If the snake is not going right then it goes left
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes the snake's direction to make it go right"""
        # If the snake is not going left then it goes right
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
