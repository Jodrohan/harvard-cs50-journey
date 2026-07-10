# CS50P Week 8: Object-Oriented Programming (OOP)

## Overview
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods). This week covers transitioning from procedural programming and basic data structures to defining custom types using classes, encapsulating data, and implementing inheritance.

---

## 1. The Limitations of Basic Data Structures
Before classes, data grouping relies on built-in types. Each has structural limitations when representing complex entities.

### 1.1 Tuples
Tuples group immutable data. Modifying a value requires reassigning the entire tuple.
```python
def main(): # Define the main execution function
    name, house = get_student() # Unpack the returned tuple into local variables
    print(f"{name} from {house}") # Print the formatted string to standard output

def get_student(): # Define the function to retrieve student data
    name = input("Name: ") # Prompt for and store the name string
    house = input("House: ") # Prompt for and store the house string
    return name, house # Return the data grouped as an immutable tuple

if __name__ == "__main__": # Verify if the script is executed directly
    main() # Call the main function
```

### 1.2 Lists
Lists allow mutation but lack semantic keys, making index-based access prone to errors.
```python
def main(): # Define the main execution function
    student = get_student() # Retrieve the student data list
    if student[0] == "Harry": # Check the value at integer index 0
        student[1] = "Gryffindor" # Mutate the value at integer index 1
    print(f"{student[0]} from {student[1]}") # Access and print values by index

def get_student(): # Define the function to retrieve student data
    name = input("Name: ") # Prompt for and store the name string
    house = input("House: ") # Prompt for and store the house string
    return [name, house] # Return the data grouped as a mutable list

if __name__ == "__main__": # Verify if the script is executed directly
    main() # Call the main function
```

### 1.3 Dictionaries
Dictionaries map keys to values, improving readability, but lack inherent structural validation mechanisms.
```python
def main(): # Define the main execution function
    student = get_student() # Retrieve the student data dictionary
    print(f"{student['name']} from {student['house']}") # Access values via string keys

def get_student(): # Define the function to retrieve student data
    name = input("Name: ") # Prompt for and store the name string
    house = input("House: ") # Prompt for and store the house string
    return {"name": name, "house": house} # Return the data as a key-value dictionary

if __name__ == "__main__": # Verify if the script is executed directly
    main() # Call the main function
```

---

## 2. Classes and Objects
A `class` is a blueprint for a custom data type. An `object` is an instance of a class. 

### 2.1 Initialization (`__init__`)
The `__init__` method initializes the object's state. `self` refers to the specific instance being created.
```python
class Student: # Define a new custom class named Student
    def __init__(self, name, house): # Define the initialization method with instance reference and parameters
        self.name = name # Create and assign the name instance variable
        self.house = house # Create and assign the house instance variable

def main(): # Define the main execution function
    student = get_student() # Instantiate a Student object and store in variable
    print(f"{student.name} from {student.house}") # Access instance variables using dot notation

def get_student(): # Define the function to instantiate a Student
    name = input("Name: ") # Prompt for and store the name string
    house = input("House: ") # Prompt for and store the house string
    return Student(name, house) # Return a newly instantiated Student object

if __name__ == "__main__": # Verify if the script is executed directly
    main() # Call the main function
```

### 2.2 String Representation (`__str__`)
The `__str__` method defines the string representation of an object, invoked automatically by functions like `print()`.
```python
class Student: # Define the Student class
    def __init__(self, name, house): # Define the initialization method
        self.name = name # Assign the name instance variable
        self.house = house # Assign the house instance variable

    def __str__(self): # Define the string representation method
        return f"{self.name} from {self.house}" # Return the formatted string representation

def main(): # Define the main execution function
    student = Student("Harry", "Gryffindor") # Instantiate a Student object directly
    print(student) # Print the object, automatically triggering the __str__ method
```

---

## 3. Encapsulation: Properties, Getters, and Setters
Properties prevent objects from entering an invalid state by intercepting attribute access and assignment.

*   **Getter:** Invoked when an attribute is accessed.
*   **Setter:** Invoked when an attribute is assigned, containing validation logic.

```python
class Student: # Define the Student class
    def __init__(self, name, house): # Define the initialization method
        self.name = name # Triggers the name setter method
        self.house = house # Triggers the house setter method

    @property # Decorator designating the following method as a getter
    def name(self): # Define the getter method for name
        return self._name # Return the internal, protected variable _name

    @name.setter # Decorator designating the following method as a setter for name
    def name(self, name): # Define the setter method for name
        if not name: # Check if the provided name string is empty
            raise ValueError("Missing name") # Raise a ValueError if validation fails
        self._name = name # Assign the validated value to the protected variable _name

    @property # Decorator designating the following method as a getter
    def house(self): # Define the getter method for house
        return self._house # Return the internal, protected variable _house

    @house.setter # Decorator designating the following method as a setter for house
    def house(self, house): # Define the setter method for house
        valid_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # Define allowed values
        if house not in valid_houses: # Check if the provided house is in the allowed list
            raise ValueError("Invalid house") # Raise a ValueError if validation fails
        self._house = house # Assign the validated value to the protected variable _house
```

---

## 4. Class Variables and Class Methods
*   **Class Variables:** Shared across all instances of a class.
*   **Class Methods (`@classmethod`):** Bound to the class itself, not instances. Often used as alternative constructors. `cls` represents the class.

```python
class Student: # Define the Student class
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # Define a class variable shared by all instances

    def __init__(self, name, house): # Define the initialization method
        self.name = name # Assign the name instance variable
        self.house = house # Assign the house instance variable

    @classmethod # Decorator designating the following method as a class method
    def get(cls): # Define the class method, passing the class reference as cls
        name = input("Name: ") # Prompt for and store the name string
        house = input("House: ") # Prompt for and store the house string
        return cls(name, house) # Instantiate and return an object using the class reference
```

---

## 5. Static Methods
Static methods (`@staticmethod`) belong to the class's namespace but do not require access to class (`cls`) or instance (`self`) state. They function as utility functions grouped within the class.

```python
import random # Import the standard random module

class Student: # Define the Student class
    @staticmethod # Decorator designating the following method as a static method
    def generate_id(): # Define the static method with no self or cls parameters
        return random.randint(1000, 9999) # Return a random integer between 1000 and 9999
```

---

## 6. Inheritance
Inheritance establishes a hierarchical relationship where a subclass inherits attributes and methods from a superclass. `super()` calls the superclass implementation.

```python
class Wizard: # Define the base superclass Wizard
    def __init__(self, name): # Define the initialization method for Wizard
        if not name: # Check if the name string is empty
            raise ValueError("Missing name") # Raise a ValueError if validation fails
        self.name = name # Assign the validated name instance variable

class Student(Wizard): # Define the Student subclass inheriting from Wizard
    def __init__(self, name, house): # Define the initialization method for Student
        super().__init__(name) # Call the Wizard superclass __init__ to handle name assignment
        self.house = house # Assign the Student-specific house instance variable

class Professor(Wizard): # Define the Professor subclass inheriting from Wizard
    def __init__(self, name, subject): # Define the initialization method for Professor
        super().__init__(name) # Call the Wizard superclass __init__ to handle name assignment
        self.subject = subject # Assign the Professor-specific subject instance variable
```

---

## 7. Operator Overloading
Dunder (double underscore) methods can be overridden to dictate how standard Python operators interact with custom objects.

```python
class Vault: # Define the Vault class
    def __init__(self, galleons=0, sickles=0, knuts=0): # Define initialization with default integer values
        self.galleons = galleons # Assign the galleons instance variable
        self.sickles = sickles # Assign the sickles instance variable
        self.knuts = knuts # Assign the knuts instance variable

    def __str__(self): # Define the string representation method
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts" # Return formatted string

    def __add__(self, other): # Overload the addition (+) operator
        galleons = self.galleons + other.galleons # Calculate the sum of galleons from both objects
        sickles = self.sickles + other.sickles # Calculate the sum of sickles from both objects
        knuts = self.knuts + other.knuts # Calculate the sum of knuts from both objects
        return Vault(galleons, sickles, knuts) # Instantiate and return a new Vault object containing the sums

def main(): # Define the main execution function
    potter = Vault(100, 50, 25) # Instantiate the first Vault object
    weasley = Vault(25, 50, 100) # Instantiate the second Vault object
    total = potter + weasley # Execute the overloaded __add__ method using the + operator
    print(total) # Print the resulting Vault object, triggering __str__
```
