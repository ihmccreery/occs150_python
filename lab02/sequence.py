# sequence.py
# Lists the squares of all the integers from some starting number down to 1.
# 
# I. H. McCreery
# 8 January 2010

START_NUM = 6

# print
print 'Squares from {0} down to 1;'.format(START_NUM**2)

for i in reversed(range(1, START_NUM + 1)):
    if i != 1:
        # the comma prevents a newline from starting
        print '{0}, '.format(i**2),
    else:
        print '1'
