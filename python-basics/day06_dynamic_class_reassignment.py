class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

pet = Dog()
print(pet.speak())

pet.__class__ = Cat
print(pet.speak())