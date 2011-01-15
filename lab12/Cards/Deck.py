# Deck.py
#
# I. H. McCreery
# 14 January 2010
"""A module to impliment basic deck functionality
Includes classes Deck, EuchreDeck, and BlackjackDeck

>>> Deck().deal()
[Card(1, 1)]
>>> Deck().deal(3)
[Card(1, 1), Card(2, 1), Card(3, 1)]
"""

import random
from Card import Rank, Suit, Card

class Deck(object):
    """A basic, 52-card deck with 13 of each of 4 suits.

    Functions:
    deal -- returns list of the next card(s)
    shuffle -- shuffles the deck
    size -- returns number of cards in deck

    >>> Deck()
    Deck()
    """

    def __init__(self):
        """Initializer function

        >>> Deck()
        Deck()
        """
        self.stack = []
        self.populate()

    def __repr__(self):
        return "{0}()".format(self.__class__.__name__)

    def __str__(self):
        return self.__repr__

    def deal(self, n=1):
        """Returns first n card(s) in deck.

        deal([n]): if n is not specified, returns a list of 1 card.
        If n is specified, returns a list of n cards.

        >>> Deck().deal()
        [Card(1, 1)]
        >>> Deck().deal(3)
        [Card(1, 1), Card(2, 1), Card(3, 1)]
        """

        card_list = []
        for i in range(n):
            card_list.append(self.stack.pop(0))
        return card_list

    def populate(self, replace=False):
        """Populates deck with standard 52 cards.

        populate([replace]): if replace is set to True, the current deck
        is replaced with a new standard deck.
        """
        for suit in Suit.INTS:
            for rank in Rank.INTS:
                self.stack.append(Card(rank, suit))

    def shuffle(self):
        """Shuffles the deck.

        Employs random.shuffle function.
        """

        random.shuffle(self.stack)

    def size(self):
        """Returns the number of cards in the deck.

        >>> Deck().size()
        52
        """

        return len(self.stack)


class EuchreDeck(Deck):
    """A deck for playing Euchre.

    Only 9s, 10s, Jacks, Queens, Kings, and Aces.

    >>> EuchreDeck().size()
    24
    """

    def __init__(self):
        """The initializer function

        >>> EuchreDeck().size()
        24
        """

        super(EuchreDeck, self).__init__()
        newstack = []
        for i, card in enumerate(self.stack):
            if not Rank(1) < card.rank < Rank(9):
                newstack.append(self.stack[i])
        self.stack = newstack


class BlackjackDeck(Deck):
    """A deck for playing Blackjack.

    Initializer takes 1 optional argument, shoes, which indicates
    how many 52-card decks are used to assemble the Blackjack deck.
    Number of shoes defaults to 1.

    >>> BlackjackDeck().size()
    52
    >>> BlackjackDeck(2).size()
    104
    """

    def __init__(self, shoes=1):
        """Initializer function

        >>> BlackjackDeck().size()
        52
        >>> BlackjackDeck(2).size()
        104
        """

        super(BlackjackDeck, self).__init__()
        self.shoes = shoes
        for i in range(shoes-1):
            self.populate()

    def __repr__(self):
        if self.shoes != 1:
            return "{0}({1})".format(self.__class__.__name__,
                                     self.shoes)
        else:
            return super(BlackjackDeck, self).__repr__()


# Test

if __name__ == "__main__":
    import doctest
    doctest.testmod()
