student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

#Creates the dictionary that will contian students' grades
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

#Going through all students in students_scores dictionary
for student in student_scores:
  #Retrieving current student's score
  student_score = student_scores[student]

  #Creating variable that will contain student grade
  student_grade = ""

  #Tests student's score and assign matching grade
  if student_score <= 70:
    #Student's score is below or equal to 70, grade is "Fail"
    student_grade = "Fail"
  elif student_score <= 80:
    #Student's score is between 71 and 80, grade is "Acceptable"
    student_grade = "Acceptable"
  elif student_score <= 90:
    #Student's score is between 81 and 90, grade is "Exceeds Expectations"
    student_grade = "Exceeds Expectations"
  elif student_score <= 100:
    #Student's score is between 91 and 100, grade is "Outstanding"
    student_grade = "Outstanding"
  else:
    #Student's score is over 100, it is an error
    student_grade = "Error"

  #Studen'ts grade is added to the dicrionary containing grades
  student_grades[student] = student_grade   
    
# 🚨 Don't change the code below 👇
print(student_grades)