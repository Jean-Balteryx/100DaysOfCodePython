#Write your code below this row 👇

#Goes through all numbers from 1 to 100
for number in range(1, 101):
  #Tests if the number is divisible by 3 and 5
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  #Tests if the number is divisible by 3
  elif number % 3 == 0:
    print("Fizz")
  #Tests if the number is divisible by 5
  elif number % 5 == 0:
    print("Buzz")
  else:
    #The number is neither divisible by 3 nor 5
    print(number)