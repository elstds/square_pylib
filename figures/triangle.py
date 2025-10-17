import math

from figures import Figure


class Triangle(Figure):
    def __init__(self, x, y, z):
        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError("x, y, and z must be positive")
        if x + y <= z or y + z <= x or z + x <= y:
            raise ValueError("The sides do not form a triangle")
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        s = (self.x + self.y + self.z) / 2
        return math.sqrt(s * (s - self.x) * (s - self.y) * (s - self.z))

    def is_right_angled(self):
        sides = sorted([self.x, self.y, self.z])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
