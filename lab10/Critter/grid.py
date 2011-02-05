# grid.py
#
# I. H. McCreery
# 4 February 2011
"""A simple grid class for the critters.  Works something like a chessboard."""

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
        self._field = []

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
