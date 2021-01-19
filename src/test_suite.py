import unittest
from multiCurrency import Dollar
from multiCurrency import Franc


class testDollar(unittest.TestCase):
    def testMultiplication(self):
        fiveDollars = Dollar(5)
        self.assertEquals(Dollar(10),fiveDollars.times(2))
        self.assertEquals(Dollar(15),fiveDollars.times(3))

    def testEquality(self):
        self.assertEquals(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))         

class testFranc(unittest.TestCase):
    def testMultiplication(self):
        fiveDollars = Franc(5)
        self.assertEquals(Franc(10),fiveDollars.times(2))
        self.assertEquals(Franc(15),fiveDollars.times(3))

