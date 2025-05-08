class Wizard:
    def __init__(self, name):
        if not name:
            ValueError("No Name recieved")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{self.name}, je {self.house} e thake,"


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def __str__(self):
        return f"take {professor.name} {professor.subject} poray"


student = Student("Harry", "Gryffindor")
professor = Professor("Samrat sir", "Physics")
print(student, professor)
