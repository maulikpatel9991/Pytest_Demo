# Add Conftest file use fixture
# create confest file
#We can define the fixture functions in this file to make them accessible across multiple test files.
#use data

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0