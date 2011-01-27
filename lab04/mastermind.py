# mastermind.py
#
# I. H. McCreery
# 10 January 2010

import random

NUM_TURNS = 10
NUM_PEGS = 4
COLORS = ('R', 'B', 'G', 'Y', 'O', 'P')

def main():
    """Plays the game of mastermind with you."""

    intro()
    code = generate_code()

    solved = False
    turn = 0
    while (not solved) and turn <= NUM_TURNS:
        turn += 1
        guess = get_guess()
        solved = clue(code, guess)
    if solved:
        print "Good job!"
    else:
        print "Sorry, you ran out of guesses."
    print

def intro():
    print
    print "I have a {0}-letter code made from {1} colours.".format(NUM_PEGS, len(COLORS))
    print "The colors are: "+', '.join(COLORS[0:-1])+", and", COLORS[-1]
    print

def generate_code():
    """Generates the codemaker's code and returns it as a list."""
    code = []
    for i in range(NUM_PEGS):
        code.append(random.choice(COLORS))
    return code

def print_code(code):
    print ''.join(code)

def get_guess():
    """Gets a valid guess from player and returns a list."""
    while True:
        try:
            guess = raw_input("Your guess: ")
            if not all([(x.capitalize() in COLORS) for x in guess]):
                raise ValueError("Invalid input: {0}".format(guess))
            return [x.capitalize() for x in guess]
        except ValueError as err:
            print err
            continue

def clue(code, guess):
    """Checks guess against code.  Prints out number of white and black
    pegs, and returns True if the guess equals the code."""

    code = [x for x in code]
    black = 0
    white = 0

    # check for black pegs (color AND position are correct)
    for i, peg in enumerate(guess):
        # print peg
        if peg == code[i]:
            black += 1
            code[i] = 'code_black'
            guess[i] = 'guess_black'

    # check for white pegs (color is correct, position is wrong)
    for g, guess_peg in enumerate(guess):
        for c, code_peg in enumerate(code):
            # print guess_peg, ":", code_peg
            if guess_peg == code_peg:
                white += 1
                code[c] = 'code_white'
                guess[g] = 'guess_white'

    if black == NUM_PEGS:
        return True
    else:
        print "Not quite.  You got {0} black pegs and {1} white pegs.".format(black, white)
        print
        return False


main()
