#RecStr.py
#1-17-11
#Alex Amlie-Wolf
#A program for string recursion

def main():
    s = raw_input("Enter a string s: ")
    t = raw_input("Enter a string t: ")
    print "The string %s backwards is %s."%(s, back(s))
    if palin(s):
        print "The string %s is a palindrome."%(s)
    else:
        print "The string %s is not a palindrome."%(s)
    if(subseq(s, t)):
        print "The string %s is a subsequence of %s."%(t, s)
    else:
        print "The string %s is not a subsequence of %s."%(t, s)

def back(s):
    if len(s) == 0:
        return s
    else:
        t = s[len(s)-1]
        s = s[:len(s)-1]
        return t + back(s)

def palin(s):
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[len(s)-1]:
        return palin(s[1:len(s)-1])
    else:
        return False

def subseq(s, t):
    if len(t) == 0:
        return True
    if len(t) > len(s):
        return False
    if s[0] == t[0]:
        return subseq(s[1:], t[1:])
    else:
        return subseq(s[1:], t)

main()
