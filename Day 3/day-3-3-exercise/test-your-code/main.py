# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#Test if the year is evenly divisible by 100
if year % 100 == 0:
  #Tests if the year is evenly divisible by 400
  if year % 400 == 0:
    #The year is both evenly divisible by 100 and 400 -> leap year
    print("Leap year.")
  else:
    #The year is evenly divisible by 100 but not by 400 -> not leap year
    print("Not leap year.")
#Tests if the year is evenly divisible by 4
elif year % 4 == 0:
  #The year isn't evenly divisible by 100 but is evenly divisible by 4 -> leap year
  print("Leap year.")
else:
  #The year isn't evenly divisible neither by 100 nor 4 -> not leap year
  print("Not leap year.")







































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
    with patch('builtins.input', return_value=given_answer), patch('sys.stdout', new=StringIO()) as fake_out: 
      testing_copy.test_func()
      self.assertEqual(fake_out.getvalue(), expected_print) 

  def test_1(self):
    self.run_test(given_answer='2016', expected_print='Leap year.\n')

  def test_2(self):
    self.run_test(given_answer='2018', expected_print='Not leap year.\n')

  def test_3(self):
    self.run_test(given_answer='1999', expected_print='Not leap year.\n')

  def test_4(self):
    self.run_test(given_answer='2020', expected_print='Leap year.\n')

  def test_5(self):
    self.run_test(given_answer='2000', expected_print='Leap year.\n')

  def test_6(self):
    self.run_test(given_answer='1900', expected_print='Not leap year.\n')


print("\n\n\n.\n.\n.")
print('Checking what your code prints for several different years.\nYour code needs to either print "Leap year." or "Not leap year." *exactly* (that includes the full stop).\n')
print('\nRunning some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py") 

