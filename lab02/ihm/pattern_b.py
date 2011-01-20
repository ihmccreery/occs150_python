# pattern_a.py
# prints Patter A as defined
# 
# I. H. McCreery
# 8 January 2010

# prompt user for integer
x = input('Please enter an integer: ')

# print pattern
for i in range(1, x+1):
    # format i and use Python's string multiplication functionality
    print ("{0} ".format(i)) * x

# for i in range(1, x+1):
    # for j in range(1, x+1):
        # print i,
    # print
