'''
MICRO-CHALLENGE: THE VAULT DOOR (V2 - ARCHITECT EDITION)
Write a script that acts as a security system using Week 1 concepts.

1. Ask the user: "Enter clearance level (admin/user/guest): "

2. Use a `match` statement to handle the clearance level:
    - "admin" -> print("Full system access.")
    - "user" -> print("Limited system access.")
    - "guest" -> print("Read-only access.")
    - Anything else -> print("Intruder detected.") AND STOP THE PROGRAM IMMEDIATELY.

3. THE ARCHITECT UPGRADE: 
    - ONLY ask the user: "Enter your 4-digit PIN: " (and convert it to an int) IF they passed step 2. 
    - If they are an intruder, the program must terminate before this question is ever asked.

4. Create a helper function called `is_even(n)`:
    - It must take the PIN as an argument.
    - It must return the Boolean `True` if it is even, and `False` if it is odd. (Use your Pythonic method!)

5. Evaluate the PIN:
    - Pass the PIN into your `is_even` function.
    - If True -> print("PIN accepted. Vault open.")
    - If False -> print("PIN rejected. Vault locked.")

Constraints:
- You MUST use a `match` statement.
- You MUST use a helper function that returns `True` or `False`.
- NO GOOGLING. NO PEEKING AT NOTES.
'''

def main():
    clearance_level = input("Enter clearance level (admin/user/guest): ")
    match clearance_level:
        case "admin":
            print("full system access: ")
        case "user":
            print("limited system access: ")
        case "guest":
            print("Read-only access: ")
        case _:
            print("Intruder detected: ")
            return

    pin = (input("Enter your 4 digit pin: "))
    if is_even(pin):
        print("Pin accepted. Vault open: ")
    else:
        print("Pin rejected. Vault Locked: ")


   

def is_even(check):
    check = int(check)
    return check % 2 == 0

if __name__ == "__main__":
    main()

    
  









