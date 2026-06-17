'''
Log File Analyzer (Week 4 Syllabus Version)
1. Accept a filename as a command-line argument using sys.argv.
2. If the user doesn't provide a filename, use sys.exit() to exit.
3. Open the file manually using file = open(filename, "r").
4. Count how many lines contain the string "ERROR".
5. Close the file manually using file.close().
6. Print the total count.
7. Wrap the open/read process in a try...except FileNotFoundError block.

Pseudo-code:
    - IMPORT sys
    - TRY to get filename from sys.argv
    - IF filename missing, EXIT
    - TRY:
        - file = open(filename, "r")
        - INITIALIZE counter = 0
        - FOR each line in file:
            - IF "ERROR" in line:
                - INCREMENT counter
        - PRINT counter
        - file.close()
    - CATCH FileNotFoundError: PRINT message, EXIT
'''

import sys
def main():
    counter = 0
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("No file name entered: ")
        sys.exit()

    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("No such file in the system")
        sys.exit()

    else:
        for line in file:
            if "ERROR" in line:
                counter += 1
        file.close()
        print(counter)
if __name__ == "__main__":
    main()





    

