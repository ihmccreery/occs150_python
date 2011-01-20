# Picture.py
# 19 January 2010
# I. H. McCreery and Alex Amlie-Wolf
"""A picture object

This module aims to provide students with an easily-accessible, versatile
tool for learning basic computer science skills with a visual
representation.

Must have PIL installed on Python path or otherwise accessible in working
directory.
"""

from PIL import Image

class Picture(object):
    """A picture object

    Picture(width, height, bg_color='#ffffff') -> Picture object

    width and height must be integers.

    bg_color is optional, defaults to white, and supports the following
    color formats:
       -Hexadecimal color specifiers, given as "#rgb" or "#rrggbb". For
        example, "#ff0000" specifies pure red.
       -RGB functions, given as "rgb(red, green, blue)" where the colour
        values are integers in the range 0 to 255. Alternatively, the
        color values can be given as three percentages (0% to 100%). For
        example, "rgb(255,0,0)" and "rgb(100%,0%,0%)" both specify pure
        red.
       -Hue-Saturation-Lightness (HSL) functions, given as "hsl(hue,
        saturation%, lightness%)" where hue is the colour given as an
        angle between 0 and 360 (red=0, green=120, blue=240), saturation
        is a value between 0% and 100% (gray=0%, full color=100%), and
        lightness is a value between 0% and 100% (black=0%, normal=50%,
        white=100%). For example, "hsl(0,100%,50%)" is pure red.
       -Common HTML colour names. The ImageDraw provides some 140 standard
        colour names, based on the colors supported by the X Window system
        and most web browsers. Colour names are case insensitive, and may
        contain whitespace. For example, "red" and "Red" both specify pure
        red.
    """

    def __init__(self, width, height, bg_color='white'):

        self.penX = 0.0
        self.penY = 0.0
        self.penWidth = 1.0
        self.penUp = False
        self.penDirection = 0.0
        self.penColor = "black"

        # self.im represents the drawing surface
        self.im = Image.new('RGB', width, height, bgcolor)

    def getWidth(self):
        return self.im.size[0]

    def getHeight(self):
        return self.im.size[1]

    def close(self):
        # This is probably something we'll need to impliment in Tkinter
        pass

    def getPixelRed(self, x, y):
        """Returns an integer (0-255), the red value at (x, y)."""
        return self.im.getpixel((x,y))[0]

    def getPixelGreen(self, x, y):
        """Returns an integer (0-255), the green value at (x, y)."""
        return self.im.getpixel((x,y))[1]

    def getPixelBlue(self, x, y):
        """Returns an integer (0-255), the blue value at (x, y)."""
        return self.im.getpixel((x,y))[2]

    def setPixelRed(self, x, y, r):
        """Sets the red value of (x, y) to the given value.
        Leaves other values alone"""

        color = self.im.getpixel((x, y))
        color[0] = r
        self.im.putpixel((x, y), color)

    def setPixelGreen(self, x, y, g):
        """Sets the green value of (x, y) to the given value.
        Leaves other values alone"""

        color = self.im.getpixel((x, y))
        color[1] = g
        self.im.putpixel((x, y), color)

    def setPixelBlue(self, x, y, b):
        """Sets the blue value of (x, y) to the given value.
        Leaves other values alone"""

        color = self.im.getpixel((x, y))
        color[2] = b
        self.im.putpixel((x, y), color)

    def getPixelColor(self, x, y):
        pass

    def setPixelColor(self, x, y, r, g, b):
        pass

    def writeFile(self, S):
        pass

    def errorManagement(self, f):   #not sure if this is necessary
        pass

    def setPenColor(self, c):   #C is a color, we could also use RGB
        pass

    def getPenColor(self):
        pass

    def drawLine(self, x1, y1, x2, y2):
        pass

    def drawLine(self, x, y):
        pass

    def drawCircle(self, x, y, radius):
        pass

    def drawCircleFill(self, x, y, radius):
        pass

    def drawEllipse(self, x, y, minor, major):
        pass

    def drawEllipseFill(self, x, y, minor, major):
        pass

    def drawRect(self, x, y, w, h):
        pass

    def drawRectFill(self, x, y, w, h):
        pass

    def drawPixel(self, x, y):
        pass

    def setPenUp(self): #not entirely sure what this is for
        pass

    def setPenDown(self):   #this either
        pass

    def isPenUp(self):
        pass

    def setX(self, x):
        pass

    def setY(self, y):
        pass

    def getX(self):
        pass

    def getY(self):
        pass

    def setPosition(self, x, y):
        pass

    def setDirection(self, d):
        pass

    def rotate(self, d):
        pass

    def getDirection(self):
        pass

    def drawForward(self, dist):
        pass

    def fillPoly(self, X, Y, n):    #X and Y will probably have to be tuples
        pass

    def setPenWidth(self, pWidth):
        pass

    def getPenWidth(self):
        pass

    def getPenRed(self):    #not sure if we need these
        pass

    def getPenGreen(self):
        pass

    def getPenBlue(self):
        pass

    def setPenRed(self, r):
        pass

    def setPenGreen(self, g):
        pass

    def setPenBlue(self, b):
        pass

    def setPenColor(self, r, g, b):
        pass

    #the rest of the Picture class is for mouse movements, and key pressing

    
