# 011.py
#
# I. H. McCreery
# 3 February 2011
"""A program to solve Project Euler problem 11"""

FILE = '011.txt'

def main():
    fin = open(FILE)

    # construct grid
    grid = []
    for r, line in enumerate(fin):
        grid.append([])
        for c, entry in enumerate(line.split()):
            grid[r].append(int(entry))

    maximum = grid[0][0]

    for r in range(len(grid[0:-3])):
        for c in range(len(grid[r][0:-3])):
            rt = right(r, c, grid)
            dn = down(r, c, grid)
            rd = rightdown(r, c, grid)
            m = max([rt, dn, rd])
            if m > maximum:
                maximum = m
        for c in range(len(grid[r][3:])):
            c += 3 # to correct for starting at third row
            ld = leftdown(r, c, grid)
            if ld > maximum:
                maximum = ld

    print maximum

def right(r, c, grid):
    prod = 1
    for i in range(4):
        prod *= grid[r][c+i]
    return prod

def down(r, c, grid):
    prod = 1
    for i in range(4):
        prod *= grid[r+i][c]
    return prod

def rightdown(r, c, grid):
    prod = 1
    for i in range(4):
        prod *= grid[r+i][c+i]
    return prod

def leftdown(r, c, grid):
    prod = 1
    for i in range(4):
        prod *= grid[r+i][c-i]
    return prod


main()
