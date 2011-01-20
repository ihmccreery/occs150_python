# pattern_a.py
# prints Patter A as defined
# 
# I. H. McCreery
# 8 January 2010

# prompt user for integer
x = input('Please enter an integer: ')

# print pattern
# print top line
print '*' * (x+2)
# print first section
for i in range(0, x):
    print '*'
# print middle line
print '*' * (x+1)
# print second section
for i in range(0, x):
    print '*'
# print bottom line
print '*' * (x+2)
