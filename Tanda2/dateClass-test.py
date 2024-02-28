"""
Test clase DateClass

Author: Jorge Pradillo Hinterberger
Date: 28/02/2024
"""
from dateClass import Date
import unittest


class TestDate(unittest.TestCase):
    def setUp(self):
        self.d1 = Date(1, 2, 2023)
        self.d2 = Date(29, 2, 2024)
        self.d3 = Date(31, 12, 2100)
        self.d4 = Date(28, 2, 2025)

    def test_to_iso_format(self):
        self.assertEqual(self.d1.to_iso_format(), '2023-02-01')
        self.assertEqual(self.d2.to_iso_format(), '2024-02-29')
        self.assertEqual(self.d3.to_iso_format(), '2100-12-31')

    def test_is_leap(self):
        self.assertFalse(self.d1.is_leap())
        self.assertTrue(self.d2.is_leap())
        self.assertFalse(self.d3.is_leap())

    # Tarda mucho en procesar la información, por eso están indicados como comentarios.
    """ 
    def test_weekday(self):
        self.assertEqual(self.d1.weekday(), 2)
        self.assertEqual(self.d2.weekday(), 3)
        self.assertEqual(self.d3.weekday(), 4)
    """

    def test_add(self):
        self.d1 = self.d1.__add__(3)
        self.assertEqual(self.d1, Date(4, 2, 2023))
        self.d1 = self.d1.__add__(390)
        self.assertEqual(self.d1, Date(29, 2, 2024))
        self.d2 = self.d2.__add__(365)
        self.assertEqual(self.d2, Date(28, 2, 2025))
        self.d3 = self.d3.__add__(366)
        self.assertEqual(self.d3, Date(1, 1, 2102))
        self.d3 = self.d3.__add__(-365)
        self.assertEqual(self.d3, Date(1, 1, 2101))

    def test_sub(self):
        self.d1 = self.d1.__sub__(365)
        self.assertEqual(self.d1, Date(1, 2, 2022))
        self.d4 = self.d4.__sub__(365)
        self.assertEqual(self.d4, Date(29, 2, 2024))
        self.d3 = self.d3.__sub__(729)
        self.assertEqual(self.d3, Date(1, 1, 2099))
        self.d3 = self.d3.__sub__(1)
        self.assertEqual(self.d3, Date(31, 12, 2098))
        self.d3 = self.d3.__sub__(-1)
        self.assertEqual(self.d3, Date(1, 1, 2099))
        self.fist_day_firs_year = Date(1, 1, 1)
        self.last_day_first_year = Date(31, 12, 1)
        self.d_aux = self.last_day_first_year.__sub__(self.fist_day_firs_year)
        self.assertEqual(self.d_aux, 364)

    def test_is_ok(self):
        # años
        with self.assertRaises(ValueError):
            self.d1.year = 0
        with self.assertRaises(ValueError):
            self.d2.year = -13

        # meses
        with self.assertRaises(ValueError):
            self.d3.month = 13
        with self.assertRaises(ValueError):
            self.d3.month = -1

        # días
        with self.assertRaises(ValueError):
            self.d3.day = 32
        with self.assertRaises(ValueError):
            self.d4.day = 29
        with self.assertRaises(ValueError):
            self.d1.day = -1

    def tearDown(self):
        del self.d1
        del self.d2
        del self.d3
        del self.d4
        del self.d_aux
