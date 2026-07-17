"""
Task 1: The Pokedex Entry
-------------------------
Background: You are building a simple database to track Pokémon.
Your goal is to define a blueprint (class) for individual entries.

Instructions:
1. Define a class named `Pokemon`.
2. Implement the `__init__` method to accept `name` (str) and `type_` (str).
3. Add validation: If `name` or `type_` is an empty string, raise a ValueError.
4. Implement the `__str__` method so that printing the object returns 
   the format: "Name (Type Type)" -> e.g., "Pikachu (Electric Type)".

Test your code by instantiating a valid Pokémon and printing it, 
then try instantiating one with an empty name to see if your ValueError works.
"""

class Pokemon:
    def __init__(self, name, type_):
        if not name or not type_:
            raise ValueError("Name and type cannot be empty")
            
        self.name = name
        self.type_ = type_

    def __str__(self):
        return f"{self.name} ({self.type_} Type)"


def main():
    pikachu = Pokemon("Pikachu", "Electric")
    print(pikachu)

    try:
        Pokemon("", "Water")
    except ValueError as e:
        print(f"Validation successful: {e}")


if __name__ == "__main__":
    main()