#PatternA.py
#Alex Amlie-Wolf
#1-10-11
#A program to generate pattern A in the CS150 Lab #2

def main():
    x = input("Enter an integer: ")
    for j in range(x):
        for i in range(1, x+1):
            print i,
        print ""

main()
