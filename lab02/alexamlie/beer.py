# beer.py
# Prints out the verses of the song 'Ninety-Nine Bottles of Beer on the
# Wall'
# 
# I. H. McCreery
# 8 January 2010

# static variables, by convention, are declared as UPPERCASE
START_BOTTLES = 99

# see notes02.txt for more on for-loops in Python
for i in reversed(range(3, START_BOTTLES + 1)):
    print '''
{0} bottles of beer on the wall,
{0} bottles of beer!
Take on down, pass it around,
{1} bottles of beer on the wall!'''.format(i, i-1)

# special case to take care of grammar
print '''
2 bottles of beer on the wall,
2 bottles of beer!
Take one down, pass it around
1 bottle of beer on the wall!

1 bottle of beer on the wall,
1 bottle of beer!
Take one down, pass it around,
No more bottles of beer on the wall!
'''
