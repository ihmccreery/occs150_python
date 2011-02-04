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

import math
from PIL import Image, ImageColor, ImageDraw, ImageTk
import Tkinter
import threading

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

    def __init__(self, size, bg_color='white'):

        self.pen_xy = (0, 0)
        self.pen_width = 1
        # self.pen_Up = False # what does this do?
        self.pen_direction = 0.0 # in radians
        self.pen_color = (0, 0, 0)
        self.fill_color = (0, 0, 0)

        # self.im represents canvas
        self.im = Image.new('RGB', size, bg_color)

        # self.draw represents drawing capabilities
        self.draw = ImageDraw.Draw(self.im)

        self.imtk = PictureTk(self.im)
        self.imtk.start()

    def write_file(self, name):
        """Saves to a file. name is a string."""
        self.im.save(name)

    def show(self):
        """Shows image in default external viewer."""
        self.im.show()

    def close(self):
        # This is probably something we'll need to impliment in Tkinter
        pass


    # Rather than defining separate get_x and get_y, just return tuple
    # with two values

    def get_size(self):
        return self.im.size


    # The following methods' implimentations are slightly different than
    # Java because of Python's tuple capabilities. Rather than taking a
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
        self.im.putpixel(xy, color)
        self.im.setpixel(xy, color)


    # Pen methods

    # XY

    def set_pen_xy(self, xy):
        """Sets pen position to xy. xy is a tuple of two ints"""
        # perhaps we should assert more restrictions here?
        self.pen_xy = xy

    def get_pen_xy(self):
        """Returns current pen position (a tuple of 2 ints)."""
        return self.pen_xy

    # Color

    def set_pen_color(self, color):
        """Sets the pen color. Takes the usual types of color args."""
        if type(color) == str:
            color = ImageColor.getrgb(color) # converts to standard tuple
        self.pen_color = color

    def get_pen_color(self):
        return self.pen_color

    def set_fill_color(self, color):
        """Sets thhe pen color. Takes the usual types of color args."""
        if type(color) == str:
            color = ImageColor.getrgb(color) # converts to standard tuple
        self.fill_color = color

    def get_fill_color(self):
        return self.fill_color

    # Direction

    def set_pen_direction(self, d):
        """Sets the pen direction.  Takes a number as an argument."""
        self.pen_direction = d

    def pen_rotate(self, d):
        """Rotates the pen dir.  Takes a number as an argument."""
        self.pen_direction += d

    def get_pen_direction(self):
        return self.pen_direction

    # Width

    def set_pen_width(self, w):
        assert w > 0, "Width must be integer greater than 0"
        self.pen_width = int(w)

    def get_pen_width(self):
        return self.pen_width

    # Drawing

    def draw_line(self, xy1, xy2=None, color=None, width=None):
        """Draws a line from xy1 to xy2, or from current pen position to
        xy1 if no xy2 is given, and sets pen position to ending point and
        sets pen color to color
        """

        # if no xy2 is given, orient so line will be drawn from current
        # position
        if not xy2:
            xy2 = xy1
            xy1 = self.get_pen_xy

        # if no color is given, set color to current pen color
        if color:
            self.set_pen_color(color)

        # if no width is given, set width to current pen width
        if width:
            self.set_pen_width(width)

        # execute draw_line from 1 to 2
        # width is divided by 2 to correct for problem with PIL.
        self.draw.line([xy1, xy2], fill=self.get_pen_color(), width=self.get_pen_width())

        # set attributes accordingly
        self.set_pen_xy(xy2)

    def draw_forward(self, dist, xy=None, color=None, width=None, direction=None):
        """Draws a line from current position of length dist and at angle
        direction.
        """

        # if no xy is given, orient so line will be drawn from current
        # position
        if xy:
            self.set_pen_xy(xy)

        xy1 = self.get_pen_xy()

        # if no direction is given, set direction to current pen
        # direction
        if direction:
            self.set_pen_direction(direction)

        xy2 = (int(xy1[0] + dist * math.sin(self.get_pen_direction())),
               int(xy1[1] + dist * math.cos(self.get_pen_direction())))

        self.draw_line(xy1=xy1, xy2=xy2, color=color, width=width)


    # Shape drawing methods

    def draw_ellipse(self, center, a, b=None, pen_color=None, fill=None):
        """Draws an ellipse with center at center and radii of a
        (horizontal) and b (vertical).

        If no b radius is given, draws a circle.
        """

        if not b:
            b = a

        self._set_shape_colors(pen_color, fill)

        xy1 = (center[0] - a, center[1] - b)
        xy2 = (center[0] + a, center[1] + b)

        self.draw.ellipse([xy1, xy2], outline=self.get_pen_color(), fill=self.get_fill_color())

    def draw_rect(self, xy, x_side, y_side=None,
                  pen_color=None, fill=None):
        """Draws a rectangle with top-right corner at xy and sides of
        x_side (horizontal) and y_side (vertical).

        If no y is given, draws a square.
        """

        if not y_side:
            y_side = x_side

        self._set_shape_colors(pen_color, fill)

        xy1 = xy
        xy2 = (xy1[0] + x_side, xy1[1] + y_side)

        self.draw.rectangle([xy1, xy2], outline=self.get_pen_color(), fill=self.get_fill_color())

    def draw_poly(self, xy, pen_color=None, fill=None):
        """Draws a polygon with coordinates defined in xy (a list) and
        options as above.
        """

        self._set_shape_colors(pen_color, fill)

        self.draw.polygon(xy, outline=self.get_pen_color(), fill=self.get_fill_color())

    def _set_shape_colors(self, pen_color, fill):
        if pen_color != None:
            self.set_pen_color(pen_color)

        if fill != None:
            self.set_fill_color(fill)

class PictureTk(threading.Thread):

    def __init__(self, im):
        threading.Thread.__init__(self)
        self.root = Tkinter.Tk()
        self.label = Tkinter.Label(self.root,
                                   borderwidth=0)
        self.label.pack()

    def run(self):
        self.root.wait_variable(self.label)
