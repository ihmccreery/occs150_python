#PicClient.py
#Alex Amlie-Wolf
#This is my program for messing around with the Picture class to see how things work

from PictureAlex import Picture

def main():
    pic = Picture(500, 500, bg_color="rgb(255, 200, 150)")
    pic.set_pen_color("black")
    pic.fill_poly(((25, 25), (50, 50), (75, 75)))
    pic.write_file("test.bmp")
    

main()
