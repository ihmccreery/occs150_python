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

from PIL import Image, ImageDraw

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
        self.penWidth = 1 #for the drawline method, this has to be an int
        self.penUp = False
        self.penDirection = 0.0
        self.penColor = "black"

        # self.im represents the drawing surface
        self.im = Image.new('RGB', (width, height), bg_color)

        #it seems that we have to initialize a separate imagedraw item to draw
        self.draw = ImageDraw.Draw(self.im)

    def getWidth(self):
        return self.im.size[0]

    def getHeight(self):
        return self.im.size[1]

    def close(self):
        # This is probably something we'll need to impliment in Tkinter
        pass

    """These get color methods may not be necessary:

    def getPixelRed(self, x, y):
        Returns an integer (0-255), the red value at (x, y).
        return self.im.getpixel((x,y))[0]

    def getPixelGreen(self, x, y):
        Returns an integer (0-255), the green value at (x, y).
        return self.im.getpixel((x,y))[1]

    def getPixelBlue(self, x, y):
        Returns an integer (0-255), the blue value at (x, y).
        return self.im.getpixel((x,y))[2]
        
        """

    """This may be the only necessary getColor method."""
    def getPixelColor(self, x, y):
        #returns a tuple with (R, G, B) values at (x, y)
        return self.im.getpixel((x,y))

    def setPixelRed(self, x, y, r):
        """Sets the red value of (x, y) to the given value.
        Leaves other values alone"""

        color = self.im.getpixel((x, y))
        newColor = (r, color[1], color[2])
        self.im.putpixel((x, y), newColor)

    def setPixelGreen(self, x, y, g):
        """Sets the green value of (x, y) to the given value.
        Leaves other values alone"""

        color = self.im.getpixel((x, y))
        newColor = (color[0], g, color[2])
        self.im.putpixel((x, y), newColor)

    def setPixelBlue(self, x, y, b):
        """Sets the blue value of (x, y) to the given value.
        Leaves other values alone"""

        color = self.im.getpixel((x, y))
        newColor = (color[0], color[1], b)
        self.im.putpixel((x, y), newColor)


    def setPixelColor(self, x, y, r, g, b):
        """Sets the r, g, and b values of (x, y) to the given values."""
        color = (r, g, b)
        self.im.putpixel((x, y), color)

    def writeFile(self, S):
        #we should figure out what kind of filetypes this supports, .bmp works
        """S must be a string describing the filename the image should
        be saved as."""
        self.im.save(S)

    def errorManagement(self, f):   #not sure if this is necessary
        pass


    """I'm not so sure about how to deal with colors, since we have tuples here.
    My thought is that we need only one 'getColor' method, because we can just
    get the tuple that way and choose with component we want. However, setting
    the colors is a little trickier because tuples don't allow you to assign values,
    in other words you can't say colors[0] = r, because tuples are immutable. This
    tells me that maybe we'll need individual methods to set each component color."""
    
    def setPenColor(self, color):
        """Color should be a string in any of the formats described earlier."""
        self.penColor = color

    def getPenColor(self):
        return self.penColor
    
    def setPenWidth(self, penWidth):
        #penWidth should be an int
        self.penWidth = penWidth

    def getPenWidth(self):
        return self.penWidth

    """I don't think we need these:

    def getPenRed(self):    
        pass

    def getPenGreen(self):
        pass

    def getPenBlue(self):
        pass
        
        """
    """These may be hard to implement, since we're allowing the pen to be
    either in RGB format, simple color name format, or any of the others.
    Maybe we should just specify that this only works if your pen is in RGB
    format. I'm unclear as to how we should implement the color variable of
    the pen"""
    def setPenRed(self, r):
        pass

    def setPenGreen(self, g):
        pass

    def setPenBlue(self, b):
        pass

    def setPenColor(self, r, g, b):
        pass

    def drawLine(self, x1, y1, x2, y2):
        self.draw.line((x1, y1, x2, y2), fill = self.penColor, width = self.penWidth)

    def drawLineTo(self, x, y):
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

    #the rest of the Picture class is for mouse movements, and key pressing

    
