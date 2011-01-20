#MonteCarloPi.py
#Alex Amlie-Wolf
#1-11-11
#A program to approximate pi by a random dart throwing (Monte Carlo) method

from random import *
from math import *

def main():
    print "This program approximates pi by a Monte Carlo method."
    n = input("How many darts do you want to throw? ")

    hits = 0
    
    for i in range(n):
        x = uniform(-1, 1)  #this returns a random float between -1 and 1
        y = uniform(-1, 1)
        if simpleDistance(x, y) <= 1:
            hits += 1
            
    inTarget = float(hits) / n
    piApprox = 4*inTarget*1.0
    print "The value of Pi after %d iterations is %f."%(n, piApprox)
    error = ((piApprox-pi)/pi)*100.0
    print "This is off by %f percent from the value of pi."%(error)

def simpleDistance(x, y):
    return hypot(x, y)  #this is a method for finding the hypotenuse of a triangle but it is the same formula we want in this case
                        #we could also use math.sqrt(x*x + y*y), I like this method

main()
