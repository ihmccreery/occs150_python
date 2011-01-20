#Stacker.py
#Alex Amlie-Wolf
#1-13-11
#A program to draw a stack of some number of boxes specified by the user

def main():
    box = input("How many boxes do you want to draw? ")
    for i in range(box, box+3):
        printBox(i)

def printSymbols(x, c):
    for y in range(x):
        print c,
    print ""

def printBox(x):
    printSymbols(x, "*")
    for i in range(x-2):
        print "*",
        print " "*(x-2),
        print "*"
    printSymbols(x, "*")

main()
