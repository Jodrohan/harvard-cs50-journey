from um import count
import pytest

def test_single_um():
    assert count("um") == 1

def test_word_with_um_in_it():
    assert count("umbrella") == 0
    assert count("numbera") == 0

def test_multiple():
    assert count("Hey i am um um is the um of the um") == 4

def test_case_ins():
    assert count("Um is one of the goatest of the all time in the Um history of um in the house of targaryans of the  Um") == 4