class Animal():
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("I am a dog.")

class Cat(Animal):
    def make_sound(self):
        print("I am a cat.")

class Cow(Animal):
    def make_sound(self):
        print("I am a cow.")


animals = [Dog(), Cat(), Cow()]
for animal in animals:
     animal.make_sound()
