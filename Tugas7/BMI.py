def add_bmi_method(cls):
    def bmi(self):
        return self.weight / (self.height ** 2)
    cls.bmi = bmi
    return cls

@add_bmi_method
class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

person1 = Person('John', 22, 60, 170)
print(person1.bmi())
