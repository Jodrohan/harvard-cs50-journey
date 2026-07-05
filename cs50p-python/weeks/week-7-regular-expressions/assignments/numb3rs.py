"""
================================================================================
CS50P WEEK 7 ASSIGNMENT 1: NUMB3RS
================================================================================

Description:
An IPv4 address is a numeric identifier used for network communication. It is 
typically formatted in dot-decimal notation as #.#.#.#, where each '#' represents 
an integer between 0 and 255, inclusive. For example, 127.0.0.1 and 255.255.255.255 
are valid, but 275.3.6.28 is out of range and therefore invalid.

Your task is to use regular expressions to validate user input against this format.

Requirements:
1. Primary Script (numb3rs.py):
    - Implement a function named `validate(ip)`.
    - `validate` must accept an IPv4 address as a string parameter.
    - `validate` must return `True` if the string is a valid IPv4 address, or 
      `False` if it is not.
    - You must prompt the user for an IPv4 address inside the `main()` function 
      and print the boolean result of your `validate` function.
    - Restrictions: You may only import the `re` and/or `sys` libraries.

2. Testing Script (test_numb3rs.py):
    - Implement two or more functions to thoroughly test `validate()`.
    - Every testing function must begin with `test_` so that `pytest` can discover 
      and execute them.
    - Ensure your tests check for correct formatting, out-of-range values, and 
      invalid characters.

Execution Example:
# Run the script using the python interpreter
$ python numb3rs.py
# The terminal prompts the user; user inputs an IP
IPv4 Address: 127.0.0.1
# The script evaluates the string and prints the boolean outcome
True
================================================================================
"""
import sys
import re
def main():
    ip = input("What's IP address? ")
    print(validate(ip))

def validate(ip):
    search = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",ip)
    if search:
        pieces = search.groups()
        for group in pieces:
            group = int(group)
            if group > 255:
                return False
        return True
    else:
        
        return False
if __name__ == "__main__":
    main()