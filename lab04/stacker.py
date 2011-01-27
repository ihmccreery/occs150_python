# stacker.py
#
# I. H. McCreery
# 27 January 2010

def main():
    """Draws a stack of some number of boxes as specified by the user."""
    n = input("How many boxes: ")
    for i in range(3, n+3):
        print_box(i)

def print_symbols(n, c):
    """prints char c, n times."""
    print c*n;

def print_box(n):
    """prints a box of size n."""
    print '*' * n
    for i in range(n-2):
        print '*'+' ' * (n-2)+'*'
    print '*' * n

main()
