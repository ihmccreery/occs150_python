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

        # self.im represents the drawing surface
        self.im = Image.new('RGB', width, height, bgcolor)
