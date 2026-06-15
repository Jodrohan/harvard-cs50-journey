'''
CS50P Week 4 - Frank, Ian and Glen's Letters

FIGlet, named after Frank, Ian, and Glen's letters, is a program from the early 1990s 
for making large letters out of ordinary text, a form of ASCII art.

In a file called figlet.py, implement a program that:
- Expects zero or two command-line arguments:
    - Zero if the user would like to output text in a random font.
    - Two if the user would like to output text in a specific font, in which case 
      the first of the two should be -f or --font, and the second should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font, 
or the second is not the name of a font, the program should exit via sys.exit with an error message.

Example Execution:
$ python figlet.py
Input: hello
(Outputs "hello" in a random font)

$ python figlet.py -f slant
Input: hello
(Outputs "hello" in the 'slant' font)

$ python figlet.py -f invalid_font
Invalid usage

Hints:
- You will need to install the 'pyfiglet' package from PyPI.
- You can get a list of available fonts with:
  from pyfiglet import Figlet
  figlet = Figlet()
  figlet.getFonts()
'''
import sys
import random
from pyfiglet import Figlet


def main():
   
    figlet = Figlet()
    valid_fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        random_font = random.choice(valid_fonts)
        figlet.setFont(font=random_font)
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        if sys.argv[2] not in valid_fonts:
            sys.exit("Invalid usage")
        figlet.setFont(font= sys.argv[2])
    else:
        sys.exit("Invalid usage")
    
    user_input = input("Input: ")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()