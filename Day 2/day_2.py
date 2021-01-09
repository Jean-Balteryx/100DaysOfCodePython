###17. Python Primitive Data Types###

##String --> literals

"Hello"

#Using brackets allows to choose a particular character
print("Hello"[0])

#Using + sign with strings concatenates them
print("123" + "345")

##Integer --> whole numbers

56283

#Using + sign with integers sums them
print(123 + 345)

#Underscores can be used with large numbers to make them more readable
123_456_789

##Float --> decimal numbers

3.14159

#Boolean --> True/False are the only values

True
False


###19. Type Error, Type Checking and Type Conversion

#TypeError
#len(4837)

#TypeError
num_char = len(input("What is your name?"))
#print("Your name has " + num_char + " characters.")

#type() function returns the type of the data input
print(type(num_char))

#str() function converts the data input to a string
new_num_char = str(num_char)

#Now it works as the variable new_num_char is a string
print("Your name has " + new_num_char + " characters.")

#float() function converts the data input to a float
a = float(123)
print(type(a))


###20. Mathematical Operations in Python###

#Addition
3 + 5

#Substraction
7 - 4

#Multiplication
3 * 2

#Division -> always returns a float
6 / 3

#Power
2 ** 2

##PEMDAS
#Parenthesis
#Exposant
#Multiplication, Division
#Addition, Substraction
print(3 * 3 + 3 / 3 - 3)

#Challenge : How to get 6 from the previous operation ?
print(3 * (3 + 3) / 3 - 3)


###22. Number Manipulation and F Strings in Python###

#round() function rounds the number input
print(round(8 / 3))

#round() function can round to any precision specified as the second parameter
print(round(8 / 3, 2))

#// returns the result of the division as an integer, flooring the float result
print(8 // 3)


result = 4 / 2
#Equals result = result / 2
result /= 2
print(result)


score = 0
height = 1.8
isWinning = True

#f-String
print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")