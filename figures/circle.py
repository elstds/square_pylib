import math

from figures import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError('radius cannot be negative')
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2