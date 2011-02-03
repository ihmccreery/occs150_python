# critter_test.py
#
# I. H. McCreery
# 2 February 2011
"""A way to test critters"""

from stone import Stone
from mouse import Mouse

s = Stone(2, 4)
m = Mouse(3, 5)
print s.move()
print m.color()
print s.x
print m.y
