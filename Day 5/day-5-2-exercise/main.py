# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#Initializes the variable that contains the highest score
highest_score = student_scores[0]

#Goes through all scores
for score in student_scores:
  #Tests if the current highest score is less than the current score
  if highest_score < score:
    #The current score becomes the new highest score
    highest_score = score
  
#Prints the highest score
print(f"The highest score in the class is: {highest_score}")