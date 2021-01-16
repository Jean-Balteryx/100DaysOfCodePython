#Importing the clear() function to clear the output window
from replit import clear

#Importing the logo variable to print it
from art import logo

#Printing the logo
print(logo)

#Printing the welcome message
print("Welcome to the secret auction program.")

#Creating the Dictionary that will store the bids
bids = {}

#Defining the function that register the bids
def register_bid():
  #Storing the user input for its name
  bidder = input("What is your name?: ")

  #Storing the user input for its bid
  bid = int(input("What is your bid?: $"))

  #Adding the user's bid to the Dictionary storing all bids
  bids[bidder] = bid

  #Storing the user input for a new bidder
  new_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  #Clearing the output window
  clear()

  #Testing if there is a new bidder
  if new_bidder == 'yes':
    #There is a new bidder -> registering a new bid
    register_bid()
  else:
    #There is no more bidder -> finding the highest bidder
    find_highest_bid()


#Defining the function that find the highest bid and the winner of the auction
def find_highest_bid():
  #Creating the variable storing the highest bid
  highest_bid = 0

  #Creating the variable storing the winner
  winner = ""

  #Going through all the bidders
  for bidder in bids:
    #Testing if the current bid is higher than the highest bid
    if highest_bid < bids[bidder]:
      #The current bid becomes the highest bid
      highest_bid = bids[bidder]

      #The current bidder becomes the winner 
      winner = bidder

  #Printing the result of the auction
  print(f"The winner is {winner} with a bid of ${highest_bid}")


#Starting the auction
register_bid()