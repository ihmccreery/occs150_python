#Match.py
#Alex Amlie-Wolf
#1-16-11
#A program to test for matches with a number of marker sequences for proteins

def main():
    fName = raw_input("Enter the filename you wish to read: ")
    F = open(fName, "r")
    source = F.readline()
    source = source.strip("\n")
    pSequence = []

    for char in source:
        pSequence.append(char)

    lineCount = 0

    for line in F:
        lineCount += 1
        tSequence = []
        line = line.strip("\n")
        for char in line:
            tSequence.append(char)
        lowError = len(pSequence) #it can't possibly be wronger than every value
        bestStart = 0
        for i in range(len(pSequence) - len(tSequence)):  #starting values
            numErrors = 0
            for j in range(len(tSequence)):    #testing sequences
                if pSequence[j+i] != tSequence[j]:
                    numErrors += 1
            if numErrors < lowError:
                lowError = numErrors
                bestStart = i
        print "Sequence %d has %d error(s) at position %d."%(lineCount, lowError, bestStart)

main()
