# 067.py
#
# I. H. McCreery
# 4 February 2011
"""A program to solve Project Euler problem 67"""

FILE = '067.txt'

def main():

    fin = open(FILE)

    triangle = []

    for r, row in enumerate(fin):
        triangle.append([])
        for c, entry in enumerate(row.split()):
            triangle[r].append(int(entry))

    for r, row in enumerate(triangle[-2::-1]):
        r = len(triangle) - r - 2
        for c, entry in enumerate(triangle[r]):
            # print triangle[r][c]
            triangle[r][c] += max(triangle[r+1][c],
                                  triangle[r+1][c+1])

    print triangle[0][0]

main()
