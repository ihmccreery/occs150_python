# fancy.py
# Greet the user in style.
# 
# I. H. McCreery
# 8 January 2010

# the built-in input function takes in exactly what the user types, so one would
# have to type 'Tom', rather than just Tom.  The raw_input function takes care
# of that.
first_name = raw_input('Please enter your first name: ')
nickname = raw_input('Please enter your nickname: ')
last_name = raw_input('Please enter your last name: ')

print 'Welcome back, {0} "{1}" {2}!'.format(first_name, nickname, last_name)
# In Python 3, this will look like:
# print('So, we meet again,', name+'!')
