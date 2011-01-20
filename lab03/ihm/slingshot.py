# slingshot.py
# 
# A program to simulate a large water balloon slingshot located at the Northwest
# corner of Tappan Square in Oberlin, OH.
# 
# I. H. McCreery
# 10 January 2010

import random
import math

SPLASH_SIZE = 6

MAX_TRIES = 10

HEIGHT = 500
WIDTH = 500
G = 9.8

def main():
    # intro
    intro()

    # generate target
    target_x = random.randint(0, WIDTH)
    target_y = random.randint(0, HEIGHT)

    # print target coordinates
    print "The target is at ({0}, {1}).".format(target_x, target_y)
    print

    tries = 0
    hit = False

    while tries < MAX_TRIES:
        tries += 1

        # request bearing, elevation, velocity
        bearing = math.radians(get_n("Bearing for slingshot (degrees): "))
        velocity = get_n("Balloon velocity: ")
        angle = math.radians(get_n("Elevation angle (degrees): "))
        print "           |           "
        print "           V           "

        # calculate coordinates and output
        d = balloon_distance(velocity, angle)
        balloon_x = d * math.cos(bearing)
        balloon_y = d * math.sin(bearing)
        d_between = field_distance(target_x, target_y, balloon_x, balloon_y)
        
        print "Balloon traveled {0:.4} meters and hit ({1:.4}, {2:.4}).".format(d, balloon_x, balloon_y)
        if d_between <= SPLASH_SIZE:
            print "Hit!!"
            print
            hit = True
            break
        else:
            print "You missed by {0:.4} meters.".format(d_between)
            print

    if hit:
        print "You hit the target in just {0} tries!".format(tries)
    else:
        print "Sorry, you only had {0} balloons.  You lose.".format(MAX_TRIES)
    print
    
    # Fin!

def intro():
    print """
Welcome to the Water Balloon Slingshot Fun!

    You've got a water balloon slingshot in the corner of
    Tappan Square.  A friend has placed a target somewhere
    in the field.  See how quickly you can hit it!  You have
    {0} balloons.
    
    [Slingshot is at 0,0 and bearing is angle South from due East.]
""".format(MAX_TRIES)

def get_n(message):
    # get and return an integer, with exception handling
    while True:
        try:
            # use raw_input so input is not mistaken for an object ref
            n = float(raw_input(message))
            return n
        except ValueError as err:
            print err

def balloon_distance(velocity, angle):
    return velocity**2 * math.sin(2*angle)/G

def field_distance(x1, y1, x2, y2):
    rad = (x2-x1)**2 + (y2-y1)**2
    return math.sqrt(rad)

main()
