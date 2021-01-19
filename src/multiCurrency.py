#money rounding?
#table lookup?
#equal null?
#equal other object?
# Common times



from unittest.result import TestResult

class Money:
    def __init__(self,amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount
class Dollar(Money):

    def times(self,multiplicator):
        return Dollar(self._amount * multiplicator)
    
class Franc(Money):

    def times(self,multiplicator):
        return Franc(self._amount * multiplicator)    