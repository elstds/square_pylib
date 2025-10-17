import unittest
import math
from figures import Figure, Circle, Triangle


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25, places=5)

    def test_circle_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6, places=5)

    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # The sides do not form a triangle

    def test_triangle_is_right_angled(self):
        right_triangle = Triangle(3, 4, 5)
        self.assertTrue(right_triangle.is_right_angled())
        not_right = Triangle(2, 3, 4)
        self.assertFalse(not_right.is_right_angled())

    def test_polymorphism(self):
        shapes = [Circle(1), Triangle(3, 4, 5)]
        areas = [shape.area() for shape in shapes]  # Runtime без знания типа
        self.assertGreater(areas[0], 0)
        self.assertGreater(areas[1], 0)


if __name__ == "__main__":
    unittest.main()
