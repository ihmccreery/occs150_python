#SecondConverter.py
#Alex Amlie-Wolf
#1-7-11
#A program to convert a number of seconds into hours, minutes, and seconds

def main():

    totSec = input("Enter a number of seconds: ")
    sec = totSec%60
    hours = totSec/3600
    minSec = totSec-(3600*hours)
    minutes = minSec/60
    

    print "%d seconds is equal to %d hours, %d minutes, and %d seconds." %(totSec,hours,minutes,sec)

main()
                                                                           
