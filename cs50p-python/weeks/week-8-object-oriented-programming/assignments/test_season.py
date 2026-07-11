import pytest
from datetime import date
from seasons import get_dob, format_words

def test_get_dob():
    assert get_dob("1999-01-01") == date(1999, 1, 1)
    with pytest.raises(SystemExit):
        get_dob("January 1, 1999")
    with pytest.raises(SystemExit):
        get_dob("1999/01/01")

def test_format_words():
    assert format_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert format_words(1051200) == "One million, fifty-one thousand, two hundred"