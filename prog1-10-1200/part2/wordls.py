import random

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
        target.health -= 50

humans = []
humans_removed = []
dragons = []

def main():
    for i in range(100):
        humans.append(Human(f"Name{i}"))

    for i in range(10): 
        dragons.append(Dragon(f"Dragon{i}", 1000))

    # UZDEVUMS:
    # Izveido programmu kas 20 reizes nejauši
    # izvēlēsies vienu pūķi un vienu cilvēku
    # un attiecīgi tas pūķis uzbruks cilvēkam

    for i in range(200):
        random_dragon = random.choice(dragons)
        random_human = random.choice(humans)
        random_dragon.attack(random_human)

    # UZDEVUMS:
    # Ja kādam cilvēkam beidzās veselība tad
    # lai izņem to no saraksta `humans` un 
    # ieliec to citā sarakstā `humans_removed`

        if random_human.health <= 0:
            humans.remove(random_human)
            humans_removed.append(random_human)

    print(len(humans_removed))
main()