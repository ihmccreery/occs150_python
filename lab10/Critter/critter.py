# critter.py
#
# I. H. McCreery
# 2 February 2011

# directional constants
# tuples in the form (delta_x, delta_y)
# note that north is down, like in standard image representation
NORTH = (0, -1)
NORTHEAST = (1, -1)
EAST = (1, 0)
SOUTHEAST = (1, 1)
SOUTH = (0, 1)
WEST = (-1, 0)

# fighting constants
ROAR = 0
POUNCE = 1
SCRATCH = 2

class Critter(object):
    """A Critter absctract base class"""

    def __init__(self):
        """Initializer"""
        pass

    def move(self):
        """Returns the color of this critter."""
        pass

    def fight(self, opponent):
        """Returns the tactic of this critter."""
        pass

    def fight_over(self, won, opponent_tactic, opponent_color):
        """Called when fight is over to allow critter to analyze."""
        pass

    def character(self):
        """Returns the color of this critter."""
        pass

    def color(self):
        """Returns the color of this critter."""
        pass
