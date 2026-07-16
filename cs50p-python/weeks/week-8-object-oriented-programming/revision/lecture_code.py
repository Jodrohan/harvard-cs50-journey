class Student:  # Define a Student class encapsulating data and behavior
    def __init__(self, name, house):  # Initialize the instance with name and house
        self.name = name  # Call the name setter to validate and assign
        self.house = house  # Call the house setter to validate and assign

    def __str__(self):  # Define how the object represents itself as a string
        return f"{self.name} from {self.house}"  # Return formatted string for output

    @classmethod  # Mark as a class method that operates on the class itself
    def get(cls):  # Define alternative constructor to handle input gathering
        name = input("Name: ")  # Prompt user for the student's name string
        house = input("House: ")  # Prompt user for the student's house string
        return cls(name, house)  # Return an instance instantiated with the inputs

    @property  # Define a getter property for the name attribute
    def name(self):  # Retrieve the internal protected name variable
        return self._name  # Return the protected _name value to the caller

    @name.setter  # Define a setter property to encapsulate the name value
    def name(self, name):  # Validate and set the incoming name string
        if not name:  # Check if the provided name is empty or falsy
            raise ValueError("Missing name")  # Enforce name requirement with exception
        self._name = name  # Store the verified value in protected _name variable

    @property  # Define a getter property for the house attribute
    def house(self):  # Retrieve the internal protected house variable
        return self._house  # Return the protected _house value to the caller

    @house.setter  # Define a setter property to encapsulate the house value
    def house(self, house):  # Validate and set the incoming house string
        if not house:  # Check if the provided house is empty or falsy
            raise ValueError("Missing house")  # Enforce house requirement with exception
        self._house = house  # Store the verified value in protected _house variable


def main():  # Define the entry point function of the program
    student = Student.get()  # Leverage class method to create the student instance
    if student.name == "anoop":  # Evaluate the student's name using the getter property
        student.house = "bhosdipur"  # Update the student's house using the setter property
    print(student)  # Print the object directly, triggering the __str__ method


if __name__ == "__main__":  # Ensure code runs only when executed as a script
    main()  # Call the main function to kick off execution