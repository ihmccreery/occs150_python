# stone.py
#
# I. H. McCreery
# 2 February 2011

from Critter import *

class Stone(Critter):
    """A class to impliment a Stone critter"""

    def __init__(self):
        """The initializer"""
        pass

    def move(self):
        """Returns the color of this critter."""
        return CENTER

    def fight(opponent):
        """Returns the tactic of this critter."""
        return SCRATCH

    def fight_over(won, opponent_tactic, opponent_color):
        """Called when fight is over to allow critter to analyze."""
        pass

    def character():
        """Returns the color of this critter."""
        return 'S'

    def color():
        """Returns the color of this critter."""
        return (64, 64, 64)
