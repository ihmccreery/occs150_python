#PatternB.py
#Alex Amlie-Wolf
#1-10-11
#A program to generate pattern B in CS150 lab #2

def main():
    x = input("Enter an integer: ")
    for j in range(1, x+1):
        for i in range(x):
            print j,
        print ""

main()
    
