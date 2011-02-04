# critter_main.py
#
# I. H. McCreery
# 2 February 2011
"""The main file for the critter lab.

Usage: python Critter/critter_main.py <Critter1> <Critter2> [...]
Where <Critter1>, etc. is the capitalized name of critters
"""
import sys
import Tkinter
import Critter

# creates list of critter classes from arguments in script call
# executes necessary imports, throws error if bad call.
CRITTER_LIST = []
for Critter_Name in sys.argv[1:]:
    critter_name = str.lower(Critter_Name)
    exec "from "+critter_name+" import "+Critter_Name
    exec "CRITTER_LIST.append({0})".format(Critter_Name)

# fighting constants
# not sure how to represent these still. . .

TITLE = 'Critter Main'

WORLD_WIDTH = 60
WORLD_HEIGHT = 50

def main():
    """The main method for the critter lab."""

    application = Tkinter.Tk()
    application.title(TITLE)

    world = Critter.World(WORLD_WIDTH, WORLD_HEIGHT, CRITTER_LIST)
    # window = Critter.Main_Window(application, world)
    # application.mainloop()

main()
