#Greetings.py
#Alex Amlie-Wolf
#1-5-2011
#A program to prompt for the users name and prints a message to them

def main():
    print "What is your name?",
    name = raw_input()
    if name == 'Alex':
        print "Alex is the best name ever."
    else:
        print "Hello, " + name + "!"
    print "Goodbye."

main()
