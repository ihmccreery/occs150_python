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

from PIL import Image, ImageColor, ImageDraw

class Picture(object):
    """A picture object

Picture(width, height, bg_color='#ffffff') -> Picture object

width and height must be integers.

bg_color is optional, defaults to white

all color arguments support the following color formats:

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

        self.pen_xy = (0, 0)
        self.pen_width = 1.0
        # self.pen_Up = False # what does this do?
        self.pen_dir = 0.0
        self.pen_color = (0, 0, 0)

        # self.im represents canvas
        self.im = Image.new('RGB', width, height, bgcolor)

        # self.draw represents drawing capabilities
        self.draw = ImageDraw.Draw(self.im)

    def write_file(self, name):
        """Saves to a file. name is a string."""
        self.im.save(name)

    def close(self):
        # This is probably something we'll need to impliment in Tkinter
        pass

    def get_width(self):
        return self.im.size[0]

    def get_height(self):
        return self.im.size[1]


    # The following methods' implimentations are slightly different
    # because of Python's tuple capabilities. Rather than taking a
    # separate argument for each value, they are taken and returned as
    # tuples.


    # Pixel methods

    def get_pixel_color(self, xy):
        """Returns the pixel color of given pixel in the form (r, g, b)
where r, g, and b are integers (0-255)."""
        return self.im.getpixel(xy)

    def set_pixel_color(self, xy, color):
        """Sets the pixel color of given pixel in the form (r, g, b)
where r, g, and b are integers (0-255)."""
        self.im.setpixel(xy, color)


    # Pen methods

    def set_pen_xy(self, xy):
        """Sets pen position to xy. xy is a tuple of two ints"""
        # perhaps we should assert more restrictions here?
        self.pen_xy = xy

    def get_pen_xy(self):
        """Returns current pen position (a tuple of 2 ints)."""
        return self.pen_xy

    def set_pen_color(self, color):
        """Sets the pen color. Takes the usual types of color args."""
        color = ImageColor.getrgb(color) # converts to standard tuple
        self.pen_color = color

    def get_pen_color(self):
        return self.pen_color

    def set_pen_dir(self, d):
        """Sets the pen direction. Takes a number as an argument."""
        self.pen_dir = d

    def pen_rotate(self, d):
        """Rotates the pen dir. Takes a number as an argument."""
        self.pen_dir += d

    def get_pen_dir(self):
        return self.pen_dir

    def set_pen_width(self, w):
        assert w > 0, "Width must be greater than 0"
        self.pen_width = w

    def get_pen_width(self):
        return self.pen_width

    def draw_line(self, xy1, xy2=None, color=None, width=None):
        """Draws a line from xy1 to xy2, or from current pen position to
xy1 if no xy2 is given, and sets pen position to ending point and
sets pen color to color"""

        # if no xy2 is given, orient so line will be drawn from current
        # position
        if not xy2:
            xy2 = xy1
            xy1 = self.pen_xy

        # if no color is given, set color to current pen color
        if not color:
            color = self.pen_color

        # if no width is given, set width to current pen width
        if not width:
            width = self.pen_width

        # execute draw_line from 1 to 2
        # width is divided by 2 to correct for problem with PIL.
        # should be changed when PIL 1.6 comes out
        self.draw.line([xy1, xy2], color=color, width=width/2)

        # set attributes accordingly
        self.set_pen_xy(xy2)
        self.set_pen_color(color)
        self.set_pen_width(width)

    def drawForward(self, dist):
        pass


    # Shape drawing methods

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

    def fillPoly(self, X, Y, n): #X and Y will probably have to be tuples
        pass

    #the rest of the Picture class is for mouse movements, and key pressing

