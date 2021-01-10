# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

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
































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇


with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:40]
    for x in f2:
      file.write("    " + x)


import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def run_test(self, given_answer, expected_print):
    with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_1(self):
    self.run_test(given_answer=['1.7', '75'], expected_print='Your BMI is 26, you are slightly overweight.\n')

  def test_2(self):
    self.run_test(given_answer=['1.5', '65'], expected_print='Your BMI is 29, you are slightly overweight.\n')

  def test_3(self):
    self.run_test(given_answer=['1.5', '51'], expected_print='Your BMI is 23, you have a normal weight.\n')


print('\n\n\n.\n.\n.')
print('Checking if your print statements match the instructions: \n For 1.7m and 75kg it should print this line *exactly*:\n')
print('Your BMI is 26, you are slightly overweight.')
print('\nRunning some tests on your code with different combinations for height and weight:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 

