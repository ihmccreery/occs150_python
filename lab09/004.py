# 004.py
#
# I. H. McCreery
# 28 January 2011
"""A program to solve Project Euler problem 4"""

def main():
    ans = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if palindrome(str(prod)) and prod > ans:
                ans = prod
    print ans

def palindrome(s):
    """Check if a string is a palindrome"""
    try:
        return s[0] == s[-1] and palindrome(s[1:-1])
    except IndexError:
        return True

main()
