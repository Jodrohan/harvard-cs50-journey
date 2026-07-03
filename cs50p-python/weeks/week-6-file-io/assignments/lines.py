'''
Lines of Code

Goal:
Write a program that expects exactly one command-line argument (the name of a Python file) 
and prints the exact number of executable lines of code inside that file.

Error Handling (Use sys.exit):
1. If the user provides exactly zero arguments, exit.
2. If the user provides two or more arguments, exit.
3. If the provided file name does not end in ".py", exit.
4. If the file does not exist (FileNotFoundError), exit.

Counting Logic (What to ignore):
- Ignore blank lines: Do not count lines that are completely empty or only contain whitespace.
- Ignore comments: Do not count lines where the very first non-whitespace character is a hash (#).
- Note: You do not need to worry about ignoring block quotes/docstrings.
'''

import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
        
    if len(sys.argv) > 2:
        sys.exit("Too many argumnents")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")

    try:
        print(count_lines(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File dosen't exists")


def count_lines(filename):
    count = 0

    with open(filename) as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue
            
            if line.startswith("#"):

                continue
            
            count += 1

    return count


if __name__ == "__main__":
    main()