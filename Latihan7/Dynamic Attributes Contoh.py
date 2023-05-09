class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Person = Person("John", 30)

# Menambah atribut address secara dinamis
Person.address = "123 Main St."

# Mengubah nilai atribut age secara dinamis
Person.age = 35


print(Person.name)
print(Person.age)
print(Person.address)
