###27. Control Flow with if / else and Conditional Operators###

print("Welcome to the rollercoaster!")

#Asks the user for its height
height = int(input("What is your height in cm? "))

#Conditional structure to display a message depending on the height input
#Tests if the height is above or equal to 120 cm
if height >= 120:
  #The height is above or equal to 120 cm
  print("You can ride the rollercoaster!")
else:
  #The height is below 120 cm
  print("Sorry, you have to grow taller before you can ride.")

  ##Conditional Operators
  #== : equal to
  #!= : different than
  #< : below
  #> : above
  #<= : below or equal to
  #>= : above or equal to


###29. Nested if statements and elif statements###

print("Welcome to the rollercoaster!")

#Asks the user for its height
height = int(input("What is your height in cm? "))

#Conditional structure to display a message depending on the height input
#Tests if the height is above or equal to 120 cm
if height >= 120:
  #The height is above or equal to 120 cm
  print("You can ride the rollercoaster!")
  
  #Asks the user for its age
  age = int(input("What is your age? "))

  #Tests if the age is below 12
  if age < 12:
    #The age is below 12
    print("Please pay $5.")
  #Tests if the age is below or equal to 18
  elif age <= 18:
    #The age is below or equal to 18
    print("Please pay $7.")
  else:
    #The age is over 18
    print("Please pay $12.")
else:
  #The height is below 120 cm
  print("Sorry, you have to grow taller before you can ride.")


###32. Multiple if Statements in Succesion###

print("Welcome to the rollercoaster!")

#Asks the user for its height
height = int(input("What is your height in cm? "))

bill = 0

#Conditional structure to display a message depending on the height input
#Tests if the height is above or equal to 120 cm
if height >= 120:
  #The height is above or equal to 120 cm
  print("You can ride the rollercoaster!")
  
  #Asks the user for its age
  age = int(input("What is your age? "))

  #Tests if the age is below 12
  if age < 12:
    #The age is below 12
    bill += 5
    print("Child tickets are $5.")
  #Tests if the age is below or equal to 18
  elif age <= 18:
    #The age is below or equal to 18
    bill += 7
    print("Youth tickets are $7.")
  else:
    #The age is over 18
    bill += 12
    print("Adults tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")
  
else:
  #The height is below 120 cm
  print("Sorry, you have to grow taller before you can ride.")


###34. Logical Operators###

##Logical Operators
#and : expr1 and expr2 -> if both expr1 and expr2 are true then the total is true else the total is false
#or : expr1 or expr2 -> if at least one of the expr is true then the total is true else the totla is false
#not : not expr -> returns the opposite (true -> false, false -> true)

print("Welcome to the rollercoaster!")

#Asks the user for its height
height = int(input("What is your height in cm? "))

bill = 0

#Conditional structure to display a message depending on the height input
#Tests if the height is above or equal to 120 cm
if height >= 120:
  #The height is above or equal to 120 cm
  print("You can ride the rollercoaster!")
  
  #Asks the user for its age
  age = int(input("What is your age? "))

  #Tests if the age is below 12
  if age < 12:
    #The age is below 12
    bill += 5
    print("Child tickets are $5.")
  #Tests if the age is below or equal to 18
  elif age <= 18:
    #The age is below or equal to 18
    bill += 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. You get to ride on us!")
  else:
    #The age is over 18
    bill += 12
    print("Adults tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")
  
else:
  #The height is below 120 cm
  print("Sorry, you have to grow taller before you can ride.")