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
        get -- get the given card
        draw -- draws from the given deck
        play -- returns the given card
        str_hand -- returns str representation of hand
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

    def get(self, card):
        """Adds the given card to hand.

        get(card)

        >>> p = Player("Monty")
        >>> p.get(Card.Card(5, 2))
        >>> p.hand
        [Card(5, 2)]
        """
        assert isinstance(card, Card.Card)
        self.hand.append(card)

    def draw(self, deck, n=1):
        """Draws n cards from the given deck.

        draw(deck)

        If there are no more cards in the deck, prints a message
        and quits."""
        drawn = 0
        for i in range(n):
            try:
                self.get(deck.deal())
                drawn += 1
            except IndexError:
                print "There are no more cards in the deck."
                if drawn > 0:
                    print "{0} drew {1} cards.".format(self.name, drawn)
                break

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
