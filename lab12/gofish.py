# gofish.py
#
# I. H. McCreery
# 15 January 2010
"""A game to play the cardgame Go Fish.

Utilizes the Cards module and extends the Player class to be effective
for the game of Go Fish.  Built for a human player to play against 1-3
computer players.
"""

import Cards
import textwrap
import random

def main():
    pass
    # Print out instructions
    intro()
    print

    # Construct list of players
    players = construct_players()
    print

    # Construct deck
    deck = Cards.Deck()
    deck.shuffle()
    # Deal
    deal(players, deck)
    for player in players:
        player.check_for_pairs()
    print

    # Play!
    turn = 1
    while deck.size():
        print "Turn {0}:".format(str(turn))
        print "Deck has {0} cards left.".format(deck.size())
        player_n = (turn-1) % len(players)
        current_player = players[player_n]
        # player asks for a rank from a asked_player
        # print "Hand:"+', '.join(str(c) for c in current_player.hand)
        asked_rank, asked_player = current_player.ask_for_rank([player for player in players if player != current_player])
        print "{0} asked for a {1} from {2}".format(current_player,
                                                    str(asked_rank),
                                                    asked_player)
        # if asked_player has card of that rank:
        try:
            card = asked_player.get_card_of_rank(asked_rank)
            current_player.draw(card)
            print "{0} got a {1} from {2}".format(current_player,
                                                  str(card),
                                                  asked_player)
            # check for pairs
            # print "Hand:"+', '.join(str(c) for c in current_player.hand)
            assert current_player.check_for_pairs()
            turn -= 1
        except ValueError as err:
            print err
            # Go Fish!
            print "Go Fish!"
            current_player.draw(deck.deal())
            # current_player draws a card
            if player.check_for_pairs():
                turn -= 1

        print
        turn += 1


def intro():
    """Introduces the game."""
    print "Go Fish!"
    print
    print '\n'.join(textwrap.wrap("Go Fish! can be played with any deck that has an even number of cards of each rank in the deck. We will play with a standard 52-card deck. The goal of the game is to collect pairs of cards that have the same rank. Whenever a player has such a pair, they are removed from her hand and placed face-up in front of the player. Play continues until all cards are used. The winner is the player that has the most pairs in front of her at the end of the game.", 79))

def construct_players():
    """Returns list of players."""

    #get human player's name
    h_name = raw_input('What is your name? ')
    # get number of players
    while True:
        try:
            player_n = int(raw_input('Against how many players would '+
                                     'you like to play (1-3)? '))
            if player_n < 1 or player_n > 3:
                raise ValueError("You can only play agaist 1-3 players.")
            break
        except ValueError as err:
            print err
            continue
    players = []
    # construct human player
    players.append(Human_Player(h_name))
    # construct computer players
    for i in range(player_n):
        players.append(Player("Computer "+str(i)))
    # return list
    return players

def deal(players, deck):
    """Deals 5 cards to each player in players."""

    print "Dealing 5 cards to each player..."
    for player in players:
        for i in range(5):
            player.draw(deck.deal())


class Player(Cards.Player):
    """A player class for the game of Go Fish!"""

    def __init__(self, name):
        super(Player, self).__init__(name)
        self.pairs = []
        self.wins = 0

    def check_for_pairs(self):
        """Places all pairs of cards (by rank) in the pairs list and prints
        the result."""

        check_again = True
        pairs = False
        while check_again:
            pops = []
            check_again = False
            for i, icard in enumerate(self.hand):
                for j, jcard in enumerate(self.hand[:i]):
                    # if card is same as any other card
                    if icard.rank == jcard.rank:
                        # pop j first in order to preserve index i
                        r = icard.rank
                        print "{0} got a pair of {1}s!".format(self.name,
                                                               str(r))
                        self.pairs.append(self.hand.pop(i))
                        self.pairs.append(self.hand.pop(j))
                        pairs = True
                        check_again = True
        return pairs

    def ask_for_rank(self, players):
        rank = random.choice(self.hand).rank
        while True:
            player = random.choice(players)
            if player == self:
                continue
            else:
                break

        return (rank, player)

    def get_card_of_rank(self, rank):
        for i, icard in enumerate(self.hand):
            if icard.rank == rank:
                return self.hand.pop(i)
        raise ValueError(self.name+" doesn't have a card of that rank.")


class Human_Player(Player):
    pass

main()
