"""
Problem Set 4: Math Interpreter (interpreter.py)

The Goal:
Build a program that prompts the user for an arithmetic expression and then calculates and outputs the result.

The Rules:
1. Prompt the user for an expression formatted as "x y z", where:
   - x is an integer
   - y is a math operator (+, -, *, /)
   - z is an integer
   (Example input: "1 + 1")
2. Assume the user will always format it correctly with spaces.
3. Calculate the math and print the result formatted as a float with exactly one decimal place.
   (Example output: 2.0)
"""

expression = input("Expression: ")
x, y, z= expression.split(" ")

x = int(x)
z = int(z)

if y == "+":
   print(float(x+z))
elif y == "-":
   print(float(x-z))
elif y == "*":
   print(float(x*z))
elif y == "/":
   print(float(round(x/z, 1)))
else:
   print("Expression is not in the database: ")