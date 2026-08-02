class Student:
    def __init__(self, name, house, colour):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Aravali", "Nilgiri", "Shivalik", "Udaygiri"]:
             raise ValueError("Invalid House")

        self.name = name
        self.house = house
        self.colour = colour

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.colour:
            case "Shivalik":
                return "red"
            case "Aravali":
                return "blue"
            case "Nilgiri":
                return "green"
            case "Udaygiri":
                return "yellow"
def main():
    student = get_student()
    print("Expected Colour:")
    print(student.colour())

def get_student():
    name = input("name:")
    house = input("house:")
    colour = input("colour: ")

    return Student(name, house, colour)

if __name__ == "__main__":
    main()