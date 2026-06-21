"""
test_fuel.py

A pytest suite designed to thoroughly test the convert and gauge 
functions from fuel.py, including checking for expected exceptions.
"""

from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("4/5") == 80
    assert convert("0/5") == 0
    assert convert("4/4") == 100
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(69) == "69%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
