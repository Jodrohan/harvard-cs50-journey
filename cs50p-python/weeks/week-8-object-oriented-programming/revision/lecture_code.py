class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if not house:
            raise ValueError("Missing house")
        self._house = house


def main():
    student = Student.get()
    if student.name == "anoop":
        student.house = "bhosdipur"
    print(student)


if __name__ == "__main__":
    main()