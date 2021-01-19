#money rounding?
#table lookup?
#equal null?
#equal other object?

from unittest.result import TestResult


class Dollar:
    def __init__(self,amount):
        self._amount = amount

    def times(self,multiplicator):
        return Dollar(self._amount * multiplicator)
    
    def __eq__(self, other):
        return self._amount == other._amount