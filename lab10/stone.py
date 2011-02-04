# stone.py
#
# I. H. McCreery
# 2 February 2011

from Critter import *

class Stone(Critter):
    """A class to impliment a Stone critter"""

    def __init__(self):
        """The initializer"""
        super(Stone, self).__init__()
        pass

    def move(self):
        """Returns the movement of this critter."""
        return CENTER

    def attack(opponent):
        """Returns the attack of this critter."""
        return ROAR

    def character(self):
        """Returns the character of this critter."""
        return 'S'

    def color(self):
        """Returns the color of this critter."""
        return (63, 63, 63)
