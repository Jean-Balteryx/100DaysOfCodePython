#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

#Imports the random module
import random

#Tests the value of a random generated integer between 0 and 1
if random.randint(0, 1) == 0:
  #The generated integer is 0
  print("Tails")
else:
  #The generated integer is 1
  print("Heads")