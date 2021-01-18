# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

num_1 = two_digit_number[0]
num_2 = two_digit_number[1]

print(int(num_1) + int(num_2))



































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
    self.run_test(given_answer='52', expected_print="7\n")

  def test_2(self):
    self.run_test(given_answer='92', expected_print="11\n")

  def test_3(self):
    self.run_test(given_answer='10', expected_print="1\n")


print("\n\n\n.\n.\n.")
print('Checking if your code prints the sum of the two numbers...')
print('Running some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py") 
