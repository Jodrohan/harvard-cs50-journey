'''
File: chai.py

Trikuta Chai Stand Kiosk

Implement a program that enables a user to place an order at the
Trikuta Chai Stand. The program should continuously prompt the user
for an item, one per line, until the user inputs "Checkout".

Menu and Prices:
- Masala Chai: ₹20
- Kashmiri Kahwa: ₹50
- Samosa: ₹15
- Bread Pakora: ₹25
- Bun Maska: ₹30

Requirements:
1. Dictionary: Store the menu items and their corresponding prices 
   in a dictionary.
2. Functions: Structure your code by defining a main() function and 
   at least one custom helper function.
3. Input Handling: Treat user input case-insensitively and ignore any 
   leading or trailing whitespace. For example, "samosa", "SAMOSA", 
   and "  SamoSa " should all be treated as valid inputs.
4. Conditionals: If the user inputs an item that is not on the menu, 
   the program should simply ignore the input and prompt them again.
5. Loops: Keep a running total of the order cost as valid items are entered.
6. Termination: When the user inputs "Checkout" (also handled case-
   insensitively), print the final total formatted exactly as 
   "Total: ₹<amount>" and exit the program.
'''
def main():
    menu = {
        "masala chai" : 20,
        "kashmiri khawa" : 50,
        "samosa" : 15,
        "bread pakora": 25,
        "bun maska" : 30,
    }
    total = 0
    while True:
        user_input = input("What do you wanna do: 1) Order, 2) Checkout: ").strip().lower()
        if user_input == "1":
            total += make_order(menu)
        elif user_input == "2":
            checkout(total)
            break
        else:
            continue

def make_order(m):
    while True:
        user_choice = input("enter what you wanna order okay: ").strip().lower()
        if user_choice in m:
            print(f"{user_choice}, added to the order")
            return m[user_choice]
        else:
            continue

def checkout(c):
    print(f"Total: ₹{c}")
    return c



if __name__ == "__main__":
    main()