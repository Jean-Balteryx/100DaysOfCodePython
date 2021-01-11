###39. Random Module###

#Imports the random module
import random

#randomint() function creates a random integer between specified integers
random_integer = random.randint(1, 10)
print(random_integer)

#random() function creates a random decimal number between 0 and 1
random_float = random.random()
print(random_float)


###41. Understanding the Offset and Appending Items to Lists###

#Lists are declared using brackets and separating values using commas
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#Retrieves the first element of the list
print(states_of_america[0])

#Retrieves the element before the last of the list
print(states_of_america[-2])

#Adds elements to the list
#states_of_america.extend(["Angelaland", "Jack Bauer Land"])
#print(states_of_america)

#Modifies element from the list
#states_of_america[1] = "Pencilvania"
#print(states_of_america)


###43. IndexErrors and Working with Nested Lists###

#IndexError
#print(states_of_america[50])

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#Creates two lists from dirty_dozen, one for fruits and one for vegetables
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#Nest both lists in dirty_dozen list
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

#Prints third element of the first list within dirty_dozen
print(dirty_dozen[0][2])