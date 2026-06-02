# --- Iteration 1: The bulky if/elif chain ---
'''
name = input("What's your name? ")

if name == "Rohan" or name == "Sourav" or name == "Sarabjeet":
    print("Shivalik")
elif name == "Anoop":
    print("Udaygiri")
elif name == "Devansh":
    print("Aravali")
else: 
    print("Who?")
'''

# --- Iteration 2: The clean match statement ---
name = input("Enter name: ")

match name:
    case "Rohan" | "Sarabjeet" | "Zaid":
        print("Shivalik")
    case "Sourav" | "Devansh" | "Aarif" | "Singh" | "Ron":
        print("Aravali")
    case _:
        print("Who?")