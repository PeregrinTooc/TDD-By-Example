#money rounding?
#table lookup?
#equal null?
#equal other object?
# Common times
#Currency?


from abc import ABC, abstractmethod 

def makeDollar(amount):
    return Dollar(amount)

def makeFranc(amount):
    return Franc(amount)
class Money(ABC):
    def __init__(self,amount):
        self._amount = amount

    def __eq__(self, other):
        return ( self._amount == other._amount and self.__class__ == other.__class__ )
    
    @abstractmethod
    def times(self, multiplicator):
        pass
class Dollar(Money):

    def times(self,multiplicator):
        return Dollar(self._amount * multiplicator)
    
class Franc(Money):

    def times(self,multiplicator):
        return Franc(self._amount * multiplicator)    