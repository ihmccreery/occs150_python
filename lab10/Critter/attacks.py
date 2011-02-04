# directions.py
#
# I. H. McCreery
# 4 February 2011
"""The attack class and constants for the critters"""

class attack(object):

    def __init__(self, c):
        assert c in 'rps'
        self._value = c

    def __lt__(self, other):
        if self._value == 'r' and other._value == 'p':
            return True
        if self._value == 'p' and other._value == 's':
            return True
        if self._value == 's' and other._value == 'r':
            return True
        return False

    def __eq__(self, other):
        if self._value == other._value:
            return True
        else:
            return False

    def __gt__(self, other):
        if self._value == 'r' and other._value == 's':
            return True
        if self._value == 'p' and other._value == 'r':
            return True
        if self._value == 's' and other._value == 'p':
            return True
        return False

ROAR = attack('r')
POUNCE = attack('p')
SCRATCH = attack('s')

