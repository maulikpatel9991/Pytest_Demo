# pytest test_failure.py -v --maxfail 1
# pytest runs tests in sequential order.
# pytest test_multiplication.py -v --junitxml="result.xml"
# pytest -n 3 == parallel run pytest
import pytest
import math

def test_sqrt_failure():
   num = 25
   assert math.sqrt(num) == 6

def test_square_failure():
   num = 7
   assert 7*7 == 40

def test_equality_failure():
   assert 10 == 11