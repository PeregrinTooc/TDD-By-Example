import unittest
from unittest.main import TestProgram
from multiCurrency import Dollar


class Dollar(unittest.TestCase):
    def testMultiplication(self):
        fiveDollars = Dollar(5)
        self.assertEquals(Dollar(10),fiveDollars.times(2))
        self.assertEquals(Dollar(15),fiveDollars.times(3))

    def testEquality(self):
        self.assertEquals(Dollar(5), Dollar(5))
        self.assertNotEquals(Dollar(5), Dollar(6))         

