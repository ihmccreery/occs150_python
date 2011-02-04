# world.py
#
# I. H. McCreery
# 4 February 2011
"""The world class for the critters"""

import random

class World(object):
    """Represents the world in which the creatures interact."""

    def __init__(self, width, height, critter_list):

        # perhaps turn these into properties, but probably not worth it
        self._width = width
        self._height = height

        # perform necessary imports of critters and assembles list
        # throws proper error if input is invalid
        self.critter_list = critter_list

        # opens a new simulation
        self.reset()

        for item in self._grid:
            print item

    def reset(self):
        """Resets the world to a new simulation."""
        self._grid = Grid(self._width, self._height, object=list)
        self.populate(25)

    def populate(self, num):
        """Populates world with num of each type of critter
        Drops each critter in a uniquely-determined random location."""
        location_list = random.sample(self._grid,
                                      num * len(self.critter_list))
        for Critter in self.critter_list:
            for i in range(num):
                location_list.pop().append(Critter())

    def tick(self):
        self.move()
        self.resolve()

    def move(self):
        for location in self._grid:
            move = location[0].move()

    def resolve(self):
        pass


class Grid(object):
    """A simple 2D nested-list structure

    g = Grid(width=20, height=40, object=list)
    default is the object that each entry contains when initialized.

    An entry is accessed as follows:
    g(1, 2) = 5
    g(3, 5).append(17)
    """

    def __init__(self, width, height, object=None):
        self._width = width
        self._height = height
        self._field = [[object() for y in range(height)]
                                 for x in range(width)]

    def __getitem__(self, (x, y)):
        return self._field[x][y]

    def __setitem__(self, (x, y)):
        return self._field[x][y]

    def __iter__(self):
        iter = []
        for x, row in enumerate(self._field):
            for y, column in enumerate(self._field[x]):
                iter.append(self[(x, y)])
        return iter.__iter__()

    def __len__(self):
        return self._width * self._height
