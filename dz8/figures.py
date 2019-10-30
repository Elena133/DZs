import math


class Circle:
    def __init__(self, r):
        self.name = 'Круг'
        self.r = r

    def getSquare(self):
        return math.pi * self.r ** 2

    def getPer(self):
        return math.pi * self.r * 2


class Rectangle:
    def __init__(self, a, b):
        self.name = 'Прямоугольник'
        self.a = a
        self.b = b

    def getSquare(self):
        return self.a * self.b

    def getPer(self):
        return self.a * 2 + self.b * 2


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = 'Треугольник'

    def getSquare(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def getPer(self):
        return self.a + self.b + self.c
