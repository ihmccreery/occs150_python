# 020.py
#
# I. H. McCreery
# 28 January 2010
"""A program to solve Project Euler problem 20"""

import math

def main():
    print sum([int(x) for x in str(math.factorial(100))])

main()
