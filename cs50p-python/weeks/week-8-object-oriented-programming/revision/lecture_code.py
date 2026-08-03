class Student:
    def __init__(self, name, house, colour):
        if not name:
            raise ValueError("Missing name")
        # Validates against the specific houses
        if house not in ["Aravali", "Nilgiri", "Shivalik", "Udaygiri"]:
             raise ValueError("Invalid House")

        self.name = name
        self.house = house
        self.colour = colour

    def __str__(self):
        return f"{self.name} from {self.house}"

    def expected_colour(self):
        # Matches against the house to return the correct associated color
        match self.house:
            case "Shivalik":
                return "red" 
            case "Aravali":
                return "blue"
            case "Nilgiri":
                return "green"
            case "Udaygiri":
                return "yellow"

def main():
    # Gets the student information from the user
    student = get_student()
    
    print("\n--- Student Profile ---")
    print(student)
    print(f"Provided Colour: {student.colour}")
    print(f"Expected House Colour: {student.expected_colour()}")

def get_student():
    name = input("Name: ")
    house = input("House (Aravali, Nilgiri, Shivalik, Udaygiri): ")
    colour = input("Colour: ")

    return Student(name, house, colour)

if __name__ == "__main__":
    main()