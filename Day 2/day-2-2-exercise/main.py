# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Casts variables as numbers
height = float(height)
weight = int(weight)

#Computes BMI as an integer
bmi = int(weight / height**2)

#Prints BMI
print(bmi)