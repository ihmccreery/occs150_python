# sketchy.py
# draws a picture and saves it to the current directory
# 
# I. H. McCreery
# 10 January 2010

from PIL import Image, ImageDraw

CANVAS_SIZE = (800, 800)

def main():
    # Assign/initialize image
    im = Image.new('RGB', CANVAS_SIZE, (255, 255, 255))
    im.show()

main()
