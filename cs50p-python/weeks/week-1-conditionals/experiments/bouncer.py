'''
MICRO-CHALLENGE: THE AUTOMATED BOUNCER
Write a script that does the following:

1. Ask the user: "Enter your age: "
2. Ask the user: "Do you have a VIP pass? (yes/no): "

Logic Requirements:
- If under 18 AND does NOT have a VIP pass -> print("Access Denied")
- If under 18 AND DOES have a VIP pass -> print("VIP Access Granted")
- If 18 or older -> print("Standard Access Granted")

Constraints:
- You must handle sloppy input for the VIP question (e.g., "  YES  ", "yEs", "no ").
- You must use if, elif, and else.
- No helper functions or def main() needed.
- NO GOOGLING. NO LOOKING AT PAST CODE.
'''

age = int(input("Enter  your age: "))

vip = input("Do you have a vip pass? (yes/no): ").strip().lower()
if age >= 18:
    print("Standard Access Granted")
elif age < 18 and vip == "yes":
    print("VIP Access Granted")
else:
    print("Access Denied")


