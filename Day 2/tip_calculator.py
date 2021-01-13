#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#Print welcome message
print("Welcome to the tip calculator.")

#Stores user inputs in variables
total_bill = input("What was the total bill? ")
percentage_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
number_of_person = input("How many people to split the bill? ")

#Casts variables as numbers
total_bill = float(total_bill)
percentage_tip = float(percentage_tip)
number_of_person = int(number_of_person)

#Computes the amount each person should pay
bill_per_person = round((total_bill / number_of_person) * (1 + percentage_tip / 100), 2)

#Prints the result
print(f"Each person should pay: ${bill_per_person}")
