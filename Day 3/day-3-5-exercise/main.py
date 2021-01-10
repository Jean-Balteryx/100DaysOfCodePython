# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Assembles both names and lowers the case
combined_names = (name1 + name2).lower()

#Counts the number of times the letters in the word TRUE occurs
true = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")
#Counts the number of times the letters in the word LOVE occurs
love = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")

#Computes the score appending both parts
score = int(str(true)+str(love))

#Test the score
if score < 10 or score > 90:
  #The score is either less than 10 or more than 90
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  #The score is between 40 and 50
  print(f"Your score is {score}, you are alright together.")
else:
  #The score is either between 10 and 39 or between 51 and 90
  print(f"Your score is {score}.")