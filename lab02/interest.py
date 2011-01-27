# interest.py
# Computes the interest in a savings account
# 
# I. H. McCreery
# 8 January 2010

print
print 'Welcome to the Interest Calculator!'
print

# prompt user for initial deposit, monthly interest rate, monthly deposit, and
# number of months to be computed
bal = input('Enter your initial savings: ')
r = input('Enter you monthly interest rate: ')
deposit = input('Enter you monthly deposit: ')
n = input('Enter the number of months to be computed: ')
print

# print initial deposit
# .2 tells python to display the number with two decimal places
# f tells python to convert the number to a float
print 'Initially, you put in ${0:.2f}'.format(bal)

for i in range(1, n+1):
    bal += bal*r + deposit
    print 'After month {0}, you would have ${1:.2f}'.format(i, bal)

print
