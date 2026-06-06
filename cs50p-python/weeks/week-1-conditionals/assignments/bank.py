"""
Problem Set 2: Home Federal Savings Bank (bank.py)

The Goal:
Prompt the user for a greeting and calculate how much money you owe them based on Seinfeld's rules.

The Rules:
1. Ask the user for a greeting.
2. If the greeting starts with "hello", output: $0
3. If the greeting starts with an "h" (but not "hello"), output: $20
4. If the greeting starts with anything else, output: $100
5. Ignore any leading whitespace in the user's input, and treat it case-insensitively.
"""

greeting = input("Greetings: ").lower().strip()
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("100")


