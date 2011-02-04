# critter_main.py
#
# I. H. McCreery
# 2 February 2011
"""The main file for the critter lab.

Usage: python Critter/critter_main.py <Critter1> <Critter2> [...]
Where <Critter1>, etc. is the capitalized name of critters
"""
import sys
import Tkinter
import collections
import Critter

CRITTER_LIST = []

for Critter_Name in sys.argv[1:]:
    CRITTER_LIST.append(Critter_Name)

# directional constants
# tuples in the form (delta_x, delta_y)
# note that north is down, like in standard image representation

Location = collections.namedtuple('Location', 'x y')

NORTH = Location(0, -1)
NORTHEAST = Location(1, -1)
EAST = Location(1, 0)
SOUTHEAST = Location(1, 1)
SOUTH = Location(0, 1)
WEST = Location(-1, 0)
CENTER = Location(0, 0)

# fighting constants
# not sure how to represent these still. . .

ROAR = 0
POUNCE = 1
SCRATCH = 2

TITLE = 'Critter Main'

WORLD_WIDTH = 60
WORLD_HEIGHT = 50

def main():
    """The main method for the critter lab."""
    # unclear to me right now how to include the critters necessary
    application = Tkinter.Tk()
    application.title(TITLE)

    world = Critter.World(WORLD_WIDTH, WORLD_HEIGHT, CRITTER_LIST)
    # window = Critter.Main_Window(application, world)
    # application.mainloop()

main()
