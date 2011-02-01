# 009.py
#
# I. H. McCreery
# 28 January 2010
"""A program to solve Project Euler problem 9"""

import math

class Found(Exception):
    pass

def main():
    b = 1
    try:
        while True:
            for a in range(1, b):
                c = math.hypot(a, b)
                if math.fmod(c, 1) == 0:
                    if a + b + c == 1000:
                        raise Found(int(a*b*c))
            b += 1
    except Found as err:
        print err


main()
