# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

# Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def make_sound(self):
        return "Tweet"

class Mammal(Animal):
    def make_sound(self):
        return "Roar"

class Reptile(Animal):
    def make_sound(self):
        return "Hiss"

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Класс Zoo с использованием композиции
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

# Классы сотрудников
class ZooKeeper:
    def feed_animal(self, animal):
        return f"{animal.name} is being fed by the ZooKeeper"

class Veterinarian:
    def heal_animal(self, animal):
        return f"{animal.name} is being healed by the Veterinarian"

# Пример использования
bird1 = Bird("Parrot", 5)
mammal1 = Mammal("Lion", 10)
reptile1 = Reptile("Snake", 3)

zoo = Zoo()
zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zookeeper = ZooKeeper()
veterinarian = Veterinarian()

print("Animal sounds:")
animal_sound([bird1, mammal1, reptile1])

print(zookeeper.feed_animal(bird1))
print(veterinarian.heal_animal(mammal1))