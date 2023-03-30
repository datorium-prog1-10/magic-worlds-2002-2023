class Wizard:
    count = 0
    
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.health = 100
        Wizard.count += 1

    def status(self):
        print(f"📄 Name:{self.name}\t Energy:{self.energy}\t Health:{self.health}")

    def heal(self, target):
        print(f"💗 {self.name} heals {target.name}")
        target.health = 100


class Human:
    count = 0

    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.health = 100
        Human.count += 1

    def status(self):
        print(f"📄 Name:{self.name}\t Energy:{self.energy}\t Health:{self.health}")


class Dragon:
    count = 0

    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.health = 100
        Dragon.count += 1

    def status(self):
        print(f"📄 Name:{self.name}\t Energy:{self.energy}\t Health:{self.health}")

    def attack(self, target):
        if self.energy < 100:
            print(f"⚡ Not enough energy to attack. {self.name} has {self.energy} energy.")
            return

        print(f"💥 {self.name} attacks {target.name}!")
        self.energy -= 100
        target.health -= 30

wiz1 = Wizard("Gandalf", 200)
wiz2 = Wizard("Saareman", 200)
hum1 = Human("Harry")
drag1 = Dragon("Smaug", 300)

wiz1.status()
hum1.status()
drag1.status()

for i in range(4):
    drag1.attack(hum1)
    hum1.status()

wiz1.heal(hum1)
hum1.status()