"""
PRACTICE CHALLENGE: THE SPELL BOOK

Create a class called 'Spell'.
1. The __init__ method should take two arguments: 'name' (str) and 'category' (str).
2. Implement the __str__ method so that printing a Spell object returns exactly:
   "{name} (Category: {category})"
3. Use the @property decorator to create a getter for 'category'.
4. Create a setter for 'category' that validates the input. It must raise a 
   ValueError("Invalid category") if the category is not exactly "Charm", "Curse", or "Hex".
   
Example Usage:
    s = Spell("Lumos", "Charm")
    print(s)             # Expected Output: Lumos (Category: Charm)
    s.category = "Hex"   # This should update successfully
    s.category = "Jinx"  # This should raise ValueError: Invalid category
"""
