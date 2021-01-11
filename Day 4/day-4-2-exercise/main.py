# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Imports the random module
import random

#Generates a random position from 0 to the size of the list minus 1
random_position = random.randint(0, len(names)-1)

#Prints the message using the name at the random position in the list
print(names[random_position] + " is going to buy the meal today!")