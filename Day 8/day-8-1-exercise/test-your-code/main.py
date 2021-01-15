#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#Imports the ceil function from the math module
from math import ceil

#Defines the function paint_calc with 3 parameters : height of the wall, width of the wall and coverage
def paint_calc(height, width, cover):
  #Computes the number of cans needed
  cans_number = ceil(height * width / cover)

  #Prints the result
  print(f"You'll need {cans_number} cans of paint.")

#Write your code above this line 👆
    


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)














# Tests
import unittest
from unittest.mock import patch
from io import StringIO

class MyTest(unittest.TestCase):
# Testing Print output
    def test_1(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(3, 6, 5)
            expected_print = "You'll need 4 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print) 

    def test_2(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(3, 9, 5)
            expected_print = "You'll need 6 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_3(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(7, 9, 2)
            expected_print = "You'll need 32 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_4(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            paint_calc(12, 45, 5)
            expected_print = "You'll need 108 cans of paint.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)


print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)