class Person:
    first_name: str
    last_name: str
    age: int


person1 = Person()

person1.first_name = 'John'
person1.last_name = 'Doe'
person1.age = 43

print(person1.first_name)


# Простой класс с конструктором
class Person:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name: str, last_name: str, age: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


person2 = Person('John', 'Doe', 43)

print(person2.first_name)


# Класс с методами
class Person:
    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name: str, last_name: str, age: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def info(self):
        print(f"Person: {self.first_name} {self.last_name}, age: {self.age}")


person3 = Person('John', 'Doe', 43)

person3.info()