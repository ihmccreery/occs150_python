# mouse.py
#
# I. H. McCreery
# 2 February 2011

from Critter import *

class Mouse(Critter):
    """A class to impliment a Stone critter"""

    def __init__(self, x, y):
        """The initializer"""
        super(type(self), self).__init__(x, y)
        self.last_dir = SOUTH
        self._color = (255, 255, 255)

    def move(self):
        """Returns the movement of this critter."""
        if self.last_dir == SOUTH:
            self.last_dir = EAST
            return EAST
        else:
            self.last_dir = SOUTH
            return SOUTH

    def attack(opponent):
        """Returns the attack of this critter."""
        return SCRATCH

    def character(self):
        """Returns the character of this critter."""
        return 'M'

    def color(self):
        """Returns the color of this critter."""
        return self._color
