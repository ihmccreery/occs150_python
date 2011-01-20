# montecarlo_pi.py
# runs a monte carlo simulation to calculate pi, and calculates the error
#
# I. H. McCreery
# 10 January 2010

import random
import math

def main():
    # introduction
    intro()
    # how many darts?
    n = get_n('How many darts would you like to throw? ')

    hits = 0
    # simulate
    i = 0
    while i < n:
        # rather than generating whole circle, just do 1st quadrant
        x = random.random() # returns a float from 0.0 to 1.0
        y = random.random()
        if distance_from_orig(x, y) < 1:
            hits += 1
        i += 1
    # calculate pi
    result = 4. * hits / n
    # calculate error
    error = math.fabs(result-math.pi) / math.pi
    # print results
    print "The value of Pi after {0} iterations is {1}".format(n, result)
    print "This value is off by {0:.3%}".format(error)

def intro():
    print """
This program calculates the value of Pi by
simulating the throwing of darts onto a round
target on a square background.
"""

def get_n(message):
    # get and return an integer, with exception handling
    while True:
        try:
            n = int(raw_input(message))
            return n
        except ValueError as err:
            print err

def distance_from_orig(x, y):
    return math.sqrt(x**2 + y**2)

main()
