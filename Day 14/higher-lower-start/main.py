#Importing the ASCII arts from the art module
import art

#Importing the random module to pick Instagram accounts
import random

#Importing the data from the game_data module
from game_data import data

#Importing the clear function from the replit module
from replit import clear

#Initializing the boolean that will be used to stop the game when the user is wrong
continue_game = True

#Initializing the user's score
score = 0

#Picking the first Instagram account randomly
account_A = random.choice(data)

#Printing game's logo
print(art.logo)

#Running the game as long as the user is right
while continue_game:
  #Initializing the variable that willl be used to stop the second account picking
  different = False

  #Picking a different account to compare to the first one
  while not different:
    #Picking a random account
    account_B = random.choice(data)

    #Storing the result of the difference between both accounts
    different = account_B != account_A

  #Printing first account information
  print(f"Compare A: {account_A['name']}, a {account_A['description']}, from {account_A['country']}")

  #Printing vs. logo
  print(art.vs)

  #Printing second account information
  print(f"Against B: {account_B['name']}, a {account_B['description']}, from {account_B['country']}")

  #Storing user's choice
  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

  #Storing the right answer comparing the number of followers of both accounts
  if account_A['follower_count'] >= account_B['follower_count']:
    #First account has more followers or they have the same number
    continue_game = user_choice == 'a'
  else:
    #Second account has more followers
    continue_game = user_choice == 'b'

  #Clearing the output
  clear()

  #Printing game's logo
  print(art.logo)

  #If the user is right, its score goes up by 1
  if continue_game:
    score += 1

    #Printing the score of the player
    print(f"You're right! Current score: {score}.")

    #The second account becomes the first account to be compared
    account_A = account_B
  else:
    #Printing user's final score
    print(f"Sorry, that's wrong. Final score: {score}")

    