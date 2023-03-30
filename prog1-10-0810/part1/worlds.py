class Wizard:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.health = 100

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
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.health = 100

    def introduce(self):
        print(f"Hey, my name is {self.name}.")

    def status(self):
        print(f"Name: {self.name} Energy: {self.energy} Health: {self.health}")

class Dragon:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.health = 100

    def introduce(self):
        print(f"Hey, my name is {self.name}.")

    def status(self):
        print(f"Name: {self.name} Energy: {self.energy} Health: {self.health}")

    def attack(self, target):
        if self.energy < 50:
            print("Not enough energy!")
            return
        
        self.energy -= 50
        target.health -= 30


wiz1 = Wizard("Gandalf", 500)
wiz2 = Wizard("Saaraman", 500)
hum1 = Human("Harry")
drag1 = Dragon("Smaug", 120)

wiz1.status()
wiz2.status()
hum1.status()
drag1.status()

for i in range(3):
    drag1.attack(hum1)
    drag1.status()
    hum1.status()

wiz1.heal(hum1)
hum1.status()