# world.py
#
# I. H. McCreery
# 4 February 2011
"""The world class for the critters"""

class World(object):
    """Represents the world in which the creatures interact."""

    def __init__(self, width, height, critter_list):

        # perhaps turn these into properties, but probably not worth it
        self.width = width
        self.height = height

        self._grid = Grid(width, height, default=[])

        # perform necessary imports of critters and assembles list
        # throws proper error if input is invalid
        self.critter_list = []
        for Critter_Name in critter_list:
            critter_name = str.lower(Critter_Name)
            exec "from "+critter_name+" import "+Critter_Name
            self.critter_list.append(Critter_Name)

        # opens a new simulation
        self.reset()

    def reset(self):
        """Resets the world to a new simulation."""
        self.populate(25)

    def populate(self, num):
        """Populates world with number of critters."""
        for Critter_Name in self.critter_list:

    def turn(self):
        pass


class Grid(object):
    """A simple 2D nested-list structure

    g = Grid(width=20, height=40, default=[])
    default is the object that each entry contains when initialized.

    An entry is accessed as follows:
    g(1, 2) = 5
    g(3, 5).append(17)
    """

    def __init__(self, width, height, default=None):
        self.width = width
        self.height = height
        self._field = [[default for y in range(height)]
                                for x in range(width)]

    def __getitem__(self, x, y):
        return self._field[x][y]

    def __setitem__(self, x, y):
        return self._field[x][y]


