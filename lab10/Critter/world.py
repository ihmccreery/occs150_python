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
            assert len(location) < 2, "There is more than one critter here"
            try:
                move = location[0].move()
            except IndexError:
                # there isn't a critter there
                pass

    def resolve(self):
        pass
