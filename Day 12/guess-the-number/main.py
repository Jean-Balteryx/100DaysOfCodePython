#Importing the logo from the art module
from art import logo

#Importing the random module to pick the number between 1 and 100
import random

#Declaring constants for number of attempts based on difficulty level and for the number to guess
EASY_MODE_ATTEMPTS = 10
HARD_MODE_ATTEMPTS = 5
NUMBER_TO_GUESS = random.randint(1,100)

#Printing the logo
print(logo)

#Printing the greetings message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

#Storing the user's difficulty choice
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

#Initializing the number of remaining attempts based on the selected difficulty
if difficulty == 'easy':
  #The user goes for easy mode
  attempts_remaining = EASY_MODE_ATTEMPTS
elif difficulty == 'hard':
  #The user goes for hard mode
  attempts_remaining = HARD_MODE_ATTEMPTS
else:
  #The user didn't input a valid difficulty
  print("Please, pick a valid difficulty.")

#As long as the user has attempts the game goes on
while attempts_remaining > 0:
  #Printing the number of remaining attempts
  print(f"You have {attempts_remaining} attempts remaining to guess the number")

  #Storing the user guess
  guess = int(input("Make a guess: "))

  #Comparing user's guess and number to guess
  if guess == NUMBER_TO_GUESS:
    #The user guessed correctly, the program stops the loop
    break
  elif guess > NUMBER_TO_GUESS:
    #The user's guess is higher than the number to guess
    print("Too high.")
  else:
    #The user's guess is lower than the number to guess
    print("Too low.")
  
  #Subtracting 1 to the number of remaining attempts
  attempts_remaining -= 1

  #Testing the number of remaining attempts
  if attempts_remaining > 0:
    #The user has remaining attempts so he can guess again
    print("Guess again.")

#Testing the number of attempts remaining after the game is over
if attempts_remaining > 0:
  #The user has remaining attempts, it means he guessed the number
  print(f"You got it! The answer was {NUMBER_TO_GUESS}.")
else:
  #The user has no remaining attempts, he didn't guess the number
  print("You've run out of guesses, you lose.")