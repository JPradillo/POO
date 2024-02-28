from unittest import TestCase
from fraction import Fraction


class TestFunction(TestCase):
    def setUp(self):
        self.f1 = Fraction(2, 5)
        self.f2 = Fraction(8, 2)
        self.f3 = Fraction(2, 5)

    def test_result(self):
        # F1(2, 5)
        # F2(8, 2)
        # F3(2, 5)
        self.assertTrue(self.f1, 0.5)
        self.assertTrue(self.f2, 4)
        self.assertTrue(self.f3, 0.4)

    def test_mul(self):
        # F1(2, 5)
        # F2(8, 2)
        # F3(2, 5)
        self.assertEqual(self.f1 * self.f2, Fraction(8, 5))
        self.assertEqual(self.f1 * self.f3, Fraction(4, 25))
        self.assertEqual(self.f1 * 2, Fraction(4, 5))
        self.assertTrue(self.f1 * self.f2, 1.6)

    def test_rmul(self):
        # F1(2, 5)
        # F2(8, 2)
        self.assertEqual(2 * self.f1, Fraction(4, 5))
        self.assertTrue(2 * self.f2, 8)

    def test_truediv(self):
        # F1(2, 5)
        # F2(8, 2)
        self.assertEqual(self.f1 / self.f2, Fraction(1, 10))
        self.assertTrue(self.f1 / self.f2, 0.1)

    def test_add(self):
        # F1(2, 5)
        # F2(8, 2)
        self.assertEqual(self.f1 + self.f2, Fraction(22, 5))
        self.assertTrue(self.f1 + self.f2, 4.4)

    def test_sub(self):
        # F1(2, 5)
        # F2(8, 2)
        self.assertEqual(self.f1 - self.f2, Fraction(-18, 5))
        self.assertTrue(self.f1 - self.f2, -3.6)

    def test_equals(self):
        # F1(2, 5)
        # F2(8, 2)
        # F3(2, 5)
        self.assertEqual(self.f1 == self.f2, False)
        self.assertEqual(self.f1 == self.f3, True)

    def test_not_equals(self):
        # F1(2, 5)
        # F2(8, 2)
        # F3(2, 5)
        self.assertEqual(self.f1 != self.f2, True)
        self.assertEqual(self.f1 != self.f3, False)

    def test_lt(self):
        # F1(2, 5)
        # F2(8, 2)
        # F3(2, 5)
        self.assertEqual(self.f1 < self.f2, True)
        self.assertEqual(self.f2 < self.f3, False)

    def test_gt(self):
        # F1(2, 5)
        # F2(8, 2)
        # F3(2, 5)
        self.assertEqual(self.f2 > self.f1, True)
        self.assertEqual(self.f3 > self.f2, False)

    def test_le(self):
        # F1(2, 5)
        # F2(8, 2)
        # F3(2, 5)
        self.assertEqual(self.f1 <= self.f2, True)
        self.assertEqual(self.f1 <= self.f3, True)
        self.assertEqual(self.f2 <= self.f3, False)

    def test_ge(self):
        # F1(2, 5)
        # F2(8, 2)
        # F3(2, 5)
        self.assertEqual(self.f1 >= self.f2, False)
        self.assertEqual(self.f1 >= self.f3, True)
        self.assertEqual(self.f2 >= self.f3, True)

    def tearDown(self):
        del self.f1
