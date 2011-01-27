# greet.py
# Greet the user.
# 
# I. H. McCreery
# 8 January 2010

# the built-in input function takes in exactly what the user types, so one would
# have to type 'Tom', rather than just Tom.  The raw_input function takes care
# of that.
name = raw_input('Please enter your name: ')

# The following could also be written as such:
# print 'So, we meet again, '+name+'!'
# print 'So, we meet again, %s!' % name
# print 'So, we meet again, {0}!'.format(name)
print 'So, we meet again,', name+'!'
# In Python 3, this will look like:
# print('So, we meet again,', name+'!')
