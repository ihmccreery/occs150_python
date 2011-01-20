#PicClient.py
#Alex Amlie-Wolf
#This is my program for messing around with the Picture class to see how things work

from Picture import Picture

def main():
    pic = Picture(500, 500, bg_color="rgb(255, 200, 150)")
    """print pic.getWidth()
    print pic.getHeight()
    print pic.getPixelRed(250, 250)
    print pic.getPixelGreen(250, 250)
    print pic.getPixelBlue(250, 250)
    pic.setPixelRed(240, 240, 100)
    pic.setPixelGreen(240, 240, 140)
    pic.setPixelBlue(240, 240, 200)
    print pic.getPixelRed(240, 240)
    print pic.getPixelGreen(240, 240)
    print pic.getPixelBlue(240, 240)
    print pic.getPixelColor(240, 240)
    pic.setPixelColor(240, 240, 50, 60, 75)
    print pic.getPixelColor(240, 240)
    pic.writeFile("test.bmp")"""
    pic.drawLine(20, 20, 50, 50)
    

main()
