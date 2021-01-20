
import unittest
import multiCurrency
from multiCurrency import Money, makeDollar


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

class testAddition(unittest.TestCase):
    def setUp(self):
        super().setUp()    
        self.bank = multiCurrency.Bank()
    def testSameCurrency(self):
        sum = multiCurrency.makeDollar(5) + multiCurrency.makeDollar(5)
        reduced = self.bank.reduce(sum, 'USD')
        self.assertEquals(reduced, multiCurrency.makeDollar(10))
    
    def testPlusReturnsASum(self):
        five = makeDollar(5)
        sum = five + five
        self.assertEquals(sum._augend, five)
        self.assertEquals(sum._addend, five)


class testReduce(unittest.TestCase):
    def setUp(self):
        self.cut = multiCurrency.Bank().reduce
    
    def testReduceSum(self):
        sum = multiCurrency.makeDollar(3) + multiCurrency.makeDollar(4)
        self.assertEqual(self.cut(sum, 'USD'),multiCurrency.makeDollar(7))
    
    def testReduceMoney(self):
        self.assertEqual(self.cut(makeDollar(7), 'USD'),multiCurrency.makeDollar(7))
