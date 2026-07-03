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
import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        print(atomic_function(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("No such file")

def atomic_function(filename):
    with open(filename) as file:
        table_data = []
        reader = csv.reader(file)
        for row in reader:
            table_data.append(row)
        formatted_result = tabulate(table_data, headers="firstrow", tablefmt="grid")
        return formatted_result
if __name__ == "__main__":
    main()
