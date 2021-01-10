# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Test if the year is evenly divisible by 100
if year % 100 == 0:
  #Tests if the year is evenly divisible by 400
  if year % 400 == 0:
    #The year is both evenly divisible by 100 and 400 -> leap year
    print("Leap year.")
  else:
    #The year is evenly divisible by 100 but not by 400 -> not leap year
    print("Not leap year.")
#Tests if the year is evenly divisible by 4
elif year % 4 == 0:
  #The year isn't evenly divisible by 100 but is evenly divisible by 4 -> leap year
  print("Leap year.")
else:
  #The year isn't evenly divisible neither by 100 nor 4 -> not leap year
  print("Not leap year.")