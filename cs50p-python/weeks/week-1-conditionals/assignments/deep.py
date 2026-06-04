"""
Problem Set 1: Deep Thought (deep.py)

The Goal: 
Prompt the user for the answer to the Great Question of Life, the Universe, and Everything.

The Rules:
1. Ask the user for input.
2. If the user types exactly "42", "forty-two", or "forty two", print "Yes".
3. If they type anything else, print "No".
"""



answer = input("Whats the answer of the question : ").strip().lower()

if answer == "42" or  answer == "forty-two" or answer =="forty two":
    print("Yes")
else:
    print("No")
