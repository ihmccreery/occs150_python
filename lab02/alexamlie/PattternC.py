#PatternC.py
#Alex Amlie-Wolf
#1-10-11
#A program to make Pattern C in the CS150 Lab 2

def main():

    x = input("Enter an integer: ")
    for j in range(1, x+1):
        for i in range(j, x+1):
            print i,
        print ""

main()
