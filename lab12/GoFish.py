# GoFish.py
# The game of Go Fish!
#
# I. H. McCreery
# 12 January 2010

import random
from Cards import Card, Deck, _RANKS


# main

# Turn class

class Request:
    "A simple request consisting of a Rank and a Player"
    
    def __init__(self, player, rank):
        self._player = player
        self._rank = rank

    @property
    def rank(self):
        return self._rank
        
    @property
    def player(self):
        return self._player

    def __str__(self):
        return "{rank} from {player}".format(rank=_RANKS[self._rank],
                                             player=self._player)

    def __repr__(self):
        return "{name}({player}, {rank})".format(name=
                                                 self.__class__.__name__,
                                                 player=repr(self._player),
                                                 rank=repr(self._rank))


# Player class

class Player:
    """A computer-based player of a card game"""

    def __init__(self, name):
        self._name = str(name)
        self._hand = []

    def __str__(self):
        return self._name

    def __repr__(self):
        return "{self}({name})".format(self=self.__class__.__name__,
                                       name=repr(self._name))

    def getcard(self, card):
        assert isinstance(card, Card), 'card must be of type Card'
        self._hand.append(card)

    def playcard(self):
        # just return a random card
        return self._hand.pop(random.randrange(len(self._hand)))

    def givecard(self, rank):
        assert rank in _RANKS, 'rank must be of type Rank'
        for card in self._hand:
            if card.rank == rank:
                return card
        raise ValueError
