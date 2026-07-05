"""
Assignment 3: Working 9 to 5

Objective:
Parse strings representing a time range in 12-hour format and convert them 
to a 24-hour format using regular expressions.

Requirements:
1. Define a function `convert(s)` that expects a string containing a 12-hour time range.
2. Acceptable input structures:
   - "9:00 AM to 5:00 PM"
   - "9 AM to 5 PM"
   - "10:30 PM to 8:50 AM"
3. Output the equivalent 24-hour format time range exactly as: "09:00 to 17:00".
4. Utilize the `re` module to validate the format and extract time components.
5. Raise a `ValueError` if the input string does not match the required structural format.
6. Raise a `ValueError` if extracted times are out of bounds (hours > 12, minutes >= 60).
7. Include a `main` function to prompt for input, call `convert`, and print the result.
"""
import re
import sys


def main():
    try:
        time = input("Hours: ").strip()
    except EOFError:
        sys.exit("Program Revoked")
        
    try:
        print(convert(time))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    match = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$", s)
    
    if not match:
        raise ValueError
        
    start_hour = match.group(1)
    start_minute = match.group(2)
    start_ampm = match.group(3)
    
    end_hour = match.group(4)
    end_minute = match.group(5)
    end_ampm = match.group(6)

    if start_minute == None:
        start_minute = "00"
    if end_minute == None:
        end_minute = "00"

    if int(start_hour) > 12 or int(start_minute) >= 60:
        raise ValueError
    if int(end_hour) > 12 or int(end_minute) >= 60:
        raise ValueError

    start_hour = int(start_hour)
    if start_ampm == "PM" and start_hour != 12:
        start_hour += 12
    elif start_ampm == "AM" and start_hour == 12:
        start_hour = 0

    end_hour = int(end_hour)
    if end_ampm == "PM" and end_hour != 12:
        end_hour += 12
    elif end_ampm == "AM" and end_hour == 12:
        end_hour = 0

    return f"{start_hour:02}:{start_minute} to {end_hour:02}:{end_minute}"


if __name__ == "__main__":
    main()