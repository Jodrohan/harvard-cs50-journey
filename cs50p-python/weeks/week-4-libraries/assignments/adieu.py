'''
CS50P Week 4 - Adieu, Adieu

In The Sound of Music, there is a song sung largely by the von Trapp children,
"So Long, Farewell". Therein do they say goodbye to their family and guests:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn't grammatically correct, since it would typically be written
(with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, "yieu" isn't even a word; it just rhymes with "you"!

In a file called adieu.py, implement a program that:
- Prompts the user for names, one per line, until the user inputs control-d (EOF).
- Assumes that the user will input at least one name.
- Bids adieu to those names, separating two names with one 'and', three names 
  with two commas and one 'and', and n names with n-1 commas and one 'and'.

Example Execution:
$ python adieu.py
Name: Liesl
Adieu, adieu, to Liesl

$ python adieu.py
Name: Liesl
Name: Friedrich
Name: Louisa
Adieu, adieu, to Liesl, Friedrich, and Louisa

Hints:
- You will need to install the 'inflect' package from PyPI.
- You can read the documentation to find how to join a list of words into 
  a properly formatted English string.
'''
import inflect

def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break
    formatted_name = p.join(names)
    print(f"Adieu, adieu, to {formatted_name}")


if __name__ == "__main__":
    main()