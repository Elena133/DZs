import random


class boxMy:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def getDamage(self):
        return random.randrange(5, 33)


def printInf(nameOne, nameTwo, damage, health):
    a = "|{health} is {nameOne}\t s remained healthy, after {nameTwo} hit for {damage}|".format(health=health,
                                                                                                nameOne=nameOne,
                                                                                                nameTwo=nameTwo,
                                                                                                damage=damage)
    for j in range(len(a) + 2):
        print('-', end='')
    print()
    print(a)
    for j in range(len(a) + 2):
        print('-', end='')
    print()
    print()
