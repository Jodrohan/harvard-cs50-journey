# --- Iteration 1: The basic inline check ---
'''
number = int(input("Enter the number: "))

if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
'''

# --- Iteration 2: The Pythonic functional approach ---
def main():
    x = int(input("Enter number: "))
    
    if is_even(x):
        print("Even")
    else:
        print("Odd")
 
def is_even(n):
    # Elegantly returns True or False directly based on the math
    return n % 2 == 0

main()