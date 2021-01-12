###48. Using the for loop with Python Lists###

#Declares a list of fruits
fruits = ["Apple", "Peach", "Pear"]

#Goes through the list of fruits using a for loop -> the loop continues as long as there are elements in the list
for fruit in fruits:
  #Prints current fruit
  print(fruit + " Pie")

#This line is indented back so the for loop is ended
print(fruits)


###51. for loops and the range() function###

#range() function creates a range from the first parameter to the second with a step matching the third (optional)
for number in range(1, 11, 3):
  print(number)

#Initializes a total variable
total = 0

#Goes through each number from 1 to 101
for number in range(1, 101):
  #Adds the current number to the total
  total += number

#Prints the total
print(total)