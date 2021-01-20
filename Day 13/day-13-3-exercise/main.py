for number in range(1, 101):
  #if number % 3 == 0 or number % 5 == 0: -> "FizzBuzz" has to be displayed when both the conditions are true, not only one of them
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  #if number % 3 == 0: -> elif has to be used as only one condition should be fulfilled at max
  elif number % 3 == 0:
    print("Fizz")
  #if number % 5 == 0: -> elif has to be used as only one condition should be fulfilled at max
  elif number % 5 == 0:
    print("Buzz")
  else:
    #print([number]) -> [] don't have to be displayed
    print(number)