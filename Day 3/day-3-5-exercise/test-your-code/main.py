# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

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





















































#Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇


with open('testing_copy.py', 'w') as file:
  file.write('def test_func():\n')
  with open('main.py', 'r') as original:
    f2 = original.readlines()[0:60]
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
    self.run_test(given_answer=['David Beckham', 'Victoria Beckham'], expected_print='Welcome to the Love Calculator!\nYour score is 45, you are alright together.\n')

  def test_2(self):
    self.run_test(given_answer=['Han Solo', 'Princess Leia Organa'], expected_print='Welcome to the Love Calculator!\nYour score is 47, you are alright together.\n')

  def test_3(self):
    self.run_test(given_answer=['Pierre Curie', 'Marie Curie'], expected_print='Welcome to the Love Calculator!\nYour score is 125, you go together like coke and mentos.\n')

  def test_4(self):
    self.run_test(given_answer=['Mark Antony', 'Cleopatra'], expected_print='Welcome to the Love Calculator!\nYour score is 54.\n')


print('\n\n\n.\n.\n.')
print('Checking if your print statements match the instructions. \nFor "Mario" and "Princess Peach" your program should print this line *exactly*:\n')
print('Your score is 43, you are alright together.\n')
print('\nRunning some tests on your code with different name combinations:')
print('.\n.\n.')
unittest.main(verbosity=1, exit=False)

os.remove('testing_copy.py') 
