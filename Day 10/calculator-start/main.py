#Importing the logo from the art module
from art import logo

#Importing the clear function from the replit module
from replit import clear

#Defining the add() function which adds two numbers
def add(n1, n2):
  return n1 + n2

#Defining the subtract() function which subtract two numbers
def subtract(n1, n2):
  return n1 - n2

#Defining the multiply() function which multiply two numbers
def multiply(n1, n2):
  return n1 * n2

#Defining the divide() function which divide two numbers
def divide(n1, n2):
  return n1 / n2

#Defining the Dictionary operations which stores operators and associated functions
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

#Defines the calculator() function which allow the user to compute operations
def calculator():
  #Clearing the output console
  clear()

  #Printing the logo
  print(logo)

  #Storing the user input for the first number
  num1 = float(input("What's the first number?: "))

  #Printing available operations
  for operation in operations:
    print(operation)

  #Creating the variable used to know if the user wants to continue calculating with the previous result or not
  stop = False

  #Looping as long as the user doesn't stop
  while not stop:
    #Storing the user input for the operator
    operation_symbol = input("Pick an operation: ")

    #Storing the user input for the second number
    num2 = float(input("What's the next number?: "))

    #Computing both numbers using the function matching the operator
    result = operations[operation_symbol](num1, num2)

    #Printing the operation and the result
    print(f"{num1} {operation_symbol} {num2} = {result}")

    #Storing the user's choice to continue or stop
    again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")

    #Testing whether the user wants to continue or stop
    if again == 'n':
      #The user wants to stop
      stop = True

      #Starts a new calculator instance
      calculator()
    else:
      #Storing the result of the preivous operation as the first number
      num1 = result

#Starting the program
calculator()