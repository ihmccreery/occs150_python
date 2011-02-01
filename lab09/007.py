# 007.py
#
# I. H. McCreery
# 28 January 2010
"""A program to solve Project Euler problem 7"""

import math

def main():
    primes = [2]
    i = 3
    while len(primes) < 10001:
        if prime(i):
            primes.append(i)
        i += 2
    print primes[10000]

def prime(n):
    """Check if a number is prime"""
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

main()
