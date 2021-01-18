# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")



























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
    self.run_test(given_answer='53', expected_print='You have 13505 days, 1924 weeks, and 444 months left.\n')

  def test_2(self):
    self.run_test(given_answer='12', expected_print="You have 28470 days, 4056 weeks, and 936 months left.\n")

  def test_3(self):
    self.run_test(given_answer='90', expected_print='You have 0 days, 0 weeks, and 0 months left.\n')


print("\n\n\n.\n.\n.")
print('Checking what your code prints for several different ages.\nFor an age of 56 it should read this *exactly*:\n')
print('You have 12410 days, 1768 weeks, and 408 months left.')
print('\nRunning some tests on your code:')
print(".\n.\n.")
unittest.main(verbosity=1, exit=False)

os.remove("testing_copy.py") 

