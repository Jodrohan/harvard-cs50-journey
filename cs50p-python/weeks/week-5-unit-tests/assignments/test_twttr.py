'''
In a file called test_twttr.py, implement one or more functions that 
collectively test your implementation of shorten thoroughly, each of whose 
names should begin with test_ so that you can execute your tests with:

pytest test_twttr.py
'''
from twttr import shorten
def test_whole_vowels():
    assert shorten("aeiou") == ""
def test_upper():
    assert shorten("IamirOnman") == "mrnmn"
def test_consonents():
    assert shorten("roaeiou") == "r"
def test_spaces():
    assert shorten("is it working") == "s t wrkng"
def test_numbers_and_symbols():
    assert shorten("CS50p!") == "CS50p!"
    