# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Casts variable age as an integer
age = int(age)

#Computes years left to live to ease next calculations
years_remaining = (90 - age)

#Computes years, months, weeks and days left to live
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

#Prints the result
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")