from Point import Point
from Rectángulo import Rectangle
from unittest import TestCase


class RectangleTest(TestCase):
    def setUp(self):
        self.p1 = Point(1, 1)
        self.p2 = Point(2, 2)
        self.p3 = Point(-1, -1)
        self.p4 = Point(0, 0)

        self.r1 = Rectangle(self.p1, self.p2)
        self.r2 = Rectangle(self.p3, self.p2)
        self.r3 = Rectangle(self.p4, self.p2)
        self.r4 = Rectangle(self.p3, self.p1)

    def test_area(self):
        self.assertEqual(self.r1.area, 1.0)
        self.assertEqual(self.r2.area, 9.0)
        self.assertEqual(self.r3.area, 4.0)
        self.assertEqual(self.r4.area, 4.0)

    def test_perimeter(self):
        self.assertEqual(self.r1.perimeter, 4.0)
        self.assertEqual(self.r2.perimeter, 12.0)
        self.assertEqual(self.r3.perimeter, 8.0)
        self.assertEqual(self.r4.perimeter, 8.0)

    def tearDown(self):
        del self.r1
        del self.r2
        del self.r3
        del self.r4
