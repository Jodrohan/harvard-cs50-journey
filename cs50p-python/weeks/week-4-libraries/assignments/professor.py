"""
CS50P Week 4 - Little Professor

One of the first educational toys was Little Professor, a "reverse calculator" that generated math problems for children to solve.

In a file called professor.py, implement a program that:
1. Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
2. Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. No need to support operations other than addition (+).
3. Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
4. The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
"""

import random

def main():
    score = 0
    level = get_level()
    for i in range(1, 11):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = (x + y)
        for attempt in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    continue
            except ValueError:
                print("EEE")
                pass
        else:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass
        

def generate_integer(level):

    if level not in [1, 2, 3]:
        raise ValueError
    if level == 1:
        return random.randint(0, 9)
    
    min_val = 10**(level - 1)
    max_val = (10**level) - 1
    
    return random.randint(min_val, max_val)


if __name__ == "__main__":
    main()
