# TkPicture.py
#
# I. H. McCreery
# 1 February 2011

from PIL import ImageTk
from Tkinter import Tk, Label

def main(im):

    # self.root is the Tk instance for displaying image
    root = Tk()

    # self.imagetk represents a PhotoImage instance for use with
    # Tkinter.  Must come after instantiation of self.root or will
    # throw
    # RuntimeError, 'Too early to create image'
    imagetk = ImageTk.PhotoImage(im)

    # self.label is the Tk label widget for displaying image
    label = Label(root, image=imagetk, borderwidth=0)
    label.pack()

    def tick():
        label.config(image=imagetk)
        print "tick."
        label.after(200, tick)

    tick()
    root.mainloop()
