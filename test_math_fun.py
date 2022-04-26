import math_fun
import pytest

# @pytest.mark.skip(reason="do not run number")
# @pytest.mark.number  #Add Decorator
# def test_add1():
#     assert math_fun.add(7,3) == 10
#     assert math_fun.add(7) == 9

@pytest.mark.number  #Add Decorator
def test_add():
    assert math_fun.add(7,3) == 10
    assert math_fun.add(7) == 9

@pytest.mark.number  #Add Decorator
def test_product():
    assert math_fun.product(5,5) == 25
    assert math_fun.product(5) == 10

@pytest.mark.string   #Add Decorator
def test_add_strings():
    result = math_fun.add('Hello','world')
    assert result == 'Helloworld'


import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket



#Fixtures can request other fixtures

import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]





