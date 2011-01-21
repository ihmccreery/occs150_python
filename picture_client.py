from Picture import Picture

size = (600, 600)
p = Picture(size, bg_color=(200, 0, 0))
p.draw_line((0, 0), (100, 100))
# p.draw_forward(100, direction=1)
p.show()
