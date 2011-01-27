# primes.py
#
# I. H. McCreery
# 10 January 2010

import math

def main():
    """Generates prime numbers and counts twin primes"""

    num_primes = input("How many primes: ")
    primes = []
    twin_primes = []
    p = 2
    while len(primes) < num_primes:
        if is_prime(p):
            if len(primes) > 0 and p - 2 == primes[-1]:
                twin_primes.append((primes[-1], p))
            primes.append(p)
        p += 1
    print "The first {0} primes are:".format(num_primes)
    print ", ".join(str(x) for x in primes)
    print "Amongst these, there are {0} twin prime pairs:".format(len(twin_primes))
    print ", ".join(str(x) for x in twin_primes)


def is_prime(n):
    """Returns true if n is prime, else returns false."""

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

main()
