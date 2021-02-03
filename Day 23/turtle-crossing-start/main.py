import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creates the screen
screen = Screen()
# Sets the screen size
screen.setup(width=600, height=600)
# Disable screen delays
screen.tracer(0)

# Creates the game components
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Makes the turtle goes up when the player press the up arrow key
screen.listen()
screen.onkey(player.up, "Up")

# Creates the control variable of the game
game_is_on = True

while game_is_on:
    # Refreshes the screen every 0.1 second
    time.sleep(0.1)
    screen.update()

    # Manages cars appearance and movement
    car_manager.add_car()
    car_manager.move()

    # Detects collision with up wall
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increment_level()
        car_manager.increase_speed()

    # Detects collision with cars
    for car in car_manager.cars:
        if abs(player.xcor()-car.xcor()) < 20 and abs(player.ycor()-car.ycor()) < 20:
            game_is_on = False
            # Displays game over message
            scoreboard.game_over()

# Sets the screen to exit when the user clicks
screen.exitonclick()
