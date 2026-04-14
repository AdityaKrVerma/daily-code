class Character:
    def __init__(self, name, job, health):
        self.name = name
        self.job = job
        self.health = health
        self.inventory = []

    def take_damage(self, amount):
        self.health -= amount
        status = "standing" if self.health > 0 else "defeated"
        return f"{self.name} took {amount} damage and is {status}."

    def add_item(self, item):
        self.inventory.append(item)
        return f"{item} added to {self.name}'s bag."

hero = Character("Aria", "Mage", 100)
print(hero.take_damage(30))