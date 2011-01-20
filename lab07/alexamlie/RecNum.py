#RecNum.py
#Alex Amlie-Wolf
#1-17-11
#A program to do recursive computation on numbers

def main():
    x = input("Enter your non-negative integer x: ")
    k = input("Enter your non-negative integer k: ")
    p = power(x, k)
    print "%d raised to the power of %d is %d."%(x, k, p)
    ss = squareSum(x)
    print "The sum of the first %d perfect squares is %d."%(x, ss)
    c = choose(x, k)
    print "%d choose %d is equal to %d."%(x, k, c)
    

def power(x, k):
    if k == 0:
        return 1
    else:
        return x * power(x, k-1)

def squareSum(x):
    if x == 1:
        return 1
    else:
        return x**2 + squareSum(x-1)

def choose(x, k):
    if k > x:
        return 0
    elif k == x:
        return 1
    elif k == 0:
        return 1
    else:
        return choose(x-1, k) + choose(x-1, k-1)

main()
