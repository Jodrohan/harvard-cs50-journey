"""
CS50P Week 6 - File I/O
Assignment 3: Scourgify

Objective:
Read an existing CSV of students, reformat their names, and write them to a new CSV.

Execution Rule:
- The user must execute the script with exactly two command-line arguments:
  1. The name of the input file (e.g., before.csv)
  2. The name of the output file (e.g., after.csv)

Validation Logic:
- If the user provides too few or too many arguments, exit via sys.exit("Too few command-line arguments") or ("Too many command-line arguments").
- If the input file cannot be read, exit via sys.exit(f"Could not read {sys.argv[1]}").

Data Processing Pipeline:
- Open the input CSV using csv.DictReader.
- The input format has two columns: "name" (formatted as "Last, First") and "house".
- Split the "name" column into two separate variables: a first name and a last name.
- Open the output CSV using csv.DictWriter.
- Write the cleaned data into the output file with three distinct columns: "first", "last", and "house".
"""
import csv
import sys

def main():
    try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        if not sys.argv[1].endswith(".csv"):
            sys.exit(f"Could not read {sys.argv[1]}")
        if not sys.argv[2].endswith(".csv"):
            sys.exit(f"Could not write {sys.argv[1]}")
        else:
            new_csv(sys.argv[1],sys.argv[2])

    except FileNotFoundError:
        sys.exit("No such file in the directory")
def new_csv(input_file,output_file):
    with open(input_file) as inputf, open(output_file, "w") as outputf:
        reader = csv.DictReader(inputf)
        writer = csv.DictWriter(outputf,fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last, first = row["name"].split(",")
            writer.writerow({
                "first" : first.strip(),
                "last" : last.strip(),
                "house" : row["house"]
            })
if __name__ == "__main__":
    main()