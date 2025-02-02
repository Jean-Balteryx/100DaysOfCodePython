#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#Prints first line
print("Day 1 - String Manipulation")
#Prints second line
print('String Concatenation is done with the '+'"+" sign.')
#Prints third line
print('e.g. print("Hello " + "world")')
#Prints fourth line
print("New lines can be created with a backslash and n.")
























#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇

with open("testing_copy.py", "w") as file:
  file.write("def test_func():\n")
  with open("main.py", "r") as original:
    f2 = original.readlines()[0:30]
    for x in f2:
      file.write("    " + x)


import testing_copy
import unittest
from unittest.mock import patch
from io import StringIO
import os

class MyTest(unittest.TestCase):
  def test_1(self): 
    with patch('sys.stdout', new = StringIO()) as fake_out: 
      testing_copy.test_func()
      expected_print = 'Day 1 - String Manipulation\nString Concatenation is done with the "+" sign.\ne.g. print("Hello " + "world")\nNew lines can be created with a backslash and n.\n'
      self.assertEqual(fake_out.getvalue(), expected_print) 

print("\n\n\n.\n.\n.")
print('Checking if what you printed matches the target output *exactly*...')
print('Running some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py") 


