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

from PIL import Image, ImageDraw, ImageColor

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

        self._penX = 0
        self._penY = 0
        self._penWidth = 1 #for the drawline method, this has to be an int
        self._penUp = False
        self._penDirection = 0.0
        self._penColor = "black"

        # self.im represents the drawing surface
        self.im = Image.new('RGB', (width, height), bg_color)

        #it seems that we have to initialize a separate imagedraw item to draw
        self.draw = ImageDraw.Draw(self.im)

    def get_width(self):
        return self.im.size[0]

    def get_height(self):
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
    def get_pixel_color(self, x, y):
        #returns a tuple with (R, G, B) values at (x, y)
        return self.im.getpixel((x,y))

    def set_pixel_red(self, x, y, r):
        """Sets the red value of (x, y) to the given value.
        Leaves other values alone"""

        color = self.im.getpixel((x, y))
        newColor = (r, color[1], color[2])
        self.im.putpixel((x, y), newColor)

    def set_pixel_green(self, x, y, g):
        """Sets the green value of (x, y) to the given value.
        Leaves other values alone"""

        color = self.im.getpixel((x, y))
        newColor = (color[0], g, color[2])
        self.im.putpixel((x, y), newColor)

    def set_pixel_blue(self, x, y, b):
        """Sets the blue value of (x, y) to the given value.
        Leaves other values alone"""

        color = self.im.getpixel((x, y))
        newColor = (color[0], color[1], b)
        self.im.putpixel((x, y), newColor)


    def set_pixel_color(self, x, y, r, g, b):
        """Sets the r, g, and b values of (x, y) to the given values."""
        color = (r, g, b)
        self.im.putpixel((x, y), color)

    def write_file(self, S):
        #we should figure out what kind of filetypes this supports, .bmp works
        """S must be a string describing the filename the image should
        be saved as."""
        self.im.save(S)

    def error_management(self, f):   #not sure if this is necessary
        pass


    """I'm not so sure about how to deal with colors, since we have tuples here.
    My thought is that we need only one 'getColor' method, because we can just
    get the tuple that way and choose with component we want. However, setting
    the colors is a little trickier because tuples don't allow you to assign values,
    in other words you can't say colors[0] = r, because tuples are immutable. This
    tells me that maybe we'll need individual methods to set each component color."""
    
    def set_pen_color(self, color):
        """Color should be a string in any of the formats described earlier."""
        color = ImageColor.getrgb(color)
        self._penColor = color

    def get_pen_color(self):
        """Returns pen color as an RGB tuple"""
        return self._penColor
    
    def set_pen_width(self, penWidth):
        #penWidth should be an int
        self._penWidth = penWidth

    def get_pen_width(self):
        return self._penWidth
    
    def set_pen_red(self, r):
        newColor = (r, _penColor[1], _penColor[2])
        im.set_pen_color(newColor)

    def set_pen_green(self, g):
        newColor = (_penColor[0], g, _penColor[2])
        im.set_pen_color(newColor)

    def set_pen_blue(self, b):
        newColor = (_penColor[0], _penColor[1], b)
        im.set_pen_color(newColor)


    def draw_line(self, x1, y1, x2, y2):
        """Draws a line from (x1, y1) to (x2, y2) with the current pen color and width."""
        self.draw.line((x1, y1, x2, y2), fill = self._penColor, width = self._penWidth)

    def draw_line_to(self, x, y):
        """Draws a line from the current position to (x,y) with the current pen color and width."""
        self.draw.line((_penX, _penY, x, y), fill = self._penColor, width = self._penWidth)

    def draw_circle(self, x, y, radius):
        """Draws a circle at (x, y) with the given radius with the current pen color."""
        self.draw.ellipse((x-radius, y-radius, x+radius+1, y+radius+1), outline=self._penColor)

    def draw_circle_fill(self, x, y, radius):
        """Draws a circle at (x, y) with the given radius filled with the current pen color."""
        self.draw.ellipse((x-radius, y-radius, x+radius+1, y+radius+1), fill=self._penColor, outline=self._penColor)

    def draw_ellipse(self, x, y, minor, major):
        """Draws an ellipse at (x, y) with the given minor and major axes with the current pen color."""
        self.draw.ellipse((x-minor, y-major, x+minor, y+major), outline=self._penColor)

    def draw_ellipse_fill(self, x, y, minor, major):
        """Draws an ellipse at (x, y) with the given minor and major axes filled with the current pen color."""
        self.draw.ellipse((x-minor, y-major, x+minor, y+major), fill=self._penColor, outline=self._penColor)

    def draw_rect(self, x, y, w, h):
        """Draws a rectangle with top left corner (x, y) of width w and height h in the current pen color."""
        self.draw.rectangle((x, y, x+h, y+h), outline=self._penColor)

    def draw_rect_fill(self, x, y, w, h):
        """Draws a rectangle with top left corner (x, y) of width w and height h filled with the current pen color."""
        self.draw.rectangle((x, y, x+h, y+h), fill=self._penColor, outline=self._penColor)

    def draw_pixel(self, x, y):
        """Draws a pixel at point (x, y) with the current pen color."""
        self.draw.point((x, y), fill=self._penColor)

    """Not really sure what these pen up things are for:
    def set_pen_up(self):      
        pass

    def set_pen_down(self): 
        pass

    def is_pen_up(self):
        pass
    """

    def set_x(self, x):
        """Sets the pen's x coordinate to x."""
        self._penX = x

    def set_y(self, y):
        """Sets the pen's y coordinate to y."""
        self._penY = y

    def get_x(self):
        """Returns the current x coordinate of the pen."""
        return self._penX

    def get_y(self):
        """Returns the current y coordinate of the pen."""
        return self._penY

    def set_position(self, x, y):
        """Sets the coordinates of the pen to (x, y)."""
        self._penX = x
        self._penY = y

    def set_direction(self, d):
        """Sets the pen's direction to d."""
        self._penDirection = d

    def rotate(self, d):
        """Rotates the current pen direction by d degrees."""
        self._penDirection += d

    def get_direction(self):
        """Returns the current pen direction."""
        return self._penDirection

    def draw_forward(self, dist):
        pass

    def fill_poly(self, coord_list):    #I'm not sure this is working correctly.
        """This draws a polygon, using coord_list, which is a tuple of tuples. In other words, you pass in a
        tuple filled with all the (x,y) coordinates you want for the vertices of your polygon. This will draw
        that polygon filled with the current pen color."""
        self.draw.polygon(coord_list, outline=self._penColor, fill=self._penColor)

    #the rest of the Picture class is for mouse movements, and key pressing

    
