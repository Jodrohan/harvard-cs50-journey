"""
CS50P: Response Validation

Implement a program that prompts the user for an email address and then prints
"Valid" or "Invalid", respectively, if the input is a syntactically valid email address.

Constraints:
- You may not use the built-in `re` module.
- You must use a third-party library from PyPI (e.g., `validator-collection` or `validators`).
- Do not validate whether the email address's domain name actually exists, only its syntax.
"""

import validators


def main():

    email = input("What's email? ")

    if validator(email):
        print("Valid")
    else:
        print("Invalid")


def validator(s):
    s = s.strip().lower()
    is_valid = validators.email(s)

    if is_valid:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
