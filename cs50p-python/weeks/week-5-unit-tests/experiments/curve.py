'''
Problem: Grade Curver (CS50P Weeks 0-5 Comprehensive Challenge)

Description:
Professors often apply a "curve" to exam scores by adding a set number of points 
to everyone's grade. Your goal is to write a program that takes a curve amount 
from the command line, continuously asks the user for test scores, and outputs 
the newly curved score.

Requirements for curve.py:
1. Command-Line Arguments (Week 4):
   - Import the `sys` module. 
   - Accept exactly one command-line argument: an integer representing the curve 
     amount (e.g., `python curve.py 5`).
   - If the user provides no arguments, too many arguments, or if the argument 
     is not a valid integer, exit cleanly using `sys.exit` with a clear error message.

2. Functions and Conditionals (Week 0 & Week 1):
   - Structure your program with a `main()` function and a second function 
     called `apply_curve(score, curve_amount)`.
   - `apply_curve` should add the curve amount to the score and return the result. 
   - A test score can never exceed 100. If the curved score goes above 100, 
     the function must return exactly 100.

3. Loops and Exceptions (Week 2 & Week 3):
   - In `main()`, use an infinite loop to continuously prompt the user for "Score: ".
   - If the user inputs text that cannot be converted to an integer, catch the 
     `ValueError` and prompt them again.
   - Stop the loop when the user inputs `control-d` (which raises an `EOFError`). 
     Catch this exception, print a newline, and exit the program cleanly.

Requirements for test_curve.py (Week 5):
- Import your `apply_curve` function.
- Using `pytest`, write at least three distinct test functions to ensure 
  `apply_curve` works correctly. 
- Test standard curve scenarios, and edge cases (like a score hitting exactly 
  100, or going well over 100).
'''