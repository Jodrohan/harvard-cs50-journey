'''
CS50P Week 6: Pizza Py

Goal:
Write a program that expects exactly one command-line argument (the name of a CSV file) 
and prints the data as a beautifully formatted ASCII art table using the `tabulate` library.

Error Handling (Use sys.exit):
1. If the user provides exactly zero arguments, exit.
2. If the user provides two or more arguments, exit.
3. If the provided file name does not end in ".csv", exit.
4. If the file does not exist (FileNotFoundError), exit.

Table Formatting Logic:
- Import the `csv` module to read the file data.
- Import the `tabulate` library to print the table (you will need to install it via terminal: `pip install tabulate`).
- The very first row of the CSV file must be used as the table's headers.
- The table must be printed using tabulate's "grid" format.
'''
import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            table = list(reader)

        print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()