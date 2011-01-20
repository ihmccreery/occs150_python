#Slingshot.py
#Alex Amlie-Wolf
#1-12-11
#A program to simulate a water balloon fight

import random
import math

SPLASH_SIZE = 6
HEIGHT = 500
WIDTH = 500
g = 9.81

def main():

    x = random.randint(0, 500)
    y = random.randint(0, 500)
    print "The target is at (%d, %d)."%(x, y)

    numBalloons = 0
    while numBalloons < 10: 
        e = input("Bearing of the slingshot? ")
        angle = input("Elevation angle? ")
        velocity = input("Velocity of balloon? ")

        distance = balloonDistance(velocity, angle)

        dy = distance * math.sin(math.radians(e))
        dx = distance * math.cos(math.radians(e))

        print "The balloon travelled %f meters and landed at (%f, %f)"%(distance, dx, dy)

        if hitOrMiss(dx, dy, x, y):
            print "You hit the target using %d balloons!"%(numBalloons)
            numBalloons = 10
        else:
            print "You missed. Try again."
            print ""
            numBalloons += 1

def balloonDistance(velocity, angle):
    return (velocity*velocity)*math.sin(2*math.radians(angle))/g

def fieldDistance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def hitOrMiss(balloonX, balloonY, targetX, targetY):
    dist = fieldDistance(balloonX, balloonY, targetX, targetY)
    return (dist <= SPLASH_SIZE+6)

main()
