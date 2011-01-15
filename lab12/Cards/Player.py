# Player.py
#
# I. H. McCreery
# 14 January 2010
"""A module to impliment basic player functionality
Includes class Player

>>> Player("Monty")
Player('Monty')
>>> Player()
Traceback (most recent call last):
...
TypeError: __init__() takes exactly 2 arguments (1 given)
"""

class Player(object):

    def __init__(self, name):
        """Initializer function

        >>> Player("Monty")
        Player('Monty')
        >>> Player()
        Traceback (most recent call last):
        ...
        TypeError: __init__() takes exactly 2 arguments (1 given)
        """

        self.name = name
        self.hand = []

    def __repr__(self):
        """Callable representation of the player

        >>> repr(Player("Monty"))
        "Player('Monty')"
        """
        return "{0}({1})".format(self.__class__.__name__,
                                repr(self.name))

    def __str__(self):
        """String representation of the player.

        >>> str(Player("Lancelot"))
        'Lancelot'
        """
        return str(self.name)


# Test

if __name__ == "__main__":
    import doctest
    doctest.testmod()
