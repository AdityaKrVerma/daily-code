class VirtualPet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.happiness = 50

    def play(self):
        self.happiness += 10
        self.hunger += 5
        return f"{self.name} the {self.species} is wagging its tail!"

    def feed(self):
        self.hunger -= 15
        return f"Nom nom! {self.name} is full."

my_pet = VirtualPet("Sparky", "Dragon")
print(my_pet.play())