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

class CardNotInHandError(Exception):
    """Custom exception for a player not having a card in his hand"""

    def __init__(self, msg):
        super(CardNotInHandError, self).__init__(msg)


# -----------------------
# --- main method -------
# -----------------------


def main():

    # Print out instructions
    print
    intro()
    print

    play_again = True

    while play_again:

        # Construct list of players
        players = construct_players()
        print

        # Construct deck
        deck = Cards.Deck()
        deck.shuffle()
        # Deal
        deal(players, deck)
        print

        # Play!
        turn = 1
        while all([p.hand for p in players]) or deck.size():
            print "Turn {0}:".format(str(turn))

            # decide who's turn it is (current_player)
            player_n = (turn-1) % len(players)
            current_player = players[player_n]
            current_player.check_if_out(deck)
            another_turn = True

            while another_turn and (all([p.hand for p in players]) or deck.size()):
                another_turn = False
                # player asks for a rank from a asked_player
                asked_rank, asked_player = current_player.ask_for_rank([player for player in players if player != current_player])
                print "{0} asked for a {1} from {2}".format(current_player,
                                                            str(asked_rank),
                                                            asked_player)

                # try to get a card of that rank
                try:
                    card = asked_player.return_card_of_rank(asked_rank)
                    current_player.get(card)
                    print "{0} got a {1} from {2}".format(current_player,
                                                          str(card),
                                                          asked_player)
                    current_player.check_for_pairs(deck)
                    another_turn = True
                # if there is no card of that rank
                except CardNotInHandError as err:
                    # player didn't have card asked for
                    print err
                    # Go Fish!
                    print "Go Fish!"
                    current_player.draw(deck)
                    # current_player draws a card
                    if current_player.check_for_pairs(deck):
                        another_turn = True

            print
            turn += 1

        # print results
        get_winner(players)
        print
        play_again = ask_play_again()
        print


# -----------------------
# --- helper methods ----
# -----------------------


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

    print "Dealing..."
    for player in players:
        player.draw(deck, 5)
        player.check_for_pairs(deck)

def get_winner(players):
    """Takes in a list of players and determines the winner based
    on len(player.pairs)"""
    winner = players[0]
    for player in players:
        pairs = len(player.pairs) / 2
        print "{0} has {1} pairs.".format(player.name,
                                          pairs)
        if pairs > len(winner.pairs)/2:
            winner = player
    winner.wins += 1
    print
    print "{0} wins!".format(winner)

def ask_play_again():
    while True:
        i = raw_input("Would you like to play again (y/n)? ")
        if i == 'y':
            return True
        elif i == 'n':
            return False
        else:
            print "Not a valid input: {0}".format(repr(i))
            continue


# -----------------------
# ------ classes --------
# -----------------------


class Player(Cards.Player):
    """A player class for the game of Go Fish!"""

    def __init__(self, name):
        super(Player, self).__init__(name)
        self.pairs = []
        self.wins = 0

    def check_for_pairs(self, deck):
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
                        self.check_if_out(deck)
                        pairs = True
                        check_again = True
                        break
        return pairs

    def check_if_out(self, deck):
        "Checks to see if hand is out, and draws 5 cards if possible"
        if len(self.hand) == 0:
            print "{0} is out of cards.".format(self)
            self.draw(deck, 5)

    def ask_for_rank(self, players):
        rank = random.choice(self.hand).rank
        player = random.choice(players)
        return (rank, player)

    def return_card_of_rank(self, rank):
        for i, icard in enumerate(self.hand):
            if icard.rank == rank:
                return self.hand.pop(i)
        raise CardNotInHandError(self.name+
                                 " doesn't have a card of that rank.")


class Human_Player(Player):

    def ask_for_rank(self, players):
        # print hand
        print "Your hand: "+self.str_hand()
        # from whom to pick?
        if len(players) == 1:
            player = players[0]
        else:
            player_message = "From whom would you like to pick (1-{0})? ".format(
                                                                len(players))
            while True:
                try:
                    player = players[int(raw_input(player_message))-1]
                    break
                except (IndexError, ValueError) as err:
                    print err
                    continue
        # for what to ask?
        while True:
            try:
                rank = Cards.Rank(raw_input("For what rank would you like to ask? "))
                if rank not in [c.rank for c in self.hand]:
                    raise ValueError("That rank is not in your hand.")
                break
            except ValueError as err:
                print err
                continue

        return (rank, player)


main()
