import random


class Boxer:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def receiveDamage(self, hit):      #count damage 
        self.health = self.health - hit
        print('{} has {} hp left'.format(self.name, self.health))

    def hit(self, boxer):               #random damage applied to boxer
        hit = random.randrange(5, 33)
        boxer.receiveDamage(hit)
        print('{} hit {} for {}'.format(self.name, boxer.name, hit))

    def receiveHeath(self):
        return self.health

