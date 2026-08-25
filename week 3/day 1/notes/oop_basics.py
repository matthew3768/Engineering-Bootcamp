class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(self.brand, self.model, self.year)


car1 = Car("Ford", "Fiesta", 2020)
car2 = Car("BMW", "M3", 2023)

car1.display_info()
car2.display_info()

class Student:
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(self.name, self.grade)

    def has_passed(self):
        if self.grade >= 40:
            print('Passed!')
        else:
            print('Failed!')

student1 = Student('Matthew', 78)
student2 = Student('Bard', 65)
student3 = Student('Harry', 89)

student1.display_info()
student1.has_passed()
student2.display_info()
student3.display_info()