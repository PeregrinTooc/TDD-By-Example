
import unittest

from multiCurrency import Bank, makeDollar, makeFranc


class commonTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.addRate(targetCurrency='USD', sourceCurrency='CHF', rate=2)


class testMultiplication(commonTest):
    def setUp(self):
        super().setUp()

    def testSimple(self):
        five = makeDollar(5)
        self.assertEquals(makeDollar(10), five.times(2))
        self.assertEquals(makeDollar(15), five.times(3))

    def testSum(self):
        fiveDollars = makeDollar(5)
        tenFrancs = makeFranc(10)
        sum = tenFrancs + fiveDollars
        expected = makeDollar(20)
        actual = self.bank.reduce(sum.times(2), 'USD')
        self.assertEquals(actual, expected)


class testEquality(unittest.TestCase):
    def testEquals(self):
        self.assertEquals(makeDollar(5),
                          makeDollar(5))

    def testNotEquals(self):
        self.assertNotEqual(makeDollar(5),
                            makeDollar(6))
        self.assertNotEqual(makeFranc(5),
                            makeDollar(5))


class TestCurrency(unittest.TestCase):
    def testFranc(self):
        self.assertEquals(makeFranc(1).getCurrency(), 'CHF')

    def testDollar(self):
        self.assertEquals(makeDollar(1).getCurrency(), 'USD')


class testAddition(commonTest):
    def setUp(self):
        super().setUp()

    def testSameCurrency(self):
        sum = makeDollar(5) + makeDollar(5)
        reduced = self.bank.reduce(sum, 'USD')
        self.assertEquals(reduced, makeDollar(10))

    def testDifferentCurrencies(self):
        sum = makeDollar(5) + makeFranc(10)
        reduced = self.bank.reduce(sum, 'USD')
        self.assertEquals(reduced, makeDollar(10))

    def testPlusReturnsASum(self):
        five = makeDollar(5)
        sum = five + five
        self.assertEquals(sum._augend, five)
        self.assertEquals(sum._addend, five)

    def testSumPlusMoney(self):
        five = makeDollar(5)
        sum = five + five
        sum += makeFranc(10)
        self.assertEquals(self.bank.reduce(sum, 'USD'), makeDollar(15))


class testReduce(commonTest):
    def setUp(self):
        super().setUp()
        self.cut = self.bank.reduce

    def testReduceSum(self):
        sum = makeDollar(3) + makeDollar(4)
        self.assertEqual(self.cut(sum, 'USD'), makeDollar(7))

    def testReduceMoney(self):
        self.assertEqual(self.cut(makeDollar(7), 'USD'),
                         makeDollar(7))

    def testReduceMoneyWithDifferentCurrencies(self):
        result = self.cut(makeFranc(2), 'USD')
        self.assertEquals(result, makeDollar(1))


class testBank(unittest.TestCase):
    def testIdentityRate(self):
        actualRate = Bank().getRate('EUR', 'EUR')
        self.assertEquals(actualRate, 1)
