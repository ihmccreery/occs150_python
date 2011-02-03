# critter_main.py
#
# I. H. McCreery
# 2 February 2011
"""The main file for the critter lab."""

# directional constants
# tuples in the form (delta_x, delta_y)
# note that north is down, like in standard image representation
# these should turn into named tuples!

NORTH = (0, -1)
NORTHEAST = (1, -1)
EAST = (1, 0)
SOUTHEAST = (1, 1)
SOUTH = (0, 1)
WEST = (-1, 0)
CENTER = (0, 0)

# fighting constants
# not sure how to represent these still. . .

ROAR = 0
POUNCE = 1
SCRATCH = 2

def main():
    """The main method for the critter lab.

    This creates a GUI for the user to run the simulations.
    """
    # unclear to me right now how to include the critters necessary
