import random

class Wizard:
    count = 0
    dictionary = dict()

    def __init__(self, name, energy):
        Wizard.count += 1
        self.name = name
        self.energy = energy
        self.health = 100
        Wizard.dictionary[self.name] = self

    def introduce(self):
        print(f"Hey, my name is {self.name}.")

    def status(self):
        print(f"Name: {self.name} Energy: {self.energy} Health: {self.health}")

    def heal(self, target):
        if self.energy < 100:
            print("Not enough energy to heal!")
            return
                
        self.energy -= 100
        target.health = 100

class Human:
    count = 0
    dictionary = dict()

    def __init__(self, name):
        Human.count += 1
        self.name = name
        self.energy = 100
        self.health = 100
        Human.dictionary[self.name] = self

    def introduce(self):
        print(f"Hey, my name is {self.name}.")

    def status(self):
        print(f"📃 Name: {self.name} Energy: {self.energy} Health: {self.health}")

class Dragon:
    count = 0
    dictionary = dict()

    def __init__(self, name, energy):
        Dragon.count += 1
        self.name = name
        self.energy = energy
        self.health = 100
        Dragon.dictionary[self.name] = self

    def introduce(self):
        print(f"Hey, my name is {self.name}.")

    def status(self):
        print(f"📃 Name: {self.name} Energy: {self.energy} Health: {self.health}")

    def attack(self, target):
        if self.energy < 50:
            print("⚡ Not enough energy!")
            return
        
        print(f"💥 {self.name} attacks {target.name}!")
        self.energy -= 50
        target.health -= 30

humans = []
humans_removed = []
dragons = []

def main():
    for i in range(100):
        humans.append(Human(f"Human{i}"))

    for i in range(10):
        dragons.append(Dragon(f"Dragon{i}", 200))

    for i in range(2000):
        random_human_index = random.randint(0, len(humans) - 1)
        random_dragon_index = random.randint(0, 9)
        dragon = dragons[random_dragon_index]
        human = humans[random_human_index]

        dragon.attack(human)
        dragon.status()
        human.status()
        if human.health <= 0:            
            humans.remove(human)
            humans_removed.append(human)
        
    print(f"Humans removed: {len(humans_removed)}")

main()