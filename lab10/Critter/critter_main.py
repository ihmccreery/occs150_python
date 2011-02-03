# critter_main.py
#
# I. H. McCreery
# 2 February 2011
"""The main file for the critter lab."""

import Tkinter
import collections

# directional constants
# tuples in the form (delta_x, delta_y)
# note that north is down, like in standard image representation

Location = collections.namedtuple('Location', 'x y')

NORTH = Location(0, -1)
NORTHEAST = Location(1, -1)
EAST = Location(1, 0)
SOUTHEAST = Location(1, 1)
SOUTH = Location(0, 1)
WEST = Location(-1, 0)
CENTER = Location(0, 0)

# fighting constants
# not sure how to represent these still. . .

ROAR = 0
POUNCE = 1
SCRATCH = 2

TITLE = 'Critters'

WORLD_WIDTH = 60
WORLD_HEIGHT = 50


def main():
    """The main method for the critter lab.

    This creates a GUI for the user to run the simulations.
    """
    # unclear to me right now how to include the critters necessary
    application = Tkinter.Tk()
    application.title(TITLE)

    world = World(WORLD_WIDTH, WORLD_HEIGHT, [])
    # window = MainWindow(application, world)
    # application.mainloop()


class MainWindow(Tkinter.Frame):
    """The main window"""

    def __init__(self, parent, world):

        # call super initializer
        # Frame may not be new-style class, so super() fails
        Tkinter.Frame.__init__(self, parent)

        self.parent = parent # keep reference of parent for later use
        self.world = world

        self.grid(row=0, column=0)

        # initialize variables
        self.stop()
        self.reset()
        self.speed = 1

        # initialize MainWindow widgets
        world_canvas = Tkinter.Canvas(self, width=712, height=600)
        sidebar = Tkinter.Frame(self)

        # layout MainWindow widgets
        world_canvas.grid(row=0, column=0)
        sidebar.grid(row=0, column=1, sticky=Tkinter.E)

        # initialize sidebar widgets
        critter_list = Tkinter.Frame(sidebar)
        turn_frame = Tkinter.Frame(sidebar)
        speed_frame = Tkinter.Frame(sidebar)
        go_button = Tkinter.Button(sidebar, text="Go")
        stop_button = Tkinter.Button(sidebar, text="Stop")
        reset_button = Tkinter.Button(sidebar, text="Reset")

        # layout sidebar widgets
        critter_list.grid(row=0, column=0)
        turn_frame.grid(row=1, column=0)
        speed_frame.grid(row=2, column=0)
        go_button.grid(row=3, column=0, sticky=Tkinter.EW)
        stop_button.grid(row=4, column=0, sticky=Tkinter.EW)
        reset_button.grid(row=5, column=0, sticky=Tkinter.EW)

        # initialize turn_frame and speed_frame widgets
        turn_label = Tkinter.Label(turn_frame, text="Turn")
        turn_display = Tkinter.Label(turn_frame, text=self.turn)
        speed_label = Tkinter.Label(speed_frame, text="Speed")
        speed_scale = Tkinter.Scale(speed_frame, variable=self.speed, from_=1, to=20, resolution=1, orient=Tkinter.HORIZONTAL)

        # layout turn_frame and speed_frame widgets
        turn_label.grid(row=0, column=0, sticky=Tkinter.W)
        turn_display.grid(row=0, column=1)
        speed_label.grid(row=0, column=0, sticky=Tkinter.W)
        speed_scale.grid(row=0, column=1)

    def reset_game(self):
        """Sets or resets the game to start over."""
        pass

    def go(self):
        """Plays the game."""
        self.state = True

    def stop(self):
        """Stops the game."""
        self.state = False

    def reset(self):
        """Resets the game to beginning."""
        self.turn = 0


class World(object):
    """Represents the world in which the creatures interact."""

    def __init__(self, width, height, critter_list):

        # perhaps turn these into properties, but probably not worth it
        self.width = width
        self.height = height

        self._grid = Grid(width, height, default=[])

        self.populate(critter_list)

    def populate(self, critter_list):
        pass

    def turn(self):
        pass


class Grid(object):
    """A simple 2D nested-list structure

    g = Grid(width=20, height=40, default=[])
    default is the object that each entry contains when initialized.

    An entry is accessed as follows:
    g(1, 2) = 5
    g(3, 5).append(17)
    """

    def __init__(self, width, height, default=None):
        self.width = width
        self.height = height
        self._field = [[default for y in range(height)]
                                for x in range(width)]

    def __getitem__(self, x, y):
        return self._field[x][y]

    def __setitem__(self, x, y):
        return self._field[x][y]

main()
