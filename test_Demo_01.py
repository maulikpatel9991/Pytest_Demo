# Pytest is a testing framework based on python.
# Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
# Pytest is free and open source.
# Running pytest without mentioning a filename will run all files of format test_*.py or *_test.py
# Pytest assertions are checks that return either True or False status

import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*7 == 40

def tesequality():
   assert 10 == 11



#
# Q-1:-In a real scenario, we will have multiple test files and each file will have a number of tests. Tests will cover
# various modules and functionalities. Suppose, we want to run only a specific set of tests
#  Ans :- pytest -k <test_Name> -v