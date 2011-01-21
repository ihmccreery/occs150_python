from Picture import Picture

size = (600, 600)
p = Picture(size, bg_color=(200, 0, 0))
p.draw_line(xy1=(0, 0), xy2=(100, 100))
p.draw_forward(dist=100, direction=1, width=3)
p.show()
