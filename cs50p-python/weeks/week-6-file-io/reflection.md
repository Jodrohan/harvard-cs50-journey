# Reflection

## What I learned
How to safely open and read files in Python using `with open(...)` so they close automatically. I also learned how to read CSV files using `csv.reader` (which gives data as lists) and `csv.DictReader` (which gives data as dictionaries, making it easy to look up values by column name).

## What confused me
Dealing with extra blank lines because Python keeps the invisible `\n` (newline) character at the end of every line. Also, understanding how `DictReader` automatically uses the first row of the file as the keys for the dictionary.

## Mistakes I made
Trying to read and write to the exact same file at the exact same time, which accidentally wiped out my data. Also, I forgot to use Linux terminal commands like `cat` to peek at my files before running the Python script.

## Next action
Practice reading messier CSV files. Create a new Git branch for my next coding lab. Make sure my git commits use clear action words (like `feat: add file reading logic`).