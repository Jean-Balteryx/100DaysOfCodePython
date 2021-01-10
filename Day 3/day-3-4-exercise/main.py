# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Initializes the bill
bill = 0

#Tests the size input by the user
if size == "S":
  #The user wants a S size pizza that costs $15
  bill += 15
elif size == "M":
  #The user wants a M size pizza that costs $20
  bill += 20
else:
  #The user wants a L size pizza that costs $25
  bill += 25

#Tests if the user wants pepperoni
if add_pepperoni == "Y":
  #The user wants pepperoni so now it tests the size of the pizza
  if size == "S":
    #The pizza is an S size so the option costs $2
    bill += 2
  else:
    #The pizza is either a M or L size pizza so the option costs $3
    bill += 3

#Tests if the user wants extra cheese
if extra_cheese == "Y":
  #The user wants extra cheese that costs $1
  bill += 1

#Prints the final bill of the user
print(f"Your final bill is: ${bill}.")