"""
CS50P Week 4 - Guessing Game

I’m thinking of a number between 1 and 100... What is it?

In a file called game.py, implement a program that:
1. Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
2. Randomly generates an integer between 1 and n, inclusive, using the random module.
3. Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
4. If the guess is smaller than that integer, the program should output "Too small!" and prompt the user again.
5. If the guess is larger than that integer, the program should output "Too large!" and prompt the user again.
6. If the guess is the same as that integer, the program should output "Just right!" and exit.

Example Execution:
$ python game.py
Level: cat
Level: -1
Level: 10
Guess: cat
Guess: -1
Guess: 5
Too small!
Guess: 8
Too large!
Guess: 7
Just right!

Hints:
- You will need to `import random`.
- Look into the `random.randint(a, b)` method in the Python documentation to generate the secret number.
- You will need to use `try` and `except ValueError:` to catch scenarios where the user types letters instead of numbers.
"""

import random
def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            pass
    random_number = random.randint(1,n)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
        except ValueError:
            pass
        else:  
            if guess < random_number:
                print("Too small!")
                continue
            elif guess > random_number:
                print("Too large!")
                continue
            else:
                print("Just right!")
            break
if __name__ == "__main__":
    main()