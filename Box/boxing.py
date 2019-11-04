import random


class boxMy:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def getDamage(self):
        return random.randrange(5, 33)

    def printInf(self, nameOne, nameTwo, damage, health):
        self.nameOne = nameOne
        self.nameTwo = nameTwo
        self.damage = damage
        self.health = health
        print("{health}{nameOne}\t s remained healthy, after {nameTwo} hit for {damage}".format(health=self.health, nameOne=self.nameOne, nameTwo=self.nameTwo,damage=self.damage))
