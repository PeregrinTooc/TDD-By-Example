#money rounding?
#table lookup?
#equal null?
#equal other object?


from abc import ABC, abstractmethod 

class Bank:
    def reduce(self, source, to):
        return source.reduce(to)
        
class Expression(ABC):
    @abstractmethod
    def reduce(self, to):
        pass
    

def makeDollar(amount):
    return Money(amount, 'USD')

def makeFranc(amount):
    return Money(amount, 'CHF')

class Sum(Expression):
    def __init__(self,augend,addend):
        self._augend = augend
        self._addend = addend
    
    def reduce(self,to):
        amount = self._augend.getAmount() + self._addend.getAmount()
        return Money(amount, to)
class Money(Expression):
    def __init__(self,amount,currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return ( self._amount == other._amount and self._currency == other._currency )

    def times(self, multiplicator):
        return Money(self._amount * multiplicator, self._currency)

    def getCurrency(self):
        return self._currency
    
    def getAmount(self):
        return self._amount
    
    def __add__(self, other):
        return Sum(self, other)
    
    def reduce(self,to):
        return self