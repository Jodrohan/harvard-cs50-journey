"""
Seasons of Love (CS50P Week 8 - Object-Oriented Programming)

Implement a program that prompts the user for their date of birth in YYYY-MM-DD format.
Calculate and print how old they are in minutes, rounded to the nearest integer,
using English words instead of numerals.

Requirements:
- Prompt the user for a date of birth (YYYY-MM-DD).
- Use `datetime.date.today()` to determine the current date.
- Subtract the date of birth from the current date to find the difference in days.
- Convert the difference in days to total minutes (assuming 24 hours/day and 60 minutes/hour).
- Use the `inflect` library to convert the integer number of minutes into English words.
- Remove any " and " from the generated string (e.g., "Five hundred twenty-five thousand, six hundred minutes").
- Exit via `sys.exit("Invalid date")` if the user inputs an invalid date format.
- Structure your code with at least one function other than `main` to handle formatting or calculation.
- Include a test file `test_seasons.py` to test your functions (excluding `main`).
"""
import sys
from datetime import date
import inflect

p = inflect.engine()

def main():
    dob = get_dob(input("Date of Birth: "))
    today = date.today()
    minutes = calculate_minutes(dob, today)
    print(f"{format_words(minutes)} minutes")

def get_dob(s):
    try:
        return date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")

def calculate_minutes(dob, today):
    delta = today - dob
    return delta.days * 24 * 60

def format_words(minutes):
    words = p.number_to_words(minutes, andword="")
    return words.capitalize()

if __name__ == "__main__":
    main()