#PatternE.py
#Alex Amlie-Wolf
#1-10-11
#A program to make Pattern E in CS150 Lab 2

def main():

    x = input("Enter an integer: ")
    for i in range(x+2):
        print "*",
    print ""

    for i in range(x):
        print "*"

    for i in range(x+1):
        print "*",
    print ""
    
    for i in range(x):
        print "*"

    for i in range(x+2):
        print "*",
    print ""

main()
