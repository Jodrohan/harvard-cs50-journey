'''
In a file called test_plates.py, implement four or more functions that 
collectively test your implementation of is_valid thoroughly, each of 
whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py
'''
from plates import is_valid

def test_length():
    
    assert is_valid("CS") == True
    assert is_valid("CS5050") == True
    assert is_valid("C") == False
    assert is_valid("CS50505") == False

def test_starts_with_two_letters():
    
    assert is_valid("BA") == True
    assert is_valid("22") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_number_placement():
    
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_punctuation():
    
    assert is_valid("PI3.14") == False
    assert is_valid("PI 14") == False
    assert is_valid("PI!14") == False