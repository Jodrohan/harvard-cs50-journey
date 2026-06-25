"""
Curve Calculator

A command-line utility that applies a flat bonus curve to student test scores.

Usage: 
    python curve.py [curve_amount]

Behavior:
    - Accepts a single integer argument representing the bonus points to add.
    - Continuously prompts the user to input student scores.
    - Automatically adds the curve and caps the maximum possible score at 100.
    - Pressing Control-D (EOF) exits the program and prints a final list 
      of all the curved scores entered during the session.
"""

import sys
def main():
  if len(sys.argv)!=2:
    sys.exit("Incorrect argument")
  else:
    try:
      curve = int(sys.argv[1])
    except ValueError:
      sys.exit("Argument is not an integer ")
  result_list = []
  while True:
    try:
      score = int(input("Score? "))
    except ValueError:
      continue
    except EOFError:
      print()
      sys.exit(f"Here is your list of final result: {result_list} ")
    else:
      result = apply_curve(curve, score)
      print(result)
      result_list.append(result)
      
def apply_curve(curve, score):
  result = score + curve
  if result > 100:
    result = 100
    return result
  else:
    return result
if __name__ == "__main__":
  main()