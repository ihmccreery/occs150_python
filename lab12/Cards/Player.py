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

import Card

# a list for importing module
__all__ = ['Player']

class Player(object):
    """Basic player class.

    Impliments:
        draw -- draw the given card
    """

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

    def draw(self, card):
        """Draws the given card list.

        draw(card_list)

        >>> p = Player("Monty")
        >>> p.draw(Card.Card(5, 2))
        >>> p.hand
        [Card(5, 2)]
        """
        assert isinstance(card, Card.Card)
        self.hand.append(card)

    def play(self, card):
        """Plays the given card.

        play(card) -> returns card if card is in hand.
                      returns ValueError if card is not in hand.
        """
        for i, my_card in enumerate(self.hand):
            if card == my_card:
                return self.hand.pop(i)
        return ValueError(self.name+": sorry, I don't have that card.")

    def str_hand(self):
        """Prints player's hand in human-readable format."""
        return ", ".join(str(c) for c in self.hand)


# Test

if __name__ == "__main__":
    import doctest
    doctest.testmod()
