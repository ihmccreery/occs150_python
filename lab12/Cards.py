# Cards.py
# A module to impliment card-game functionality
#
# I. H. McCreery
# 12 January 2010

import random

# Rank constants
_RANKS = {
    1:'Ace',
    2:'Two',
    3:'Three',
    4:'Four',
    5:'Five',
    6:'Six',
    7:'Seven',
    8:'Eight',
    9:'Nine',
    10:'Ten',
    11:'Jack',
    12:'Queen',
    13:'King',
}

# suit constants
_SUITS = {
    1:'Spades',
    2:'Hearts',
    3:'Diamonds',
    4:'Clubs',
}


def InvalidRankError(Exception):
    pass


def InvalidSuitError(Exception):
    pass


class Card:
    """Card(rank, suit)

A card with a rank and a suit

If an invalid rank or suit is passed, an
InvalidRankError or InvalidSuitError will
be raised.  See Card.rank and Card.suit."""

    def __init__(self, rank, suit):
        # Assign rank
        if rank not in _RANKS: # if rank is not a valid numeric rank
            for k, v in _RANKS.items():
                if v == rank:
                    rank = k
            else:
                raise InvalidRankError
        self._rank = rank

        # assign suit
        if suit not in _SUITS: # if suit is not a valid numeric suit
            for k, v in _SUITS.items():
                if v == suit:
                    suit = k
            else:
                raise InvalidSuitError
        self._suit = suit

    @property
    def rank(self):
        """
The card's rank, represented by an int.  A string
may also be provided:

'Ace': 1
'Two': 2
'Three': 3
'Four': 4
'Five': 5
'Six': 6
'Seven': 7
'Eight': 8
'Nine': 9
'Ten': 10
'Jack': 11
'Queen': 12
'King': 13
"""
        return self._rank

    @property
    def suit(self):
        """
The card's suit, represented by an int.  A string
may also be provided:

'Spades': 1
'Hearts': 2
'Diamonds': 3
'Clubs': 4
"""
        return self._suit

    def __str__(self):
        return "{rank} of {suit}".format(rank=_RANKS[self.rank],
                                         suit=_SUITS[self.suit])

    def __repr__(self):
        return "{name}({rank}, {suit})".format(name=
                                               self.__class__.__name__,
                                               rank=self.rank,
                                               suit=self.suit)


class Deck:
    """Deck(shoes=1)

A standard deck with (default) 52 cards"""
    
    def __init__(self, shoes=1):
        self._shoes = shoes
        self._stack = []
        for shoe in range(shoes):
            for suit in _SUITS:
                for rank in _RANKS:
                    self._stack.append(Card(rank, suit))

    def size(self):
        return len(self._stack)

    def is_empty(self):
        return self.size() == 0

    def deal(self, index=0):
        return self._stack.pop(index)

    def shuffle(self):
        random.shuffle(self._stack)

    def __str__(self):
        return ", ".join(str(k) for k in self._stack)

    def __repr__(self):
        if self._shoes == 1:
            return "{name}()".format(name=self.__class__.__name__)
        return "{name}(shoes={shoes})".format(name=self.__class__.__name__,
                                              shoes=self._shoes)


# Variations of Deck

class EurcheDeck(Deck):

    def __init__(self):
        super.__init__()
        for i, card in enumerate(self._stack):
            if 1 < card.rank < 9:
                self.deal(i)


class BlackjackDeck(Deck):
    pass
