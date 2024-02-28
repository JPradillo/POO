from unittest import TestCase
from duration import Duration


class TestDuration(TestCase):
    def setUp(self):
        self.d1 = Duration(2, 15, 57)
        self.d2 = Duration(0, 44, 3)
        self.d3 = Duration(0, 60, 0)
        self.d4 = Duration(0, 0, 60)

    def test_add(self):
        self.d1 = self.d1.__add__(self.d2)
        self.assertEqual(self.d1, Duration(3, 00, 00))
        self.d1 = self.d1.__add__(self.d3)
        self.assertEqual(self.d1, Duration(4, 00, 00))
        self.d1 = self.d1.__add__(self.d4)
        self.assertEqual(self.d1, Duration(4, 1, 00))

    def test_sub(self):
        self.d1 = self.d1.__sub__(self.d2)
        self.assertEqual(self.d1, Duration(1, 31, 54))
        self.d1 = self.d1.__sub__(self.d3)
        self.assertEqual(self.d1, Duration(0, 31, 54))
        self.d1 = self.d1.__sub__(self.d4)
        self.assertEqual(self.d1, Duration(0, 30, 54))

    def test_add_hours(self):
        self.d1.add_hours(2)
        self.assertEqual(self.d1, Duration(4, 15, 57))
        self.d1.add_hours(25)
        self.assertEqual(self.d1, Duration(29, 15, 57))

    def test_add_minutes(self):
        self.d1.add_minutes(45)
        self.assertEqual(self.d1, Duration(3, 0, 57))
        self.d1.add_minutes(60)
        self.assertEqual(self.d1, Duration(4, 0, 57))

    def test_add_seconds(self):
        self.d1.add_seconds(3)
        self.assertEqual(self.d1, Duration(2, 16, 0))
        self.d1.add_seconds(60)
        self.assertEqual(self.d1, Duration(2, 17, 0))
        self.d1.add_seconds(3600)
        self.assertEqual(self.d1, Duration(3, 17, 0))
        self.d1.add_seconds(2580)
        self.assertEqual(self.d1, Duration(4, 0, 0))

    def test_sub_hours(self):
        self.d1.sub_hours(2)
        self.assertEqual(self.d1, Duration(0, 15, 57))

    def test_sub_minutes(self):
        self.d1.sub_minutes(16)
        self.assertEqual(self.d1, Duration(1, 59, 57))
        self.d1.sub_minutes(60)
        self.assertEqual(self.d1, Duration(0, 59, 57))

    def test_sub_seconds(self):
        self.d1.sub_seconds(58)
        self.assertEqual(self.d1, Duration(2, 14, 59))
        self.d1.sub_seconds(3600)
        self.assertEqual(self.d1, Duration(1, 14, 59))
        self.d1.sub_seconds(4499)
        self.assertEqual(self.d1, Duration(0, 0, 0))

    def tearDown(self):
        del self.d1
