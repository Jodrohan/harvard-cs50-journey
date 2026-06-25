import pytest
from curve import apply_curve

def test_positive():
    assert apply_curve(5, 3) == 8
def test_99():
    assert apply_curve(69, 99) == 100