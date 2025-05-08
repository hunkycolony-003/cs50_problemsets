class Students:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("No Input recieved")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house.title() not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hupplepuff"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_students()
    print(student)


def get_students():
    name = input("Name: ")
    house = input("House: ")
    return Students(name, house)


if __name__ == "__main__":
    main()
