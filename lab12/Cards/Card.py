# Card.py
# A module to impliment basic card functionality
# Includes classes Rank, Suit, and Card
#
# I. H. McCreery
# 14 January 2010

class Rank:
    """The rank of a card.

    Takes in an integer or string
    as long as input is valid.  Raises a ValueError if it is not.  Can
    be compared with standard int binary comparisons (<, <=, =, !=, >=, >).
    Also provides a str() function.

    >>> Rank(5)
    Rank(5)
    >>> Rank("Queen")
    Rank(12)
    >>> Rank(18)
    Traceback (most recent call last):
    ...
    ValueError: invalid argument for Rank(): 18
    >>> str(Rank(13))
    'King'
    >>> Rank(5) < Rank("Queen")
    True
    """

    # maps int values to str values
    INTS = {1:'Ace',
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
            13:'King'}

    # maps int values to str values
    STRS = {'Ace':1,
            'Two':2,
            'Three':3,
            'Four':4,
            'Five':5,
            'Six':6,
            'Seven':7,
            'Eight':8,
            'Nine':9,
            'Ten':10,
            'Jack':11,
            'Queen':12}

    def __init__(self, rank):
        if rank in self.INTS:
            self.rank = rank
        elif rank in self.STRS:
            self.rank = self.STRS[rank]
        else:
            raise ValueError("invalid argument for Rank(): "+repr(rank))

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, self.rank)

    def __str__(self):
        return self.INTS[self.rank]

    def __lt__(self, other):
        return self.rank < other.rank

    def __eq__(self, other):
        return self.rank == other.rank

    def __le__(self, other):
        return self.rank <= other.rank


class Suit:
    """The suit of a card.

    Takes in an integer or string
    as long as input is valid.  Raises a ValueError if it is not.  Can
    be compared with standard int binary comparisons (<, <=, =, !=, >=, >).
    Spades > Hearts > Diamonds > Clubs.  Also provides a str() function.

    >>> Suit(1)
    Suit(1)
    >>> Suit("Hearts")
    Suit(2)
    >>> Suit(18)
    Traceback (most recent call last):
    ...
    ValueError: invalid argument for Suit(): 18
    >>> str(Suit(3))
    'Diamonds'
    >>> Suit('Hearts') < Suit('Spades')
    True
    """

    # maps int values to str values
    INTS = {1:'Spades',
            2:'Hearts',
            3:'Diamonds',
            4:'Clubs'}

    # maps int values to str values
    STRS = {'Spades':1,
            'Hearts':2,
            'Diamonds':3,
            'Clubs':4}

    def __init__(self, suit):
        if suit in self.INTS:
            self.suit = suit
        elif suit in self.STRS:
            self.suit = self.STRS[suit]
        else:
            raise ValueError("invalid argument for Suit(): "+repr(suit))

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, self.suit)

    def __str__(self):
        return self.INTS[self.suit]

    def __lt__(self, other):
        return self.suit > other.suit

    def __eq__(self, other):
        return self.suit == other.suit

    def __le__(self, other):
        return self.suit >= other.suit


class Card:
    """A card with a suit and a rank.

    Takes in a rank value and a suit value.  Provides str() function.

    >>> Card(5, 2)
    Card(5, 2)
    >>> Card('Ace', 'Spades')
    Card(1, 1)
    >>> Card(2, 9)
    Traceback (most recent call last):
    ...
    ValueError: invalid argument for Suit(): 9
    >>> str(Card(4, 4))
    'Four of Clubs'
    """

    def __init__(self, rank, suit):
        self.rank = Rank(rank)
        self.suit = Suit(suit)

    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__,
                                   self.rank.rank,
                                   self.suit.suit)

    def __str__(self):
        return "{0} of {1}".format(self.rank, self.suit)

# Test

if __name__ == "__main__":
    import doctest
    doctest.testmod()
