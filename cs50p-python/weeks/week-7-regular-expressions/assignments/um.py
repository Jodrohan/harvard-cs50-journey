"""
Regular, um, Expressions

Implement a function called count that expects a line of text as input as a str
and returns, as an int, the number of times that "um" appears in that text,
case-insensitively, as a word unto itself, not as a substring of some other word.

For instance:
- count("hello, um, world") should return 1
- count("yummy") should return 0
- count("UM, what are you doing?") should return 1

Structure:
- um.py must contain the main function and the count function.
- test_um.py must contain test functions (e.g., test_single_um, test_word_with_um_in_it)
  to rigorously test the count function using pytest.
"""

import re


def main():
    user_input = input("What's string? ")
    print(count(user_input))


def count(s):
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
