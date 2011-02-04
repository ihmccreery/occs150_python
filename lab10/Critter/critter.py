# critter.py
#
# I. H. McCreery
# 2 February 2011

import abc

class Critter(object):
    """A Critter absctract base class"""

    __metaclass__ = abc.ABCMeta

    # methods for students to overwrite

    def __init__(self):
        """Initializer"""
        super(Critter, self).__init__()

    @abc.abstractmethod
    def move(self):
        """Returns the movement of this critter."""
        pass

    @abc.abstractmethod
    def attack(self, opponent):
        """Returns the attack of this critter."""
        pass

    @abc.abstractmethod
    def character(self):
        """Returns the character of this critter."""
        pass

    @abc.abstractmethod
    def color(self):
        """Returns the color of this critter."""
        pass

    def fight_over(self, won, opponent_attack, opponent_color):
        """Called when fight is over to allow critter to analyze."""
        pass

    # private methods

    @property
    def x(self):
        """This critter's x-coordinate"""
        return self._x

    @x.setter
    def x(self, x):
        """Sets this critter's x-coordinate"""
        if type(x) == int:
            self._x = x
        else:
            raise TypeError('TypeError: expected integer, got {0)'.format(type(x)))

    @property
    def y(self):
        """This critter's y-coordinate"""
        return self._y

    @y.setter
    def y(self, y):
        """Sets this critter's y-coordinate"""
        if type(y) == int:
            self._y = y
        else:
            raise TypeError('TypeError: eypected integer, got {0)'.format(type(y)))
