#Write your code below this line 👇

#Defines the function that checks if a number is a prime one
def prime_checker(number):

  #Inititalizes the variable storing the result
  prime = True

  #Goes thourgh all the number from 2 to the tested number - 1
  for i in range(2, number):
    #Tests if the tested number is divisible by the current number
    if number % i == 0:
      #As the tested number is divisible by the current number, it's not a prime number
      prime = False

  #Prints whether the number is prime or not depending of the value of the variable prime
  if prime == True:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



