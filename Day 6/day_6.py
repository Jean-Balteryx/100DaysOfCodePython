###57. Defining and Calling Python Functions###

#Defines the function my_function() that prints the messages "Hello" and "Bye"
def my_function():
  print("Hello")
  print("Bye")

#Calls the function my_function()
my_function()

###59. Indentation in Python###

#Code can be indented using both spaces and tabs -> 1 tab / 2 spaces / 4 spaces

#IndentationError
#def indentation_error():
#print("Error")

###61. While Loops###

#For loops -> iterate over something (through a list, within a range, etc.°)
#While loops -> iterate as long as a condition is not met

#Inititalizes a number variable
number = 0

#While number is less than 5, the loop goes on
while number < 5:
  #Adds 1 to number
  number += 1
  
print(number)