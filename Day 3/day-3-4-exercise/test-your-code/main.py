# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

#Initializes the bill
bill = 0

#Tests the size input by the user
if size == "S":
  #The user wants a S size pizza that costs $15
  bill += 15
elif size == "M":
  #The user wants a M size pizza that costs $20
  bill += 20
else:
  #The user wants a L size pizza that costs $25
  bill += 25

#Tests if the user wants pepperoni
if add_pepperoni == "Y":
  #The user wants pepperoni so now it tests the size of the pizza
  if size == "S":
    #The pizza is an S size so the option costs $2
    bill += 2
  else:
    #The pizza is either a M or L size pizza so the option costs $3
    bill += 3

#Tests if the user wants extra cheese
if extra_cheese == "Y":
  #The user wants extra cheese that costs $1
  bill += 1

#Prints the final bill of the user
print(f"Your final bill is: ${bill}.")

































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
    self.run_test(given_answer=['S', 'N', 'Y'], expected_print='Welcome to Python Pizza Deliveries!\nYour final bill is: $16.\n')

  def test_2(self):
    self.run_test(given_answer=['L', 'N', 'N'], expected_print='Welcome to Python Pizza Deliveries!\nYour final bill is: $25.\n')

  def test_3(self):
    self.run_test(given_answer=['M', 'Y', 'N'], expected_print='Welcome to Python Pizza Deliveries!\nYour final bill is: $23.\n')


print('\n\n\n.\n.\n.')
print('Checking if your print statements match the instructions. \nFor a small pepperoni pizza with extra cheese your program should print this line *exactly*:\n')
print('Your final bill is: $18.\n')
print('\nRunning some tests on your code with different pizza combinations:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 
