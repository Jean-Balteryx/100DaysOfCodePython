student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#TODO-1: Create an empty dictionary called student_grades.

#Creates the dictionary that will contian students' grades
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

#Going through all keys in students_scores dictionary
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

#🚨 Don't change the code below 👇
print(student_grades)








































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:40]
    for x in f2:
      file.write("    " + x)

with open('testing_copy_2.py', 'w') as file:
  file.write('student_scores = {"Harry": 41, "Ron": 91, "Hermione": 89, "Draco": 69,"Neville": 71}\n\n')
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[8:40]
    for x in f2:
      file.write("    " + x)

import testing_copy
import testing_copy_2

import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def test_1(self): 
    with patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      expected_print = "{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_2(self): 
    with patch('sys.stdout', new=StringIO()) as fake_out:
      testing_copy_2.test_func()
      expected_print = "{'Harry': 'Fail', 'Ron': 'Outstanding', 'Hermione': 'Exceeds Expectations', 'Draco': 'Fail', 'Neville': 'Acceptable'}\n"
      self.assertEqual(fake_out.getvalue(), expected_print) 


print('\n\n\n.\n.\n.')
print('Checking if what you printed matches the target output for two different dictionaries...')
print('Running some tests on your code:')
print('.\n.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 
os.remove('testing_copy_2.py') 