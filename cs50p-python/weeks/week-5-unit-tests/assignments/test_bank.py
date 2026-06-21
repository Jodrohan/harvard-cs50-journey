'''
Testing Back to the Bank

In a file called test_bank.py, implement three or more functions that collectively 
test your implementation of value thoroughly, each of whose names should begin 
with test_ so that you can execute your tests with:

pytest test_bank.py
'''
from bank import value
def test_hello():
    assert value("hello world") == 0
def test_h():
    assert value("he is the one") == 20
def test_otherwise():
    assert value("i am rohan") == 100
    
