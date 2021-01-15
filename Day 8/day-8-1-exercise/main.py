#Write your code below this line 👇

#Imports the ceil function from the math module
from math import ceil

#Defines the function paint_calc with 3 parameters : height of the wall, width of the wall and coverage
def paint_calc(height, width, cover):
  #Computes the number of cans needed
  cans_number = ceil(height * width / cover)

  #Prints the result
  print(f"You'll need {cans_number} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)