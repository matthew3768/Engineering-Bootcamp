class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    pass


dog = Dog("Max")

print(dog.name)
dog.speak()


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed