#Imports the random module
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Creates the list of the signs
signs = [rock, paper, scissors]

#Stores the user's sign choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice > 2:
  print("You input an invalid choice. You lose.")
else:
  #Creates a random integer between 0 and 2 as the computer choice
  computer_choice = random.randint(0,2)

  #Picks the sign matching user's choice
  user_sign = signs[user_choice]

  #Picks the sign matching computer's choice
  computer_sign = signs[computer_choice]

  #Prints the user sign
  print(user_sign)

  print("Computer chose:")

  #Prints the computer sign
  print(computer_sign)

  #Tests if user chose rock and computer chose scissors -> win
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  #Tests if user chose scissors and computer chose rock -> lose
  elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
  #Tests if user's choice comes after computer's choice -> win
  elif user_choice > computer_choice:
    print("You win!")
  #Tests if computer's choice comes after user's choice -> lose
  elif computer_choice > user_choice:
    print("You lose!")
  else:
    #User and computer chose both the same
    print("It's a draw!")  