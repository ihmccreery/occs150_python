# pattern_a.py
# prints Patter A as defined
# 
# I. H. McCreery
# 8 January 2010

# prompt user for integer
x = input('Please enter an integer: ')

# print pattern
# print top
print '*'+(' '*x)+'*'
# print middle
for i in range(0, x):
    print '*'+(' '*i)+'*'+(' '*(x-i-1))+'*'
# print bottom
print '*'+(' '*x)+'*'
