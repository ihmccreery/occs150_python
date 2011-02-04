# 002.py
#
# I. H. McCreery
# 28 January 2011
"""A program to solve Project Euler problem 2"""

def main():
    fib = [1, 1]
    sum = 0
    while fib[-1] <= 4000000:
        f = fib[-1] + fib[-2]
        fib.append(f)
        if f % 2 == 0:
            sum += f
    print sum

main()