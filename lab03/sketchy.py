# sketchy.py
# draws a picture and saves it to the current directory
#
# I. H. McCreery
# 10 January 2010

from PIL import Image, ImageDraw, ImageTk
import Tkinter

CANVAS_SIZE = (400, 400)

def main():
    # Assign/initialize image
    im = image('RGB', CANVAS_SIZE, (127, 0, 0))
    # im.draw.ellipse([(50, 50), (100, 100)], outline=(255, 255, 255), fill=(0, 0, 0))
    im.show()

class image(Image.Image):

    def __init__(self, mode, size, color):
        self = Image.new(mode, size, color)
        self.root = Tkinter.Tk()
        self.draw = ImageDraw.Draw(self)
        self.tk_label_im = None

    def display(self):
        tk_im = ImageTk.PhotoImage(self)
        self.tk_label_im = Tkinter.Label(self.root, image=tk_im)

main()
