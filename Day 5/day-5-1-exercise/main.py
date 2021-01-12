# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#Initializes variables that will store the count of students and the total height
students_count = 0
total_height = 0

#Goes through the list of heights
for height in student_heights:
  #Adds one to the count
  students_count += 1

  #Adds the height to the total
  total_height += height

#Computes the average height
avg_height = round(total_height / students_count)

#Prints the average height
print(avg_height)