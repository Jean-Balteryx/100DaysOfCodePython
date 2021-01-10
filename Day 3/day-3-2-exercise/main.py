# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Casts variables as numbers
height = float(height)
weight = int(weight)

#Computes BMI as an integer
bmi = round(weight / height**2)

#Tests the value of the BMI to display the correct message
if bmi < 18.5:
  #The BMI is below 18.5
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  #The BMI is above or equal to 18.5 and below 25
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  #The BMI is above or equal to 25 and below 30
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  #The BMI is above or equal to 30 and below 35
  print(f"Your BMI is {bmi}, you are obese.")
else:
  #The BMI is above or equal to 35
  print(f"Your BMI is {bmi}, you are clinically obese.")