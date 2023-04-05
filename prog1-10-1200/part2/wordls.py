class Wizard:
    count = 0
    list = []
    dictionary = {}
    
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.health = 100
        Wizard.count += 1
        Wizard.list.append(self)
        Wizard.dictionary[self.name] = self

    def status(self):
        print(f"📄 Name:{self.name}\t Energy:{self.energy}\t Health:{self.health}")

    def heal(self, target):
        print(f"💗 {self.name} heals {target.name}")
        target.health = 100


class Human:
    count = 0
    list = []
    dictionary = dict()

    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.health = 100
        Human.count += 1
        Human.list.append(self)
        Human.dictionary[self.name] = self

    def status(self):
        print(f"📄 Name:{self.name}\t Energy:{self.energy}\t Health:{self.health}")


class Dragon:
    count = 0
    list = []
    dictionary = dict()

    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.health = 100
        Dragon.count += 1
        Dragon.list.append(self)
        Dragon.dictionary[self.name] = self

    def status(self):
        print(f"📄 Name:{self.name}\t Energy:{self.energy}\t Health:{self.health}")

    def attack(self, target):
        if self.energy < 100:
            print(f"⚡ Not enough energy to attack. {self.name} has {self.energy} energy.")
            return

        print(f"💥 {self.name} attacks {target.name}!")
        self.energy -= 100
        target.health -= 30

def main():
    humans = []
    dragons = []

    for i in range(100):
        humans.append(Human(f"Name{i}"))

    for i in range(10): 
        dragons.append(Dragon(f"Dragon{i}", 200))

    # UZDEVUMS:
    # Izveido programmu kas 20 reizes nejauši
    # izvēlēsies vienu pūķi un vienu cilvēku
    # un attiecīgi tas pūķis uzbruks cilvēkam

main()