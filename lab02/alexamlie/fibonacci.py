# fibonacci.py
# prompts the user to enter a positive integer x > 2, and then prints the xth 
# Fibonacci number
# 
# I. H. McCreery
# 8 January 2010

print 'My incredible Fibonacci number generator!'

# prompt user for integer
p = input('Please enter an integer > 2: ')

f0 = 0
f1 = 1
# here we see an declaration statement without assignment
f2 = int()

# compute
for i in range(2, p+1):
    f2 = f0 + f1
    f0 = f1
    f1 = f2

# print
if p == 3:
    print 'The {0}rd number in the Fibonacci sequence is {1}.'.format(p, f1)
else:
    print 'The {0}th number in the Fibonacci sequence is {1}.'.format(p, f1)
