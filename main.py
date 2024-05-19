class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep (self):
        print(f"{self.name} is sleeping...")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} is eating...")
        self.power += 2

    def hit(self):
        print(f"{self.name} is hitting...")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} is walking...")

    def info (self):
        print(f"Warrior's name {self.name} ")
        print(f"Warrior's power {self.power} ")
        print(f"Warrior's endurance {self.endurance} ")
        print(f"Warrior's hair color {self.hair_color}")


war1 = Warrior("Michal", 100, 20, "blue")
war2 = Warrior("Nick", 100, 20, "red")

war1.sleep()
war1.eat()
war1.walk()
war1.hit()
war1.info()

war2.sleep()
war2.eat()
war2.walk()
war2.hit()
war2.info()


