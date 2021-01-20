#Delete testFranc for Multiplication?  

import unittest
import multiCurrency
from multiCurrency import Money


class testMultiplication(unittest.TestCase):
    def testSimple(self):
        five = Money(5,'USD')
        self.assertEquals(Money(10,'USD'),five.times(2))
        self.assertEquals(Money(15,'USD'),five.times(3))

    

class testEquality(unittest.TestCase):
    def testEquals(self):
        self.assertEquals(multiCurrency.makeDollar(5), multiCurrency.makeDollar(5))
        self.assertEquals(multiCurrency.makeFranc(5), Money(5, 'CHF'))

    def testNotEquals(self):
        self.assertNotEqual(multiCurrency.makeDollar(5), multiCurrency.makeDollar(6))         
        self.assertNotEqual(multiCurrency.makeFranc(5),multiCurrency.makeDollar(5))


class TestCurrency(unittest.TestCase):
    def testFranc(self):
        self.assertEquals(multiCurrency.makeFranc(1).getCurrency(), 'CHF')
    
    def testDollar(self):
        self.assertEquals(multiCurrency.makeDollar(1).getCurrency(), 'USD')