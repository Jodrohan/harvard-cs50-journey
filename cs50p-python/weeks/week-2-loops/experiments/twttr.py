"""
Problem: Twttr
Implement a program that prompts the user for a string of text 
and then outputs that same text with all vowels (A, E, I, O, U) omitted.
"""


def main():
    text = ommited(input("Enter text :"))
    print(f"ommited text: {text}")

def ommited(o):
    result = ""
    for char in o:
        if char != "a" and char != "e" and char != "i" and char != "o" and char != "u" and \
           char != "A" and char != "E" and char != "I" and char != "O" and char != "U":
            result += char
    return result

main()