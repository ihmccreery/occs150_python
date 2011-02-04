# 006.py
#
# I. H. McCreery
# 28 January 2011
"""A program to solve Project Euler problem 6"""

def main():

    r = range(1, 101)

    sum_sq = sum(x**2 for x in r)
    sq_sum = (sum(r))**2

    ans = sq_sum - sum_sq
    print ans

main()
