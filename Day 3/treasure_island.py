print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Asks the player to choose a direction between "left" and "right"
direction = input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''').lower()

#Tests which direction has been chosen
if direction == "left":
  #The player went for left

  #Asks the player how to cross the lake either waiting for a boat or swimming
  cross_water = input('''You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n''').lower()

  #Tests which way to cross has been chosen
  if cross_water == "wait":
    #The player chose to wait for a boat

    #Asks the player which door to open between "yellow", "blue" and "red"
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()

    #Tests which door has been chosen
    if door == "yellow":
      #The user chose the yellow door -> win
      print("You found the treasure! You Win!")
    elif door == "blue":
      #The user chose the blue door -> lose
      print("You enter a room of beasts. Game Over.")
    elif door == "red":
      #The user chose the red door -> lose
      print("It's a room full of fire. Game Over.")
    else:
      #The user chose a door that doesn't exist -> lose
      print("You chose a door that doesn't exist. Game Over.")
  else:
    #The player chose to swim -> lose
    print("You get attacked by an angry trout. Game Over.")
else:
  #The player went for right -> lose
  print("You fell into a hole. Game Over.")