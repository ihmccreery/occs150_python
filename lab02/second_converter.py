# SecondConverter.java
# Translate seconds into a more readable hours, minutes, and seconds.
# 
# I. H. McCreery
# 8 January 2010

# Explain via console output what this program does.
print '''
Welcome to my Second Converter!

This program will properly calculate the number of
minutes and seconds under 60 from a given number of seconds.
'''

# Assign variable sec to user's number of seconds from the console.
# (You may want to look back at lab01 on how to get user input.)
s = input('How many seconds have you got? ')

# Compute and assign hours, mins, and seconds from the user's input.
hour = s // 3600
minute = s % 3600 // 60
second = s % 3600 % 60

# Print the results.
print '{0} seconds is equal to {1} hours, {2} minutes, and {3} seconds.'.format(s, hour, minute, second)
