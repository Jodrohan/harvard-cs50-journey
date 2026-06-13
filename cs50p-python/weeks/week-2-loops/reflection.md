# Reflection

## What I learned
- **Functions do NOT loop automatically.** If I want an action to repeat, I must explicitly build a `while` loop.
- **Dictionaries eliminate bad logic.** Using `if user_choice in menu:` instantly checks for valid inputs without writing messy, endless `if/elif` chains.
- **Return vs. Break:** `return` is the ultimate escape hatch—it immediately kills the function and throws data back to the caller. `break` only shatters the loop you are currently inside. 

## What confused me
- **Variable Scope and Data Flow:** I assumed that just calling `make_order()` would magically update my total. I didn't realize that when a function returns data, that data hits the floor and vanishes unless I explicitly set a variable to catch it.
- **Control Flow Keywords:** I tried to use `continue` inside a standard `if/else` block. It threw a `SyntaxError` because `continue` is strictly for loops, not for standard conditional branches.

## Mistakes I made
- **The Infinite State Bug:** I put the `input()` prompt *outside* my `while True` loop. The program saved the very first thing the user typed and infinitely processed it over and over because I never prompted them again inside the loop.
- **The Overwrite Bug:** I used `total =` instead of `total +=`. I completely wiped out the customer's previous total because I overwrote the variable instead of adding to it. 
- **The Action vs. Data Bug:** I tried to save a `print()` statement into a variable (`final_bill = print(...)`). `print()` just throws text on a screen; it does not hold data. It returns `None`, which broke the logic.
- **Impatience:** I got frustrated that this "simple" problem took me an hour. I need to accept that writing broken code and debugging it line-by-line is what programming actually is. 

## Next action
Stop expecting code to work on the first try. Move on to CS50P Week 3 (Exceptions) to learn how to explicitly catch and handle user errors instead of just looping around them.