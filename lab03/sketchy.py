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
    im = Image.new('RGB', CANVAS_SIZE, (127, 0, 0))
    draw = ImageDraw.Draw(im)
    draw.chord((20, 20, 40, 40), 0, 180, (0, 0, 0))
    draw.chord((90, 20, 180, 100), 0, 180, (0, 0, 0))
    im.show()

main()
