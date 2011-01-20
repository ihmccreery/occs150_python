#PatternD.py
#Alex Amlie-Wolf
#1-10-11
#A program to make Pattern D in CS150 Lab02

def main():
    x = input("Enter an integer: ")
    for i in range(1, x+1):
        for j in range(1, i+1):
            for y in range(j):
                print j,
        print ""

main()
