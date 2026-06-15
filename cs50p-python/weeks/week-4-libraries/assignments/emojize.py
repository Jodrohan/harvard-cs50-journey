'''
CS50P Week 4 - Emojize

Because emoji aren't quite as easy to type as text, at least on standard keyboards, 
some programs support "codes," whereby you can type, for instance, :thumbs_up:, 
which will magically convert to 👍.

In a file called emojize.py, implement a program that prompts the user for a str in English 
and then outputs the "emojized" version of that str, converting any codes (or aliases) 
therein to their corresponding emoji.

Example Execution:
$ python emojize.py
Input: :thumbs_up:
Output: 👍

$ python emojize.py
Input: hello, :earth_asia:
Output: hello, 🌏

Hints:
- You will need to install and import the third-party 'emoji' package from PyPI.
- Read the official documentation for the emoji.emojize() function.
- Pay special attention to the 'language' parameter in the documentation to ensure aliases like :earth_asia: work properly!
'''

import emoji
def main():
    user_input = input("Input: ")
    output = emoji.emojize(user_input, language = "alias")
    print(f"Output: {output}")

if __name__ == "__main__":
    main()
