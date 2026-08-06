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

class Spell:
    def __init__(self, name, category):
        self.name = name
        # This automatically uses the setter below to check the category
        self.category = category  
        
    def __str__(self):
        # How the spell looks when we print it
        return f"{self.name} (Category: {self.category})"
        
    @property
    def category(self):
        # Get the hidden category variable
        return self._category
        
    @category.setter
    def category(self, value):
        # Make sure it's a valid spell type before saving it
        if value not in ["Charm", "Curse", "Hex"]:
            raise ValueError("Invalid category")
        self._category = value


# Test the code
s = Spell("Lumos", "Charm")
print(s)

# Change the category to test the setter
s.category = "Hex"
print(s)