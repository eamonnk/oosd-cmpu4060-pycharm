class Person:
    def __init__(self, n, s):
        self.name = n
        self.surname = s

    def print(self):
        print("")
        print("name: ", self.name)
        print("surname: ", self.surname)


    def get_fullname(self):
        return self.name + " " + self.surname


class Employee(Person):
    def __init__(self, n, s, en):
        super().__init__(n, s)
        self.employeeNumber = en

    def print(self):
        super().print()
        print("employee number: ", self.employeeNumber)