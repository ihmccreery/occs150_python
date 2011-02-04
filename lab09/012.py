# 012.py
#
# I. H. McCreery
# 4 February 2011
"""A program to solve Project Euler problem 12"""

import math

MIN = 500

class Finished(Exception):
    pass

def main():
    n = 1
    tri_list = [0]
    try:
        while True:
            tri_list.append(n+tri_list[n-1])
            d = divisors(tri_list[n])
            print "trying:", tri_list[n], "-", d, "divisors"
            if divisors(tri_list[n]) > MIN:
                raise Finished
            n += 1
    except Finished:
        print tri_list[n]

def divisors(n):
    div = []
    for i in range(1, int(math.sqrt(n)+1)):
        if n % i == 0:
            div.append(i)
            if i != n/i:
                div.append(n/i)
    return len(div)

main()
