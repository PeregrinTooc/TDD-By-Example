# money rounding?
# table lookup?
# equal null?
# equal other object?
# return Money from 5$ + 5$
# sum commutative?


def makeDollar(amount):
    return Money(amount, 'USD')


def makeFranc(amount):
    return Money(amount, 'CHF')


def make(amount, currency):
    return Money(amount, currency)


class Bank:
    def __init__(self):
        self.rates = {}

    def reduce(self, source, to):
        return source.reduce(self, to)

    def addRate(self, targetCurrency, sourceCurrency, rate):
        self.rates[(sourceCurrency, targetCurrency)] = rate

    def getRate(self, sourceCurrency, targetCurrency):
        if sourceCurrency == targetCurrency:
            return 1
        else:
            return self.rates[(sourceCurrency, targetCurrency)]


class Expression():
    def reduce(self, to):
        pass

    def __add__(self, other):
        return Sum(self, other)

    def times(self, multiplicator):
        pass


class Sum(Expression):
    def __init__(self, augend, addend):
        self._augend = augend
        self._addend = addend

    def reduce(self, bank, to):
        amount = self._augend.reduce(bank, to).getAmount(
        ) + self._addend.reduce(bank, to).getAmount()
        return Money(amount, to)

    def times(self, multiplicator):
        return Sum(self._augend.times(multiplicator), self._addend.times(multiplicator))


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (self._amount == other._amount and self._currency == other._currency)

    def times(self, multiplicator):
        return Money(self._amount * multiplicator, self._currency)

    def getCurrency(self):
        return self._currency

    def getAmount(self):
        return self._amount

    def reduce(self, bank, to):
        rate = bank.getRate(self._currency, to)
        return Money(self._amount/rate, to)
