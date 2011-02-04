# directions.py
#
# I. H. McCreery
# 4 February 2011
"""The directional constants for the critters"""

import collections

# tuples in the form (delta_x, delta_y)
# note that north is down, like in standard image representation

Location = collections.namedtuple('Location', 'x y')

NORTH = Location(0, -1)
NORTHEAST = Location(1, -1)
EAST = Location(1, 0)
SOUTHEAST = Location(1, 1)
SOUTH = Location(0, 1)
SOUTHWEST = Location(-1, 1)
WEST = Location(-1, 0)
NORTHWEST = Location(-1, -1)
CENTER = Location(0, 0)
