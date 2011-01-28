# match.py
#
# I. H. McCreery
# 27 January 2010
"""Reads in a file of protien sequences and outputs the best fits and
numbers of errors."""

def main():

    fin = raw_input("What file would you like to use: ")
    # read in file
    f = open(fin)

    # key is protien to be used as comparison
    protein = [x for x in f.readline().rstrip()]

    for i, line in enumerate(f):
        i += 1 # take care of zero-base
        key = [x for x in line.rstrip()]
        comparison = compare_protein(protein, key)
        print "Sequence {0} has {1[0]} errors at position {1[1]}.".format(i, comparison)

def compare_protein(protein, key):
    """Takes in a protein and a key.  Returns tuple of and errors and
    position for the position of best match."""
    best_errors = len(protein)
    best_position = 0
    for i in range(len(protein) - len(key)):
        errors = find_errors(protein, key, i)
        if errors < best_errors:
            best_errors = errors
            best_position = i
    return (best_errors, best_position)

def find_errors(protein, key, i):
    """Find the number of mismatched characters in protein to key (smaller)
    starting at protein index i."""
    errors = 0
    for j in range(len(key)):
        if key[j] != protein[i+j]:
            errors += 1
    return errors

main()
