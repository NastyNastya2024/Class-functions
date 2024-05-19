class Bird:
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} is flying")

    def eat(self):
        print(f"{self.name} is eating")

    def sing(self):
        print(f"{self.name} is singing - {self.voice}")

    def info(self):
        print(f"{self.name} - name")
        print(f"{self.name} - color")
        print(f"{self.name} - voice")

class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def walk(self):
        print(f"{self.name} is walking")

bird1 = Pigeon("Mark", "LaLaLa", "blue", "breadcrumbs")
bird1.fly()
bird1.sing()
bird1.walk()

bird2= Bird("Bob", "chirp", "green")

bird2.eat()
bird2.sing()
