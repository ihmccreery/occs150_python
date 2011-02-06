# grid.py
#
# I. H. McCreery
# 4 February 2011
"""A simple grid class for the critters.  Works something like a chessboard."""

import collections

Cell = collections.namedtuple('Cell', 'contents x y')

class Grid(object):
    """A simple 2D nested-list structure

    g = Grid(width, height, object)
    object is the object that each entry contains when initialized.

    >>> g = Grid(6, 6, list)
    >>> g[0,0]
    []
    >>> g[1,1].append('q')
    >>> g[3,3].append('r')
    >>> g[3,4].append('r')
    >>> g[4,5].append('r')
    >>> print g
    +------+
    |      |
    | *    |
    |      |
    |   *  |
    |   *  |
    |    * |
    +------+
    >>> for l in g:
    ...     l.append('x')
    >>> g[5,5]
    ['x']
    >>> g[5,5] = ['rrr']
    >>> g[5,5]
    ['rrr']
    """

    def __init__(self, width, height, object):
        self.__width = width
        self.__height = height
        self.__object = object
        self.__layout()

    # collection special methods

    def __contains__(self, o):
        for x in self:
            if o in x:
                return True
        return False

    def __delitem__(self, o):
        pass

    def __getitem__(self, (x, y)):
        return self.__field[x][y].contents

    def __iter__(self):
        l = []
        for x, row in enumerate(self.__field):
            for y, column in enumerate(self.__field[x]):
                l.append(self[(x, y)])
        return l.__iter__()

    def __len__(self):
        return self.__width * self.__height

    # not implimenting
    # def __reversed__(self):

    def __setitem__(self, (x, y), c):
        self.__field[x][y] = Cell(c, x, y)

    def __str__(self):
        s = []
        s.append('+'+self.width*'-'+'+')
        for y in range(self.height):
            line = '|'
            for x in range(self.width):
                if self[x,y]:
                    line += '*'
                else:
                    line += ' '
            line += '|'
            s.append(line)
        s.append('+'+self.width*'-'+'+')
        return '\n'.join(s)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # special internal methods

    def __layout(self):
        self.__field = []
        for x in range(self.__width):
            self.__field.append([])
            for y in range(self.__height):
                self.__field[x].append(Cell(self.__object(), x, y))

# Test

if __name__ == "__main__":
    import doctest
    doctest.testmod()
