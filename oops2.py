class Employee:
    language = "python"
    salary = 234525

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


# create object
harry = Employee("Harry", 123124, "Javascript")
harry.getInfo()
harry.greet()
