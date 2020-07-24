from src.com.example.calculator.calc_func import *

def test_adding():
    result = add(3,5)
    assert result == 8

def test_sustrating():
    assert sus(5,3) == 2

def test_multipling():
    assert multi(3,3) == 9