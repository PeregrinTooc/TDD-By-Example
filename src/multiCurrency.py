#money rounding?
#table lookup?
#equal null?
#equal other object?


from abc import ABC, abstractmethod 

def makeDollar(amount):
    return Money(amount, 'USD')

def makeFranc(amount):
    return Money(amount, 'CHF')
class Money:
    def __init__(self,amount,currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return ( self._amount == other._amount and self._currency == other._currency )

    def times(self, multiplicator):
        return Money(self._amount * multiplicator, self._currency)

    def getCurrency(self):
        return self._currency
    