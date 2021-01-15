# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Defines the function
def greet():
  print("Hello!")
  print("Welcome to this program!")
  print("I hope you are fine!")

#Calls the function
greet()

#Functions with parameter "name"
def greet_with_name(name):
  print(f"Hello {name}!")
  print(f"How are you doing {name}?")

#Calls the function with argument "Bob"
greet_with_name("Bob")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"hello {name}!")
  print(f"What is it like in {location}?")

#Calls the function with positional arguments "Bob" and "Sidney"
greet_with("Bob", "Sydney")

#Calls the function with keyword arguments "Bob" and "Sidney"
greet_with(location = "Sydney", name = "Bob")