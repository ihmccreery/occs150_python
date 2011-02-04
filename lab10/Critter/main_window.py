# main_window.py
#
# I. H. McCreery
# 2 February 2011
"""The MainWindow class for the critters"""

import Tkinter

class Main_Window(Tkinter.Frame):
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
        self.world.reset()

    def go(self):
        """Plays the game."""
        self.state = True

    def stop(self):
        """Stops the game."""
        self.state = False

    def reset(self):
        """Resets the game to beginning: repopulates critters, resets scores"""
        self.turn = 0



