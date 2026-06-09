# A list of dictionaries representing complex student data
students = [
    {"name": "Rohan", "house": "Shivalik", "colour": "Red"},
    {"name": "Anoop", "house": "Udaygiri", "colour": "Yellow"},
    {"name": "Abijeet", "house": "Aravali", "colour": "Blue"},
    {"name": "Asaf", "house": "Nilgiri", "colour": None}
]

# Iterating through the list of dictionaries
for student in students:
    print(student["name"], student["house"], student["colour"], sep=", ")

# --- PYTHONIC BONUS ---
# If you just had a standard dictionary:
simple_dict = {"Rohan": "Shivalik", "Anoop": "Udaygiri"}

# Using the .items() method to get both key and value cleanly!
for name, house in simple_dict.items():
    print(f"{name} is in {house}")