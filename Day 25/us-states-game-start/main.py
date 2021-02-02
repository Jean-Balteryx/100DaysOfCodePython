import turtle
import pandas

# Creates the game screen
screen = turtle.Screen()
# Adds a title to the screen
screen.title("U.S. States Game")
# Add an image to the screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Initializes the List containing correct guesses of the player
correct_guesses = []

# Reads states data from csv file and transforms it as a List
# File : 50_states.csv
# Columns :
#   - state: state's name
#   - x, y: coordinates of where to write state's name on the map
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

# Runs the game while the user didn't guess all states or entered "Exit"
while len(correct_guesses) < 50:
    # Stores user's guess and displays right guesses count in the input window
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # Checks if the user asked to exit the game
    if answer_state == "Exit":
        # Retrieves all states not guessed by the user
        missing_states = [state for state in states if state not in correct_guesses]
        # Builds a DataFrame from List of missing states
        new_data = pandas.DataFrame(missing_states)
        # Writes the DataFrame into a csv file
        new_data.to_csv("states_to_learn.csv")
        # Stops the game
        break

    # Checks if user's guess is a right guess
    if answer_state in states:
        # Defines a Turtle object to write the state name at its position
        t = turtle.Turtle()
        # Hides the arrow
        t.hideturtle()
        # Lifts up the pen to not leave a trail when going to the state's position
        t.penup()
        # Retrieves data matching the guessed state
        state_data = data[data.state == answer_state]
        # Goes to the state position
        t.goto(int(state_data.x), int(state_data.y))
        # Writes the state's name
        t.write(answer_state)
        # Adds the state to the correct guesses
        correct_guesses.append(answer_state)
