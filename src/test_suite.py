#Delete testFranc for Multiplication?

import unittest
import multiCurrency
from multiCurrency import Money


class testMultiplication(unittest.TestCase):
    def testDollar(self):
        fiveDollars = multiCurrency.makeDollar(5)
        self.assertEquals(multiCurrency.makeDollar(10),fiveDollars.times(2))
        self.assertEquals(multiCurrency.makeDollar(15),fiveDollars.times(3))

    def testFranc(self):
        fiveFrancs = multiCurrency.makeFranc(5)
        self.assertEquals(multiCurrency.makeFranc(10),fiveFrancs.times(2))
        self.assertEquals(multiCurrency.makeFranc(15),fiveFrancs.times(3))
    

class testEquality(unittest.TestCase):
    def testDollar(self):
        self.assertEquals(multiCurrency.makeDollar(5), multiCurrency.makeDollar(5))
        self.assertNotEqual(multiCurrency.makeDollar(5), multiCurrency.makeDollar(6))         
    
    def testFranc(self):
        self.assertEquals(multiCurrency.makeFranc(5), multiCurrency.makeFranc(5))
        self.assertNotEqual(multiCurrency.makeFranc(5), multiCurrency.makeFranc(6))         

    def testMixed(self):
        self.assertNotEqual(multiCurrency.makeFranc(5),multiCurrency.makeDollar(5))