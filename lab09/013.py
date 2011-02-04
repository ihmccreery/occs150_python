# 013.py
#
# I. H. McCreery
# 4 February 2011
"""A program to solve Project Euler problem 13"""

FILE = '013.txt'

def main():
    fin = open(FILE)
    nums = [int(x) for x in fin]
    s = sum(nums)
    print str(s)[:10]

main()
