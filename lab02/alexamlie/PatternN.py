#PatternN.py
#Alex Amlie-Wolf
#1-10-11
#A program to make Pattern N in the CS150 Lab 2

def main():

    x = input("Enter an integer: ")

    print "*",
    for j in range(x):
        print " ",
    print "*"

    for j in range(1, x+1):
        print "*",
        for i in range(1, j):
            print " ",
        print "*",
        for i in range(x-j):
            print " ",
        print "*"

    print "*",
    for j in range(x):
        print " ",
    print "*"

main()
            
