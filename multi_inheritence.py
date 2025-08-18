class Employee:
    company = "MAKTEK"
    name = "Ali"

    def show(self):
        print(f"The name of Employee is {self.name} and the company is {self.company}")


class Coder:
    language = "python"

    def printLanguage(self):
        print(f"Out of the languages, here is your language: {self.language}")


class Programmer(Employee, Coder):  # Multiple inheritance
    company = "MAKTEK"

    def showLanguage(self):
        print(f"The company is {self.company} and the employee is good with {self.language}")


# Objects
a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()
